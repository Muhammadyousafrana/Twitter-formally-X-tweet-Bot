import tweepy


consumer_key = "your Consumer Key"
consumer_secret = "your consumer secret key"

access_token = "Your twitter formally X access token key"
access_token_secret = "Your twitter formally X access token secret key"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)


# If the authentication was successful, this should print the
# screen name / username of the account
username = api.verify_credentials().screen_name

tweets = api.user_timeline(screen_name=username, count=200, tweet_mode="extended")

for tweet in tweets:
    print(tweet.full_text)


























    # consumer_key='djMbbqpxMJOkbgEOUGuG3yWNn',
    # consumer_secret='NmyD517Fy9guXkZDNvCtA6hVQGdjoGmmNp5ieDiNzQSLq72ht3',
    # access_token='1694783464808349696-H5u8M5UYFjNUsQ6MNKjsdUUMc73qcV',
    # access_token_secret='JLq9uSaLUvuH4hJYjzTfYF1Ibooe6jmde6XjOdOUf4gQL',
