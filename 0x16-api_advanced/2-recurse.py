#!/usr/bin/python3
"""
Recursive function that queries the Reddit API.
Returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return None

    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'ALX-advanced_APIi/by Ajiboye Adeleye pius'}
    params = {
            'after': after,
            'limit': 100
            }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=True)
    if resp.status_code == 404:
        return None

    res = resp.json().get('data')
    after = res.get('after')
    count = res.get('dist')
    for item in res.get('children'):
        hot_list.append(item.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
