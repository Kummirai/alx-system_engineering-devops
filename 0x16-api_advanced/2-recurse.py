#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    res = requests.get(url, params=parameters, headers=headers,
                       allow_redirects=False)

    if res.status_code == 200:
        next_ = res.json().get("data").get("after")
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        all_titles = res.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
