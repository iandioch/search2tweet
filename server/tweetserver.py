from flask import Flask, request
import tweepy

flask_app = Flask(__name__)
api = None # tweepy api

@flask_app.route("/", methods=['POST'])
def hello():
    api.update_status(request.form['tweet'])

if __name__ == '__main__':
    try:
        auth_data = [l.strip() for l in open('twitter_auth.txt')]

        auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
        auth.set_access_token(auth_data[2], auth_data[3])
        api = tweepy.API(auth)

        flask_app.run()
    except Exception as e:
        print 'The server could not start:'
        print e
