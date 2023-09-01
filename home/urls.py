
from django.urls import path
from home import igdownloader
from home import home
from home import downloadprof
from home import hastag
from home import postDownloader
from home import post


urlpatterns = [
    path('insta', post.posts),
    # path('homepage',home.homepage),
    path('',home.homepage),
    path('profile',downloadprof.downloadprof),
    # path("hashtag",hastag.download_hashtag_posts),

]
