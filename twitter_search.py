from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from keys import api_key, api_secret, access_token, access_token_secret
from dateutil import parser
import json
import datetime

ACCESS_TOKEN = access_token
ACCESS_SECRET = access_token_secret
CONSUMER_KEY = api_key
CONSUMER_SECRET = api_secret

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# search_term = raw_input('Enter your search term: ')

twitter = Twitter(auth=oauth)
results = twitter.search.tweets(q='nasa', result_type='popular', lang='en', count=2)
parsed = json.loads(json.dumps(results))
statuses = parsed['statuses']

# print json.dumps(statuses, indent=4)

for status in statuses:
    screen_name = status['user']['screen_name']
    ct_str = status['created_at']
    parsed_date = parser.parse(ct_str)
    created_time = parsed_date.strftime('%m/%d/%Y %I:%M:%S %p')
    text = status['text'].encode('utf-8')
    print '\n@{0}\n{1}\n{2}\n'.format(screen_name, created_time, text)

print json.dumps(statuses[1], indent=4)
