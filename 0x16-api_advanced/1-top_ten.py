
#!/usr/bin/python3
"""
Queries Reddit API.
Prints the titles of first 10 hot posts for a gven subreddit.
"""
import requests


def top_ten(subreddit):
    """Function that queris Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return print(None)
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Ajiboye Adeleye/ALX-Api-Advanced'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params)
        dic = response.json().get('data')
        for i in dic.get('children'):
            print(i.get('data').get('title'))
    except Exception:
        return print(None)
