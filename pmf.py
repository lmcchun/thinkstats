# -*- coding: utf-8 -*-

def MakeHistFromList(list):
	hist = {}
	for x in list:
		hist[x] = hist.get(x, 0) + 1
	return hist

def MakePmfFromHist(hist):
	pmf = {}
	count = 0
	for _, freq in hist.iteritems():
		count += freq
	for x, freq in hist.iteritems():
		pmf[x] = float(freq) / count
	return pmf

def MakePmfFromList(list):
	pmf = {}
	count = len(list)
	hist = MakeHistFromList(list)
	for x, freq in hist.iteritems():
		pmf[x] = float(freq) / count
	return pmf
