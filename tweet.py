import tweepy

consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""

def sendTweet(ck, cs, at, ats, message):
    
    auth = tweepy.OAuthHandler(ck,cs)

    auth.set_access_token(at,ats)

    api = tweepy.API(auth)

    api.update_status(status = message)


if __name__ == "__main__":

    sendTweet(consumer_key,consumer_secret,access_token,access_token_secret, "Your Message Here")