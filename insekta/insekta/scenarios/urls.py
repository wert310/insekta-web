from django.conf.urls import url

from insekta.scenarios import views


app_name = 'scenarios'
urlpatterns = [
    url(r'^topiclist$', views.index, name='index'),
    url(r'^challenges$', views.index, kwargs={
        'is_challenge': True
    }, name='challenges'),
    url(r'^view/(.+)/(.+)$', views.view, name='view'),
    url(r'^download/(.+)/(.+)/(.+)/(.+)$', views.download, name='download'),
    url(r'^vms/enable/(.+)/(.+)$', views.enable_vms, name='enable_vms'),
    url(r'^vms/disable/(.+)/(.+)$', views.disable_vms, name='disable_vms'),
    url(r'^vms/ping/(.+)$', views.ping_vms, name='ping_vms'),
    url(r'^save_notes/(.+)$', views.save_notes, name='save_notes'),
    url(r'^save_comments_state$', views.save_comments_state, name='save_comments_state'),
    url(r'^get_comments/(.+)$$', views.get_comments, name='get_comments'),
    url(r'^preview_comment$', views.preview_comment, name='preview_comment'),
    url(r'^save_comment/(.+)$', views.save_comment, name='save_comment'),
    url(r'^courses/$', views.list_courses, name='list_courses'),
    url(r'^courses/(.+)/topiclist$', views.view_course, name='view_course'),
    url(r'^courses/(.+)/challenges$', views.view_course, kwargs={
        'is_challenge': True
    }, name='view_course_challenges'),
    url(r'^courses/(.+)/registration$', views.course_registration,
        name='course_registration'),
    url(r'^courseruns/(.+)/allpoints$', views.courserun_points,
        name='courserun_points'),
    url(r'^courseruns/(.+)/points$', views.courserun_points_participant,
        name='courserun_points_participant'),
    url(r'^options/(.+)/(.+)$', views.show_options, name='show_options'),
    url(r'^reset_tasks/(.+)/(.+)$', views.reset_tasks, name='reset_tasks'),
]
