try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from keys import api_key, api_secret, access_token, access_token_secret

ACCESS_TOKEN = access_token
ACCESS_SECRET = access_token_secret
CONSUMER_KEY = api_key
CONSUMER_SECRET = api_secret

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

#sample of public data
iterator = twitter_stream.statuses.sample()
tweet_count = 5
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)
    if tweet_count <= 0:
        break
