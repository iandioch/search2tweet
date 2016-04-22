# search2tweet
Let a group of users embarrass each other by tweeting everything they search.

The project is made up of a few parts:

## Server
The `server` directory contains a Flask server that, when contacted with a valid token, will tweet a given message from a certain Twitter account.

## Firefox Add-On
The `firefox` directory contains a Firefox add-on, that listens when you search something, and sends that to the above server to be tweeted and shamed.

A Chrome extension will hopefully be coming soon.
