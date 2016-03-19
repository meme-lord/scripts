import cfscrape,sys
try:
	script,forum_address,searchword = sys.argv
except:
	print "USAGE: python script.py http://site.com/forum/member.php? administrator"
	exit()
#forum_address = 'http://forums.ubi.com/member.php/'

sess = cfscrape.create_scraper()
sess.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded"}

i = 0
while True:
	profile_address = '%s%d' % (forum_address,i)
	page_text = sess.get(profile_address).text
	if searchword in page_text:
		print profile_address
	i+=1
	sys.stdout.write("%d\r" % i)
	sys.stdout.flush()