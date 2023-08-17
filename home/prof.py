from rest_framework.response import Response
import instaloader



def downloadprof(username):
    L = instaloader.Instaloader()
    stream=[]

    
    # L.login("insta.botnew", "instabot001")
    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    users = set()
    count=1
    for post in posts:
        
        # L.download_post(post, username)
        # users.add(post.owner_profile)
        print(count)
        if(post.is_video):
            print(post.video_url)
            
        else:
            print(post.url)
        count +=1
        # js={"Url":post.url,"Caption":post.caption,"Date":post.date}
        # stream.append(js)

    else:
        print("{} from {} skipped.".format(post, post.owner_profile))
    
downloadprof("cruel_hot_mummy")