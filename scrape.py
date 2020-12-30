import urllib.request
from urllib.request import urlretrieve
from html.parser import HTMLParser
import re
import threading

class BBCArchiveHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            hrefs = ['https:' + href[1] for href in attrs if (href[0] == 'href' and href[1].endswith('.mp3') and '/audio-nondrm-download/' in href[1])]
            if len(hrefs) > 0:
                print(hrefs[0])
                file_name = re.match(r'^.+/([A-Za-z0-9:]+\.mp3)$', hrefs[0]).group(1)
                print(file_name)
                urlretrieve (hrefs[0], f'mp3s/{file_name}')

def process_page(html):
    parser = BBCArchiveHtmlParser()
    parser.feed(html)

threads = []
for page in range(1, 24):
    response = urllib.request.urlopen(f'https://www.bbc.co.uk/programmes/b01s6xyk/episodes/downloads?page={page}')
    page_bytes = response.read()
    page_string = page_bytes.decode("utf8")
    response.close()
    
    thread = threading.Thread(target=process_page, args=(page_string,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()