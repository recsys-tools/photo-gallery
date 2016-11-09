"""gallery_with_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import RedirectView
from gallery_with_django import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/0')),
    url(r'^(?P<page_id>\d+)/$', views.index),

    url(r'^select_images/$', RedirectView.as_view(url='/select_images/0')),
    url(r'^select_images/(?P<page_id>\d+)/$', views.select_images),

    url(r'^image-list-delete/$', views.delete_images),
    # url(r'^test/$', RedirectView.as_view(url='/static/web/test.html')),
    # url(r'^$', TemplateView.as_view(template_name='homepage.html')),
]

