from django.conf.urls import url
from . import views
app_name='trvapp'
urlpatterns = [
    url(r'^$',views.all_contry,name='all_contr'),
    url(r'^(?P<slug>[-\w]+)$',views.detail_contry,name='detail_contry'),
    url(r'^(?P<slug>[-\w]+)/pictuers$',views.image_contry,name='image_contry'),
    url(r'^(?P<slug>[-\w]+)/history$',views.history_contry,name='history_contry'),
    url(r'^(?P<slug>[-\w]+)/wather-geography$',views.wather_geograohy,name='wather_geograohy'),
    url(r'^(?P<slug>[-\w]+)/Image-Food$',views.Image_food,name='Image_food'),
    ]
