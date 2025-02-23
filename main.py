import requests
from bs4 import BeautifulSoup
import json
from typing import Literal, Optional
import time

class Timeline:
    def __init__(self, initial_timeline, next_params):
        self.timeline = initial_timeline
        self.next_params = next_params

    def __iter__(self):
        return self

    def __next__(self):
        if not self.next_params:
            raise StopIteration
        
        url = 'https://search.yahoo.co.jp/realtime/search?'
        r = requests.get(url, params=self.next_params)
        soup = BeautifulSoup(r.text, 'html.parser')
        next_data_tag = soup.find('script', {'id': '__NEXT_DATA__'}).text
        data = json.loads(next_data_tag)
        
        self.timeline = data['props']['pageProps']['pageData']['timeline']
        self.next_params = data['props']['pageProps']['pageData']['pagination'].get('params')
        if self.next_params:
            self.next_params['oldestTweetId'] = self.timeline['entry'][-1]['id']
        return self.timeline

class YahooRealtimeSearch:
    def __init__(self):
        self.crumb = None

    def get_timeline(self, keyword: str, type: Optional[Literal["media"]] = None):
        url = 'https://search.yahoo.co.jp/realtime/search?p='
        if "@" in keyword:
            keyword = f'ID:{keyword.replace("@", "")}'
        if type == 'media':
            url = f'{url}{keyword}&ei=UTF-8&mtype=image'
        
        r = requests.get(f'{url}{keyword}')
        soup = BeautifulSoup(r.text, 'html.parser')
        next_data_tag = soup.find('script', {'id': '__NEXT_DATA__'}).text
        data = json.loads(next_data_tag)
        timeline = data['props']['pageProps']['pageData']['timeline']
        next_params = data['props']['pageProps']['pageData']['pagination'].get('params')
        if next_params:
            next_params['oldestTweetId'] = timeline['entry'][-1]['id']
        return Timeline(timeline, next_params)


if __name__ == '__main__':
    y = YahooRealtimeSearch()
    timeline = y.get_timeline('@deepseek_ai')
    print(timeline.__next__())
    time.sleep(3)
    print(timeline.__next__())