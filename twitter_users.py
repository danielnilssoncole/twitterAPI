from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from keys import api_key, api_secret, access_token, access_token_secret
from dateutil import parser
import json
import datetime
import pytz

ACCESS_TOKEN = access_token
ACCESS_SECRET = access_token_secret
CONSUMER_KEY = api_key
CONSUMER_SECRET = api_secret

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)
main_user = twitter.users.show(screen_name="cocoweixu")
mu_parsed = json.loads(json.dumps(main_user))
# statuses = parsed['statuses']
# print json.dumps(results, indent=4)

followers = twitter.followers.ids(screen_name="cocoweixu")
followers_parsed = json.loads(json.dumps(followers))
ids = followers_parsed['ids'] #list of followers ids
# print ids[-1]

#todo
#loop through ids, find each user by id user = twitter.users.show(user_id=ids[i])
#write screen name, bio, urls to file 
