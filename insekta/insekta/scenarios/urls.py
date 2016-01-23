from django.conf.urls import url

from insekta.scenarios import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dontdespair$', views.index, kwargs={
        'is_challenge': True
    }, name='challenges'),
    url(r'^view/(.+)$', views.view, name='view'),
    url(r'^vms/enable/(.+)$', views.enable_vms, name='enable_vms'),
    url(r'^vms/disable/(.+)$', views.disable_vms, name='disable_vms'),
    url(r'^vms/ping/(.+)$', views.ping_vms, name='ping_vms'),
    url(r'^save_notes/(.+)$', views.save_notes, name='save_notes'),
    url(r'^save_comments_state$', views.save_comments_state, name='save_comments_state'),
    url(r'^get_comments/(.+)$$', views.get_comments, name='get_comments'),
]
