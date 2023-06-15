from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about_page, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),

] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)