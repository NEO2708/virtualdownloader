from rest_framework.response import Response
from rest_framework.decorators import api_view
import instaloader

@api_view()

def     downloadprof(request):
    L = instaloader.Instaloader()
    stream=[]
    username = request.GET['link']
    
    # L.login("p_chauhan_58", "rina27")
    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    users = set()
    max_count=100
    sidecar=[]

    count = 1
    scc=1

    for post in posts:
        type=post.typename
        # print(type)
        if(type == "GraphVideo"):
            js={"NO":count,"Url":post.video_url,"Caption":post.caption,"Date":post.date,"type":"Video"}
            stream.append(js)
            count += 1
        elif(type == "GraphImage"):
            js={"NO":count,"Url":post.url,"Caption":post.caption,"Date":post.date,"type":"Image"}
            stream.append(js)
            count += 1
        else:
            media=post._full_metadata
            edge=media.get("edge_sidecar_to_children")
            edge=edge.get("edges")
            mdct=10


            for m in edge:

                sidepost=m.get("node")
                type=sidepost.get("__typename")
                if(count >mdct):
                    count=1
                    break
                else:
                    if(type == "GraphVideo"):
                        url=sidepost.get("video_url")
                        sc={"NU:":scc,"Url":url,"type":"Video"}
                        sidecar.append(sc)
                        scc +=1
                    elif(type == "GraphImage"):
                        dr=sidepost.get("display_resources")
                        url=dr[2]
                        url=url.get("src")
                        sc={"NU:":scc,"Url":url,"type":"Image"}
                        sidecar.append(sc)
                        scc +=1
                    else:
                        break



            js={"NO":count,"Url":sidecar,"Caption":post.caption,"Date":post.date,"type":"SideCar"}
            stream.append(js)
            count += 1

        if count >= max_count:
            break



    return Response(stream)