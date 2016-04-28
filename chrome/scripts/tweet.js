function send_tweet(tweet) {
    var http = new XMLHttpRequest();
    var url = "http://mycode.doesnot.run/cpssd_unrated";
    var params = "tweet=" +encodeURIComponent(tweet) + "&auth_token=example_token";
    http.open("POST", url, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(params);
    chrome.extension.getBackgroundPage().console.log("Tweeted " + tweet); 
}

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if(changeInfo.status == 'complete' && tab.active){
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            var query = '';
            var title = tabs[0].title;
            if(title.indexOf('Google Search') >= 0){
                query = title.substr(0, title.lastIndexOf(' -'));
            }
            if(query.length > 0){
                chrome.extension.getBackgroundPage().console.log(query);
                console.log(query);
                send_tweet(query);
            }
        });
    }
});
