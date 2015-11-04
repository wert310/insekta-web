import time
import base64
import hashlib
import hmac
import struct

from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from .bundlebuilder import write_vpn_bundle
from ..pki.models import Certificate


@login_required
def index(request):
    certificates = Certificate.objects.filter(user=request.user)
    has_valid_certificate = any(cert.is_valid for cert in certificates)
    code = _generate_download_code(request.user.pk)
    return render(request, 'vpn/index.html', {
        'has_valid_certificate': has_valid_certificate,
        'code': code
    })

# This does not have login_required because the authentication can also be
# done using a code in the URL to be friendly to wget.
def download_bundle(request, code):
    if request.user.is_authenticated():
        user = request.user
    else:
        try:
            user_id = _unpack_download_code(code)
        except ValueError:
            raise PermissionDenied()
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)

    resp = HttpResponse(content_type='application/x-tgz')
    write_vpn_bundle(user, resp)
    return resp


def _generate_download_code(user_id):
    gen_time = int(time.time()) // 60
    data = struct.pack('!II', user_id, gen_time)
    return base64.b32encode(data + _download_code_mac(data)).decode().lower()


def _unpack_download_code(code):
    data = base64.b32decode(code.upper().encode())
    if len(data) != 40:
        raise ValueError('Invalid code length')
    data, given_mac = data[:8], data[8:]
    real_mac = _download_code_mac(data)
    if not hmac.compare_digest(given_mac, real_mac):
        raise ValueError('Invalid code')
    user_id, gen_time = struct.unpack('!II', data)
    ten_minutes = 600
    if gen_time * 60 + ten_minutes < time.time():
        raise ValueError('Code expired')
    return user_id


def _download_code_mac(data):
    return hmac.new(settings.SECRET_KEY.encode(), b'vpn-download:' + data,
                    hashlib.sha256).digest()