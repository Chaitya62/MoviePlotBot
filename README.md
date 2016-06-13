# MoviePlotBot

  MoviePlotBot is a twitter bot that lets you search the plot of any movie just tag *Pending* in your tweet by the movie title and you will get an instant reply from MoviePlotBot.
  
#What does it do that?

  It Basically uses two APIs 
  
    1. Twitter API
    2. OmDB API


#How to run this bot?

##Requirements

###Language
  * Python 3.4.4
      
###Packages
    1. json (version 2.0.9)
    2. tweepy
  
for  more information on tweepy click [here](http://docs.tweepy.org/en/v3.5.0/) 
    
####Twitter App
  * Go [here](https://dev.twitter.com/) and register your twitter app
  * Get the twitter Consumer Key and Consumer Secret
  * Get the twitter Access key and Access Secret

####Configuration
      
In config.py set the values of 
~~~python
         
        CONSUMER_KEY = 'Enter your consumer key'
        CONSUMER_SECRET = 'Enter your consumer secret'
        ACCESS_KEY = 'Enter your access key'
        ACCESS_SECRET = 'Enter your access token'
        
~~~
    
In  bot.py replace all occurences of *pending* with "Your twitter Handle"


 > run stream_movie_plot.py

#Possible Improvements:

  1. It can return more things about the movie
  2. Imporve Extract_movie_title() function

#Lisense

  > Apache 2.0


#### Note: 
  *pending* is a placeholder



