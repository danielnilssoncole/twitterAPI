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

search_term = raw_input('Enter your search term: ')
print ''

twitter = Twitter(auth=oauth)
results = twitter.search.tweets(q=search_term, result_type='popular', lang='en', count=10)
parsed = json.loads(json.dumps(results))
statuses = parsed['statuses']

# print json.dumps(statuses, indent=4)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_east = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
dt_east_str = dt_east.strftime('%m/%d/%Y %I:%M %p')

with open('search.txt', 'w') as f:
    f.write('\nSearch Term: {}\n\n'.format(search_term))
    f.write('{}\n'.format(dt_east_str))

    for status in statuses:
        screen_name = status['user']['screen_name']
        ct_str = status['created_at']
        parsed_date = parser.parse(ct_str)
        created_time = parsed_date.strftime('%m/%d/%Y %I:%M %p')
        text = status['text'].encode('utf-8')
        f.write('\n@{0}\n{1}\n{2}\n'.format(screen_name, created_time, text))
