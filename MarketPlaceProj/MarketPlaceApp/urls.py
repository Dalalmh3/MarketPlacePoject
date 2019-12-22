from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^add_product$', views.add_product),
     url(r'^create_product$', views.create_product),
    url(r'^upload_file$', views.upload_file),
]