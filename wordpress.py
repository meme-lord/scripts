#usage: python wordpress.py http://blog.site.com/blog/
#http://localhost/wordpress/wp-admin/setup-config.php
#http://localhost/wordpress/wp-admin/install.php
#http://localhost/wordpress/wp-login.php
#http://localhost/wordpress/wp-admin/

import requests
import bs4
from sys import argv

script,url = argv
if url[-1]!='/':
	url = url+'/'

headers = {'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)'}

titles = []

for author_num in range(1,100):
	initial_url = "%s?author=%d" % (url,author_num)
	r = requests.get(initial_url,headers=headers)
	if r.status_code != '404':
		print "%d - %d" % (author_num,r.status_code)
	page_html = bs4.BeautifulSoup(r.text,"lxml")
	page_title =  page_html.title.text
	if page_title not in titles:
		titles.append(page_title)
		print page_title
	if initial_url!=r.url:
		print r.url