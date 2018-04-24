# -*- coding: utf-8 -*-

from operator import itemgetter

def Mean(t):
	"""Computes the mean of a sequence of numbers.

	Args:
		t: sequence of numbers

	Returns:
		float
	"""
	return float(sum(t)) / len(t)

def Mode(hist):
	max = 0
	keyOfMax = None
	for key, count in hist.iteritems():
		if count > max:
			max = count
			keyOfMax = key
	return keyOfMax

def AllModes(hist):
	pairList = [(key, count) for key, count in hist.iteritems()]
	getCount = itemgetter(1)
	return sorted(pairList, key=getCount, reverse=True)
