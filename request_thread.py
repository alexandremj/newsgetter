from threading import Thread

import requests

""" Thread subclass for HTTP requests regarding the fetching of information
    from news sources' RSS feed """
class RequestThread(Thread):
    def __init__(self, link):
        Thread.__init__(self)
        self.link = link
    
    """ Sends a GET request to the link and returns the contents of the
        RSS feed from last day """
    def run(self):
        r = requests.get(self.link)
        print(r.status_code)