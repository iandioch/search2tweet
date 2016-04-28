var self = require("sdk/self");
var tabs = require("sdk/tabs");
var file = require("sdk/io/file");
var path = require("sdk/fs/path");
var Request = require("sdk/request").Request;

var token = require("sdk/simple-prefs").prefs.auth_token;

var tweetRequest = 
tabs.on('ready', function(tab) {
    var query = '';
    if(tab.title.indexOf('Google Search') >= 0){
        console.log(tab.title);
        query = tab.title.substr(0, tab.title.lastIndexOf(' -'));
    }else if(tab.title.indexOf('DuckDuckGo') >= 0){
        query = tab.title.substr(0, tab.title.lastIndexOf(' at'));
    }else if(tab.title.indexOf(' - Yahoo Search') >= 0){
        query = tab.title.substr(0, tab.title.lastIndexOf(' -'));
    }else if(tab.title.indexOf(' - Bing') >= 0){
        query = tab.title.substr(0, tab.title.lastIndexOf(' -'));
    }else if(tab.title.indexOf(', Ask Jeeves') >= 0){
        query = tab.title.substr(0, tab.title.lastIndexOf(' ,'));
    }else if(tab.title.indexOf(' - YouTube') >= 0){
        query = tab.title.substr(0, tab.title.lastIndexOf(' -'));
    }
    if(query.length > 0){
        console.log(query);
        Request({
            url: "http://127.0.0.1:5000/",
            content: "auth_token=" + encodeURIComponent(token) + "&tweet=" + encodeURIComponent(query),
            onComplete: function (response) {
                console.log(response.text)
            }
        }).post();
    }
});

