import twitter

import config

if __name__ == '__main__':
    api = twitter.Api(consumer_key=config.CONSUMER_API_KEY,
                      consumer_secret=config.CONSUMER_API_SECRET,
                      access_token_key=config.ACCESS_TOKEN,
                      access_token_secret=config.ACCESS_SECRET_TOKEN)

    USERNAME = config.TWITTER_USERNAME
    removal_likes = True
    likes_deleted = 0
    while removal_likes:
        likes = api.GetFavorites(screen_name=USERNAME, count=200)
        if likes:
            for like in likes:
                try:
                    res = api.DestroyFavorite(like)
                    print(f'Deleted like by: {like.user.screen_name} \n Tweet: {like.text}')
                    likes_deleted += 1
                except Exception as err:
                    if err.message[0]['message'] == 'No status found with that ID.':
                        print('Tweet deleted by original tweeter')
                        continue
                    else:
                        exit
        else:
            removal_likes = False
    print(f'Likes deleted: {likes_deleted}')
