
import html
import requests
from requests.adapters import ConnectionError
from requests.models import InvalidURL


class _WebpageParser(html.parser.HTMLParser):

    def __init__(self):
        self.at_title = False
        self.title = ""
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.at_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.at_title = False

    def handle_data(self, data):
        if self.at_title:
            self.title += data


# Used to get metadata of a webpage, like title and icon
def webpage_data(url):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            parser = _WebpageParser()
            parser.feed(req.text)
            return { 'title': parser.title }
        else:
            return None
    except ConnectionError as e:
        return None
    except InvalidURL as e:
        return None
