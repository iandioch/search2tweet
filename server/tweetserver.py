from flask import Flask, request
import tweepy


flask_app = Flask(__name__)
api = None # tweepy api
tokens = []

token_file = 'tokens.txt'
twitter_auth_file = 'twitter_auth.txt'


@flask_app.route("/", methods=['POST'])
def tweet():
    if 'auth_token' not in request.form:
        print 'No token provided'
        return 'No token provided'
    if 'tweet' not in request.form:
        print 'No tweet provided'
        return 'No tweet provided'

    token = request.form['auth_token']
    if not token in tokens:
        print 'Invalid token provided'
        return 'Invalid token provided'

    tweet = request.form['tweet']
    api.update_status(tweet)
    print 'Tweeted: {}'.format(tweet)
    return 'Tweeted: {}'.format(tweet)


@flask_app.route("/add_token", methods=['POST'])
def add_token():
    if 'auth_token' not in request.form:
        print 'No login token provided'
        return 'No login token provided'
    if 'new_token' not in request.form:
        print 'No new token provided'
        return 'No new token provided'

    auth_token = request.form['auth_token']
    if auth_token not in tokens:
        print 'Invalid auth token provided'
        return 'Invalid auth token provided'

    new_token = request.form['new_token']
    
    if new_token in tokens:
        print 'Token already exists'
        return 'Token already exists'

    try:
        print 'Opening token_file'
        f = open(token_file, 'a')
        f.write(new_token)
        f.write('\n')
        print 'Closing token file'
        f.close()
        print 'All done!'
    except Exception as e:
        print e
        print 'Error {}'.format(e)
        return 'Error {}'.format(e)
    return 'Token added.'


if __name__ == '__main__':
    try:
        # load the twitter auth
        with open(twitter_auth_file, 'r') as f:
            auth_data = [l.strip() for l in f]

        auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
        auth.set_access_token(auth_data[2], auth_data[3])
        api = tweepy.API(auth)

        # load the tokens for users
        with open(token_file, 'r') as f: 
            tokens = set([l.strip() for l in f])

        # start the ball rolling
        flask_app.run()
    except Exception as e:
        print 'The server could not start:'
        print e

