#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """Printing a sorted count of article titles"""

    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
        .format(subreddit, after)
    parameters = {'after': after}
    res = requests.get(url, params=parameters, headers=headers,
                       allow_redirects=False)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if res.status_code == 200:
        res = res.json()['data']
        aft = res['after']
        res = res['children']
        for item in res:
            title = item['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
