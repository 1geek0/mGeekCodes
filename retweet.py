from __future__ import print_function
from twython import Twython, TwythonError
import mmap
import time

#Twitter Credentials
app_key = "nemYHwbENbRIsqhjECmMGS1wx"
app_secret = "mONLabyAwNIrls1PLn6M7yCroqbA52cuN4Erjs2ZqvH0PMb2I5"
oauth_token = "3678562272-rkoFVgBY1ws0PRwo8RCoznou0Rh8MvfJirViugW"
oauth_token_secret = "lU6LLvoINShdkkPsftM6LL3rZBZL40c2AhIDpD3gd7CvV"

#CSV files
#Generic Path
mGeekCodes_Path = '/home/admin/mGeekCodes/'
#For logging all the retweets
tweetedFile = open(mGeekCodes_Path+'tweeted.csv', 'a+')
#For Logging Each Followed Person
all_followed = open(mGeekCodes_Path+'all_followed.csv', 'a+')
#For Keeping a list of current followed
current_followed = open(mGeekCodes_Path+'current_followed.csv', 'a+')

#Mmaps
tweetedMmap = mmap.mmap(tweetedFile.fileno(), 0, access=mmap.ACCESS_READ)
all_followed_Mmap = mmap.mmap(all_followed.fileno(), 0, access=mmap.ACCESS_READ)
#current_followed_Mmap = mmap.mmap(current_followed.fileno(), 0, access=mmap.ACCESS_READ)

banned_accounts = ['todocoders', 'nodenow']
naughty_words = [" -RT", "HackerEarth", "Looking for", "Jobs", "job", "prizes", "todocoders"]
good_words = ["%23CodeBetter", "%23SoftwareCode", "%23AndroidCode", "%23PythonCode", "%23JavaCode", "%23Coder", "%23Coding", "%23ArduinoCode", "%23BetterAndroid", "%23CodeALot", "%23CodeHard", "%40mGeekCodes"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Setting Twitter's search results as a variable
search_results = twitter.search(q=keywords, count=100, result_type='mixed')
try:
    for tweet in search_results["statuses"]:
         tweeter = tweet['user']['screen_name']
         text = tweet['text'].encode('utf-8')
         if tweetedMmap.find(text) != -1:
             n=1
         else:
            #print(tweet)
            if tweeter not in banned_accounts:
                print("New Tweet")
                print(tweet['text'].encode('utf-8'), file=tweetedFile)
                twitter.retweet(id = tweet["id_str"])
                twitter.create_favorite(id = tweet['id_str'])
                if all_followed_Mmap.find(tweeter) == -1:
                    twitter.create_friendship(screen_name=tweeter)
                    print(tweeter+','+str(int(time.time())), file=all_followed)
                    print("New Friend: "+str(tweeter))
            else:
                n=2
              #  print("Banned Account")
except TwythonError as e:
    print(e)
print(len(search_results['statuses']))