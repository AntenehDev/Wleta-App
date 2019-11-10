from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path('add_wleta/', views.add_wleta),
  path('delete_wleta/<int:wleta_id>/', views.delete_wleta),
]
