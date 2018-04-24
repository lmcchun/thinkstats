# -*- coding: utf-8 -*-

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
