import tweepy
from time import sleep

API_KEY = 'tDTjqtriaaN36rqgWiM03dfAP'
API_SECRET = 'iXedoTTXfwE0GekR1172VNnAOXmyUXbHJ1riPFdmkL1KSJCTKT'
ACCESS_TOKEN = '2876575891-hEPoe4rxnJZcDRbQegiMpBLgEFXutkVjGnwC0dW'
ACCESS_TOKEN_SECRET = 'Kgz0tIz3yFcqim2Qo2YB38nNBOPtabkNpsku7SWpHkaQ4'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
Account = 'premier_teru'
#アカウントの情報を取得
myinfo = api.me()
#100ツイートほどTLを取得
souCount = 0
tweets = tweepy.Cursor(api.user_timeline, id = myinfo.id).items(3200)
for tweet in tweets:
    # if int(tweet.created_at.strftime('%d')) < 27:
    try:
        api.destroy_status(tweet.id)
    except Exception as e:
        print(e)
        print("削除上限数に達したため休憩します🍵")
        continue
    
    souCount = souCount + 1
    print('削除したツイートの投稿日:'+str(tweet.created_at)+' 削除数：'+str(souCount))
    if souCount % 3200 == 0:
        print('3時間休憩🍵')
        sleep(1080)