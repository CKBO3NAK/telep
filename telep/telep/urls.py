"""
URL configuration for telep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tele.views import *
import django.views.static
from django.conf.urls.static import static
from telep import settings
from django.views.generic import TemplateView
urlpatterns = [
    path ('home', home),
    path('', adminka),
    path('<int:pk>',ShowArticle.as_view(),name = "showArticle"),
    path('admin/', admin.site.urls),
    path('upload/', post),
    path('tele', telegraph),
    path('test', post),
    path('check', check),
    path(r'^$', TemplateView.as_view(template_name="test.html"), name='whatever'),
    path(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound
handler500 = some_view