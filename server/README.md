search2tweet server
-------------------

The server is written in Python 2. The dependencies can be installed with the following command:

`pip install -r requirements`

The twitter auth data is in the file `twitter_auth.txt`, which must be formatted in the following way:

```
consumer_key
consumer_secret
access_token
access_token_secret
```

You can run the server with `python tweetserver.py`. It will spin up a shiny endpoint on port `5000`. It will tweet whatever you give the `/` route in a `tweet` POST field. However, you need to provide one of the tokens from the `tokens.txt` file in the `auth_token` field.

You can add new tokens by POST-ing the `/add_token` endpoint, giving it a previously valid token in `auth_token`, and a new one in `new_token`. It will then add that new token to the `tokens.txt` file.

