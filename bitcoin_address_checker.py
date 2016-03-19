#take in a list, ignore empty wallets with zero transactions
#get ip used to relay and find out where wallet is from
from sys import argv
from urllib2 import urlopen
import json

def btc(btcinput):
	apiaddress = 'http://blockchain.info/address/%s?format=json' % btcinput 
	apiurl = urlopen(apiaddress)
	apidata = json.load(apiurl)
	if apidata['final_balance'] == 0 and apidata['total_received'] == 0 and apidata['total_sent'] == 0:
		pass
	else:
		print '%s\t%s\t%s\t%s\t%s' % (apidata['address'],apidata['final_balance'],apidata['total_received'],apidata['total_sent'],apidata['n_tx'])
		#n 0 is send n 1 is receive
		#print apidata['txs']
		#ip_addresses = []
		#for transaction_item in apidata['txs']:
		#	ip_addresses.append(transaction_item['relayed_by'])
		#for ip_address in list(set(ip_addresses)):
		#	print ip_address
			
script,listfile = argv 

btc_address_list = open(listfile)
print "Address\t\t\t\t\tBalance\tReceived\tSent\tNo. of Transactions"
for address in btc_address_list:
	btc(address.rstrip())