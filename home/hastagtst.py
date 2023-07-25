import instaloader

def download_hashtag_posts(hashtag):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    L.login("insta.botnew", "instabot001")

    # Define a function to filter posts by hashtag
    def filter_hashtag_post(post):
        return hashtag in post.caption_hashtags

    # Get posts with the specified hashtag
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()

    # Download posts with the specified hashtag
    count = 0
    for post in posts:
        if filter_hashtag_post(post):
            L.download_post(post, target=f"{hashtag}_posts")
            print(count)
            # print(post.url)
            count += 1


    print(f"Downloaded {count} posts with the #{hashtag} hashtag.")

# Replace 'your_hashtag' with the hashtag you want to download
download_hashtag_posts('mstud_rough2')
