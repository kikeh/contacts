from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/company', views.create_company, name='create_company'),
    url(r'^show/company/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.show_company, name='show_company'),
    url(r'^create/category', views.create_category, name='create_category'),
]
