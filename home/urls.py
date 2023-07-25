
from django.urls import path
from home import igdownloader
from home import home
from home import downloadprof
from home import hastag


urlpatterns = [
    path('insta',igdownloader.InstaDownloader ),
    path('homepage',home.homepage),
    path('',home.homepage),
    path('igprofile',downloadprof.downloadprof),
    path("hashtag",hastag.download_hashtag_posts)
]
