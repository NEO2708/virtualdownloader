
from django.urls import path
from home import igdownloader
from home import home
from home import downloadprof


urlpatterns = [
    path('insta',igdownloader.InstaDownloader ),
    path('homepage',home.homepage),
    path('',home.homepage),
    path('igprofile',downloadprof.downloadprof)
]
