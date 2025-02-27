import json
import pathlib
import ssl
from urllib.request import Request, urlopen

# Change this to False to use the file data.
use_live_data = True

if use_live_data:
    # Fetching the live data from reddit.
    url = "http://www.reddit.com/r/aww.json"
    request = Request(
        url,
        headers={
            'User-Agent': 'TebsLabPythonExercise/0.0.1' # setting the user agent decreases throttling by Reddit
        }
    )

    # Context is for MacOS users related to SSL certificates. Details: https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/
    response = urlopen(request, context=ssl._create_unverified_context())
    listing = json.load(response)
else:
    # Alternatively, loading the data from the provided json file.
    containing_dir = pathlib.Path(__file__).parent.resolve()
    with open(pathlib.Path(containing_dir / 'supplemental-materials' / 'reddit-aww.json')) as json_file:
        listing = json.load(json_file)

# Extract the posts to loop over them
posts = listing['data']['children']

# For our fact finding mission
posts_by_user = {}
sum_of_upvote_ratio = 0

# Iterate over the posts, extract the data, print
for post in posts:
    post_data = post['data']
    
    title = post_data['title']
    username = post_data['author']
    upvote_ratio = post_data['upvote_ratio']
    post_url = post_data['url']

    # Check if the user is already in there
    if username not in posts_by_user:
        posts_by_user[username] = 0
    
    # Then increase their post count.
    posts_by_user[username] += 1
    
    sum_of_upvote_ratio += upvote_ratio

    print('================')
    print(f'Title: {title}\nUser: {username}\nUpvote Ratio: {upvote_ratio}\nURL: {post_url}')
    print()

# Display which users posted multiple times (if any)
for username, post_count in posts_by_user.items():
    if post_count > 1:
        print(f'{username} posted {post_count} times!')

# Compute the avg upvote ratio
avg_upvote_ratio = sum_of_upvote_ratio / len(posts)
print(f'The average upvote ratio was {avg_upvote_ratio}')
