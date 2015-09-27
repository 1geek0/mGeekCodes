from twython import Twython, TwythonError

#Twitter Credentials
app_key = "nemYHwbENbRIsqhjECmMGS1wx"
app_secret = "mONLabyAwNIrls1PLn6M7yCroqbA52cuN4Erjs2ZqvH0PMb2I5"
oauth_token = "3678562272-rkoFVgBY1ws0PRwo8RCoznou0Rh8MvfJirViugW"
oauth_token_secret = "lU6LLvoINShdkkPsftM6LL3rZBZL40c2AhIDpD3gd7CvV"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

to_be_followed = ['nilaydreams', 'ashwinkandoi', 'UXHow', 'tech_souls', 'NashikNews', '_vipuls', 'TEDxBhilwara', 'prabha_satya', 'TEDchris', 'iweapp', 'BethanyJana', 'join2manish', 'gvanrossum', 'rodinhood', 'yashrajx', 'nancykatyal', 'rashmibansal', 'Joi', 'cameraculture', 'praveengedam', 'mattcutts', 'KoustuvDasgupta', 'Innometheus', 'AbhiSuryawanshi', 'iamnirman', 'inktalks', 'sohil_4932']

followed = twitter.get_friends_ids(screen_name='mGeekCodes')
following_me = twitter.get_followers_ids(screen_name='mGeekCodes')

for user in followed['ids']:
    print user
    if user not in to_be_followed:
        if user not in following_me:
            twitter.destroy_friendship(user_id=user)