from rest_framework.response import Response
import instaloader
from rest_framework.decorators import api_view
@api_view()
def posts(request):
    post_url = request.GET['link']

    L = instaloader.Instaloader()
#     if not firebase_admin._apps:
#     # Initialize the Firebase app
#         cred = credentials.Certificate({
#   "type": "service_account",
#   "project_id": "khudkibook",
#   "private_key_id": "be3361f282e441a2265d7da26605cf9d6943b401",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDK24YUVWB9XwM7\nd6ZCo4lYD2eeXai8CcsxosSYSkCG8v41hdfLw9AOWuM7HkMfnbiASnSga7q7oDIQ\nSD9jke9VsKoaITxCVsXQ+7zAXZlhFQj7WKNkIkWCUBSxfQ4HspCmYYZ5VtQCPEc7\n+ZtogQk2TBYRjosAWnQRuswGq5Xz0Yd64ul8a3/Y+b4BuxQPrLbMMVVkyTKwNEWX\nXQKyfX0QdM+T8+u1o6iLNoiThmiO55D8V8toM1TKvvhT45SEexAqVZftNl+B3Mk3\n2J3Tcs2WG+ETcZf7E5lPDfnIq72vN296+AM/l+deJY5v1B4g5AXHsiXmL8ozn/cB\nz7KiYJLxAgMBAAECggEAC7B/tu8+iqrtdEFOTtu+n9jvZyRNg1xrHZacDoyE0GHz\nPSFT0JWdiR46pt71Dj7X8WiY9N+QWJyAFgkbwgCYUo9GFhBhOQ9oAcVn2IvsOTht\nlpJChBQnfj1gG+QxaUckZ7oJ9jcHK4POtQmKp4h7/+l9ghB9OQ19T8I8XIwJrY2E\npToS6kvTM/AEU6eIEL+VFYWQ+gcVsGWXY1PshoX0Ltr5bUyKFlBLHWW7UjefyVzG\nkCtU3o2rUhJitBTjax+HGvLd5auAs/e6dH8VKgW8N8P0XHCHAjh1c9WT0wBafhln\nBj0ThSHkg9Nd1f/aN3bvlH2K4yjUnN60vsfofUnBAQKBgQDnjKGTO5FLI+STXNZC\n9QGOxX0/P5REBiFeagyXxVMMQVo4UDrKo6vpwVvRlbPJz1KH+DDw4S/eVIy0q6IO\n+ZG+job/hjDfvbnJ8um9ozg6dGsmnRCoVz/5fUSReJJlYbKIk/p+NSGqQ/B8bKAW\nToI5rObJQ8/FVTvCzLQhzUsvoQKBgQDgR0eHpTrE+byViJoiQsnxe+XpGBXwSuGI\nycfek2HpLcrjKwz9fdwgbHQRy+aeAOzb8PDtCo2FUyLbmv9LCoZ4C7nuOBXYMnc6\ngBvxkZzRDjk+fGtYUjZpvS1iLDowPleCf8+KyeZqz3IRerM4KrLvoWDgMkYBBm6r\nWFjLJnrhUQKBgDYIJggSZWQwWv1cM49qVtO3F/PzZSi+eXjrrEaaQDfi5Cex6RYy\nPUKN4Vw1379fBrY930XGdoIeHrtmNani6PSbk7r62FrNjhYm/g5HkS5qzjozepid\ny4rvhVmg1iCcPKoMRe6/fTybH/oY6v5pkY/d3fjnPwugSRK66+nbWwkhAoGAJiL4\nvtAR1jzBHIxF6V2CCVYQGjrGQD37a88j9W0KUSRAQ7CmXNRyAfFvKzeI14VAwYWO\n8j/BINKqMr2Ae7omc3NLAn729/Rc4c228rTX/ZR1l3KArlwMdJ5+gRsUKe/v4Xjq\nSadbTv5HX0GGCB76nlTKrFTgInx9hRVYw/KfIoECgYBq0CAooEw6pdwGRKHEFZbV\n4tf5tpP50wJ61sab1AmsNoCoUrQUCzsqncFfYCcvwXE+eI4nk3ens5X6Q4zHrCZe\nWnzDEXbfERpXlvW9IcnUs7WHODqiADBiY/W5tnayGc4Ozx34B4f6Bh9/R9eW63dr\nmbp3GRtAbvwv8zfvNuD8ZA==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-vegxe@khudkibook.iam.gserviceaccount.com",
#   "client_id": "106681282986463050082",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-vegxe%40khudkibook.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }
# )
#         firebase_admin.initialize_app(cred, {
#         "storageBucket": "khudkibook.appspot.com"
#         })
    
    
#     db = firestore.client()
    # def upload_file(url, filename):
    #     # Fetch the file from the URL
    #     file_data = urllib.request.urlopen(url).read()

    #     # Upload the file to Firebase Storage
    #     bucket = storage.bucket()
    #     blob = bucket.blob(filename)
    #     blob.upload_from_string(file_data, content_type='application/octet-stream')

    #     return blob.generate_signed_url(datetime.timedelta(minutes=5), method='GET')

    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])
    username=post.owner_username
    # name=post.owner_profile.full_name
    # caption=post.caption
    # avatar=post.owner_profile.get_profile_pic_url()
    # downloadable_urls = []
    videopost=[]
    videothumb=[]
    imagepost=[]
    if post.typename == "GraphVideo":
        furl=post.video_url
        vthumb=post.url
        videothumb.append(vthumb)
        videopost.append(furl)
        return Response({"videourls":videopost,"videothumb": videothumb,"imageurls": imagepost, "username":username }) 
    elif post.typename == "GraphImage":
        furl=post.url
        imagepost.append(furl)
        return Response({"videourls":videopost, "imageurls": imagepost, "username":username }) 
    elif post.typename == "GraphSidecar":
        count=1
        for media in post.get_sidecar_nodes():             
         if(media.is_video == True):
            furl=media.video_url
            videopost.append(furl)
            vthumb=media.display_url
            videothumb.append(vthumb)
            count+=1
         else:
            furl=media.display_url
            imagepost.append(furl)
            count+=1
        return Response({"videourls":videopost, "videothumb": videothumb,"imageurls": imagepost, "username":username})
             
             
    else:
        return Response({"videourls":videopost, "videothumb": videothumb,"imageurls": imagepost, "username":username})
    



