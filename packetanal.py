#!/usr/bin/python

import pygeoip,sys,dpkt,socket

gi = pygeoip.GeoIP('/opt/geoip/GeoLiteCity.dat')		

def seekcity(ip):
	try:
		rec	= gi.record_by_name(ip)
		city	= rec['city']	
		cc	= rec['country_code3']
		if city != '':
			return city+', '+cc
		else:
			return cc
	except:
		return 'Unregistered'

def infos(pcap):
	for ts, buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf) 
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] src: '+src+'---> Dst: '+dst
			print '[+] '+seekcity(src)+'---> Dst: '+dst
		except Exception, e :
			pass

def main():
	if len(sys.argv) != 2:
		print 'usage: python %s packet.pcap'% sys.argv[0]
		exit(0)

	pcap = sys.argv[1]
	arquivo_pcap = open(pcap)
	pcap = 	dpkt.pcap.Reader(arquivo_pcap)
	infos(pcap)	

main()
