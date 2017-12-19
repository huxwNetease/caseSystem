from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/wordmenu',views.showWordMenu),
    url(r'^index/picturemenu',views.showPictureMenu),
    url(r'^index/voicemenu',views.showVoiceMenu),
    url(r'^index/homemenu',views.showHomeMenu),
]