from django.conf.urls import url
from . import views
app_name='tavelfetuers'
urlpatterns = [
    url(r'^$',views.all_fetuers,name='all_fetuers'),
    url(r'^(?P<slug>[-\w]+)',views.all_detail,name='all_detail'),
]
