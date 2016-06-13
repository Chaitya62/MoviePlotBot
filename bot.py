from config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET
from fetch_data import make_query,request
import tweepy

#Authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)


def extract_movie_title(tweet_text):
    text = tweet_text.split(" ")
    text.remove(text[0])
    movie = ''
    for word in text:
        movie += (word + " ")
    return movie
        

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text) #print the query tweet
        if '@Chaitya_chase' in status.text:
            movie = extract_movie_title(status.text)
            request_url = make_query(movie)  
            plot = request(request_url)  
            sn = status.user.screen_name
            print(plot)
            #tweet length is 140 characters
            if(len(plot)>120):   
                 message = "@" + sn +" "+ plot[:115]
                 api.update_status(message,status.id)
            else:  
                message = "@" + sn +" "+ plot
                api.update_status(message,status.id)
        return 0

myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@Chaitya_chase'])

