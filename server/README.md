search2tweet server
-------------------

The server is written in Python 2. The dependencies can be installed with the following command:

`pip install -r requirements.txt`

The twitter auth data is in the file `twitter_auth.txt`, which must be formatted in the following way:

```
consumer_key
consumer_secret
access_token
access_token_secret
```

You can run the server with `python tweetserver.py`. It will spin up a shiny endpoint on port `5000`. It will tweet whatever you give it in a `tweet` POST field. 

TODO: add security :)

