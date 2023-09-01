from rest_framework.response import Response
from rest_framework.decorators import api_view
import instaloader

@api_view()

def     downloadprof(request):
    L = instaloader.Instaloader()
    stream=[]
    username = request.GET['link']
    
    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    users = set()
    # max_count=100
    sidecar=[]
    videopost=[]
    videothumb=[]
    imagepost=[]
    count = 1


    for post in posts:
        print(post)
        type=post.typename
        # if(count>=max_count):
        #    break
        

        if(type == "GraphVideo"):
            furl=post.video_url
            vthumb=post.url
            videothumb.append(vthumb)
            videopost.append(furl)
            count += 1

        elif(type == "GraphImage"):
            furl=post.url
            imagepost.append(furl)
            count += 1

        elif post.typename == "GraphSidecar":

            for media in post.get_sidecar_nodes():             
             if(media.is_video == True):
                furl=media.video_url
                videopost.append(furl)
                vthumb=media.display_url
                videothumb.append(vthumb)

             else:
                furl=media.display_url
                imagepost.append(furl)
            count+=1
        else:
            return Response({"videourls":videopost, "videothumb": videothumb,"imageurls": imagepost, "username":username})
    return Response({"videourls":videopost, "videothumb": videothumb,"imageurls": imagepost, "username":username})
           
        

        



