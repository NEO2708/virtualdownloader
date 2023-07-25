from rest_framework.response import Response
from rest_framework.decorators import api_view
import instaloader

@api_view()

def downloadprof(request):
    L = instaloader.Instaloader()
    stream=[]
    username = request.GET['link']
    
    L.login("insta.botnew", "instabot001")
    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    users = set()
    for post in posts:
        # L.download_post(post, 'msf.inc')
        # users.add(post.owner_profile)
        js={"Url":post.url,"Caption":post.caption,"Date":post.date}
        stream.append(js)

    else:
        print("{} from {} skipped.".format(post, post.owner_profile))
    return Response(stream)