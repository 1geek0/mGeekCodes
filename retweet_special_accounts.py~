from __future__ import print_function
from twython import Twython, TwythonError
import mmap
import time
import helper

#Twitter Credentials
app_key = "nemYHwbENbRIsqhjECmMGS1wx"
app_secret = "mONLabyAwNIrls1PLn6M7yCroqbA52cuN4Erjs2ZqvH0PMb2I5"
oauth_token = "3678562272-rkoFVgBY1ws0PRwo8RCoznou0Rh8MvfJirViugW"
oauth_token_secret = "lU6LLvoINShdkkPsftM6LL3rZBZL40c2AhIDpD3gd7CvV"

accounts_special = ["UXHow", "climagic", "nilaydreams", "Linux", "Android", "techjunkiejh"]
banned_accounts = ['todocoders', 'nodenow']
naughty_words = [" -RT", "HackerEarth", "Looking for", "Jobs", "job", "prizes", "todocoders"]
good_words = ["%23CodeBetter", "%23SoftwareCode", "%23AndroidCode", "%23PythonCode", "%23JavaCode", "%23Coder", "%23Coding", "%23ArduinoCode", "%23BetterAndroid", "%23CodeALot", "%23CodeHard", "%40mGeekCodes"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

for user in accounts_special:
    tweets_from_him = twitter.get_user_timeline(screen_name=user)
    for tweet in tweets_from_him:
        helper.handle_tweet(tweet)