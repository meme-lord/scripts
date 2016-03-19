import cfscrape,sys
try:
	script,forum_address = sys.argv
except:
	print "USAGE: python script.py http://www.site.ro/cache/"
	exit()
#forum_address = 'http://www.invisionpower.ro/cache/'

sess = cfscrape.create_scraper()
sess.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded"}

i = 0
years = ['15','16']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
for year in years:
	for month in months:
		for day in days:
			error_file = forum_address + 'sql_error_log_%s_%s_%s.cgi' % (month,day,year)
			page_text = sess.get(error_file).text
			if 'mySQL query error' in page_text:
				print error_file