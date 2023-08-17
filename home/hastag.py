from rest_framework.response import Response
from rest_framework.decorators import api_view
import instaloader

@api_view()

def download_hashtag_posts(request):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    L.login("insta.botnew", "instabot001")

    hashtag= request.GET['link']
    # max_count=100
    strem=[]

    # Define a function to filter posts by hashtag
    def filter_hashtag_post(post):
        return hashtag in post.caption_hashtags

    # Get posts with the specified hashtag
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

    # Download posts with the specified hashtag
    # count = 0
    for post in posts:
        if filter_hashtag_post(post):
            # L.download_post(post, target=f"{hashtag}_posts")
            hash=post.url
            strem.append(hash)
            # count += 1

        # if count >= max_count:
        #     break

    return Response(strem)


