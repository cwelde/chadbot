import tweepy
import numpy as np
import time

tr = open('speeches.txt', encoding = 'utf-8').read()
corpus = tr.split()

consumer_key ="YJ8loqlt08YF3ydEhNBw8NEE5"
consumer_secret ="oOttd5uNKODF7kW77qhnsB8KU70360p4JNLZMxwpvX3MKhNzml"
access_token ="1110649385635868673-cbMHENGmpccqXebb9vANZuF6LRFaXV"
access_token_secret ="Y1evBVfONJTYDSQyFZwxrGeS4M682OyyEtBWy2peBgvKp"

def makePairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])


    
def sendTweet(ck, cs, at, ats, message):
    
    auth = tweepy.OAuthHandler(ck,cs)

    auth.set_access_token(at,ats)

    api = tweepy.API(auth)

    api.update_status(status = message)


if __name__ == "__main__":
    while True:
        pairs = makePairs(corpus)

        word_dict = {}

        for word_1, word_2 in pairs:
            if word_1 in word_dict.keys():
                word_dict[word_1].append(word_2)
            else:
                word_dict[word_1] = [word_2]

        first_word = np.random.choice(corpus)
        chain = [first_word]
        n_words = 30

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))

        myMessage = ' '.join(chain)
        sendTweet(consumer_key,consumer_secret,access_token,access_token_secret, myMessage)
        print("Just sent one")
        time.sleep(120)
