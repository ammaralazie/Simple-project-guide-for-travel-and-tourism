from django.conf.urls import url
from . import views
app_name='foodanddrink'
urlpatterns = [
url(r'^$',views.all_food_and_drink,name='all_food_and_drink'),
url(r'^(?P<slug>[-\w]+)$',views.det_food,name='det_food'),

]
