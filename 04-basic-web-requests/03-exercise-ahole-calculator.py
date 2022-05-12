import json
from multiprocessing.sharedctypes import Value
#import pathlib
import ssl
from urllib.request import Request, urlopen

url = "http://www.reddit.com/r/amitheasshole.json"
request = Request(
    url,
    headers={
        'User-Agent': 'TebsLabPythonExercise/0.0.4' # setting the user agent decreases throttling by Reddit
    }
)

# Context is for MacOS users related to SSL certificates. Details: https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
response = urlopen(request, context=ssl._create_unverified_context())
listing = json.load(response)

print('break')

#pull out deepest layer of usable data
top_data = listing.get('data').get('children')

#Pull top posts and their URL
posts_by_title_url = {}
posts_with_votes = {}
for child in top_data:
    post = child['data']     

    #Append dict for posts
    posts_by_title_url[post['title']] = post['url']

#gather data from comments inside each post
for title, value in posts_by_title_url.items():
    #define dictionary for tallying votes
    vote_counts = {}
    vote_counts['YTA'] = 0
    vote_counts['NTA'] = 0
    vote_counts['ESH'] = 0
    vote_counts['NAH'] = 0
    vote_counts['Abstain'] = 0

    #Pull data from the post
    json_url = f'{value}.json'
    comment_request = Request(
        json_url,
        headers={
            'User-Agent': 'TebsLabPythonExercise/0.0.4' # setting the user agent decreases throttling by Reddit
        }
    )

    # Context is for MacOS users related to SSL certificates. Details: https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
    comment_response = urlopen(comment_request, context=ssl._create_unverified_context())
    #[1] because the first entry is the original post
    comment_listing = json.load(comment_response)[1]

    #print('break')

    #data>children to get to the level of comments
    comment_data = comment_listing.get('data').get('children')
    #data>body to get to the comment body to search for YTA, NTA, ESH, NAH
    for info in comment_data:
        body = info.get('data').get('body') 
        
        #error handle blank body
        if body == None:
            continue
        #Parse body for vote
        if 'YTA' in body:
            vote_counts['YTA'] += 1
        elif 'NTA' in body:
            vote_counts['NTA'] += 1
        elif 'ESH' in body:
            vote_counts['ESH'] += 1
        elif 'NAH' in body:
            vote_counts['NAH'] += 1
        else:
            vote_counts['Abstain'] += 1
    posts_with_votes[title] = vote_counts


import pprint
pp=pprint.PrettyPrinter(indent=0)
pp.pprint(posts_with_votes)



#print('break before end')