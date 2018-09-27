"""Chronicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from TTS.views import gtts
from GooglePlay.views import upload_apk_via_url, download_apk_via_url, GooglePlay
from views import Dashboard, downloadcv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Dashboard, name='index'),
    url(r'^TTS/$', gtts, name='gtts'),
    url(r'^GooglePlay/$', GooglePlay, name="GooglePlay"),
    url(r'^upload_binary_url/$', upload_apk_via_url, name="upload_binary_url"),
    url(r'^downloadcv/$',downloadcv,name="downloadcv")
]
