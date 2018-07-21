#!/usr/bin/python

import socket,dpkt,sys

def analise(pcap):
	l = []
	for ts,buf in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip  = eth.data
			tcp = ip.data
			if socket.inet_ntoa(ip.src) == '192.168.1.7' and socket.inet_ntoa(ip.dst) == '192.168.1.8':
					l.append(tcp.dport)
		except:
			pass
	l.sort()
	for i in l:
		print i
def main():
	if len(sys.argv) != 2:
		print 'uso: resolv.py pcap'
		exit(0)
	arq  = sys.argv[1]
	arq  = open(arq)
	pcap = dpkt.pcap.Reader(arq)
	analise(pcap)
main()
