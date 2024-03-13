from bs4 import BeautifulSoup
import requests

url = 'https://tickets.fandango.com/mobileexpress/seatselection?row_count=443474031&mid=234444&chainCode=AMC&sdate=2024-03-11+19:45&tid=aawwx&route=map-seat-map'

userAgentMac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
page = requests.get(url, headers={'User-Agent': userAgentMac})
print(page.status_code)