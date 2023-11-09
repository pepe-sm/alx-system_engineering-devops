#!/usr/bin/python3
"""top 10"""
import requests


def top_ten(subreddit):
    """function queries the Reddit API limit 10"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url)

    if (req.status_code != 200):
        print(None)
        return

    try:
        childrens = req.json().get('data').get('children')
        for children in childrens:
            print(children.get('data').get('title'))
    except Exception:
        pass
