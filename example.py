from main import YahooRealtimeSearch

yahoo_realtime_search = YahooRealtimeSearch()
timeline = yahoo_realtime_search.search('@ProgressBar202_')
print(timeline.timeline['entry'])