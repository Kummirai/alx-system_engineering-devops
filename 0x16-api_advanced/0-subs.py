#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):

    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

  headers = {"User-Agent": "Bing"}
  # Construct the URL for the subreddit's about.json endpoint
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  # Send a GET request and get the response as JSON
  response = requests.get(url, headers=headers).json()
  # Check if the response contains data and subscribers keys
  if "data" in response and "subscribers" in response["data"]:
    # Return the number of subscribers
    return response["data"]["subscribers"]
  else:
    # Return 0 for invalid subreddits
    return 0

