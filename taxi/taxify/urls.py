from django.conf.urls import url
form . import views


urlpatterns=[
    url('^$',views.index,name = 'index'),
]