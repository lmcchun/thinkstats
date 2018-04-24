# -*- coding: utf-8 -*-

import gzip
import os

class Record(object):
	"""Represents a record."""

class Respondent(Record): 
	"""Represents a respondent."""

class Pregnancy(Record):
	"""Represents a pregnancy."""

def MakeRecord(line, fields, constructor):
	"""Scans a line and returns an object with the appropriate fields.
	
	Args:
		line: string line from a data file
	
		fields: sequence of (name, start, end, cast) tuples specifying 
		the fields to extract
	
		constructor: callable that makes an object for the record.
	
	Returns:
		Record with appropriate fields.
	"""
	obj = constructor()
	for (field, start, end, cast) in fields:
		try:
			s = line[start-1:end]
			val = cast(s)
		except ValueError:
			# If you are using Visual Studio, you might see an
			# "error" at this point, but it is not really an error;
			# I am just using try...except to handle not-available (NA)
			# data.  You should be able to tell Visual Studio to
			# ignore this non-error.
			val = 'NA'
		setattr(obj, field, val)
	return obj

def ReadFile(data_dir, filename, fields, constructor, n=None):
	"""Reads a compressed data file builds one object per record.

	Args:
		data_dir: string directory name
		filename: string name of the file to read
	
		fields: sequence of (name, start, end, case) tuples specifying 
		the fields to extract

		constructor: what kind of object to create
	"""
	filename = os.path.join(data_dir, filename)
	with gzip.open(filename) if filename.endswith('gz') else open(filename) as fp:
		records = []
		for i, line in enumerate(fp):
			if i == n:
				break
			record = MakeRecord(line, fields, constructor)
			records.append(record)
		return records

def ReadRespondents(data_dir, filename):
	"""A tuple specifying the fields to extract.
	The elements of the tuple are field, start, end, case.
			field is the name of the variable
			start and end are the indices as specified in the NSFG docs
			cast is a callable that converts the result to int, float, etc.
	"""
	fields = [('caseid', 1, 12, int),]
	return ReadFile(data_dir, filename, fields, Respondent)

def ReadPregnancies(data_dir, filename):
	# sequence of (name, start, end, type) tuples
	fields = [
		('caseid', 1, 12, int),
		('nbrnaliv', 22, 22, int),
		('babysex', 56, 56, int),
		('birthwgt_lb', 57, 58, int),
		('birthwgt_oz', 59, 60, int),
		('prglength', 275, 276, int),
		('outcome', 277, 277, int),
		('birthord', 278, 279, int),
		('agepreg', 284, 287, int),
		('finalwgt', 423, 440, float),
	]
	records = ReadFile(data_dir, filename, fields, Pregnancy)
	for record in records:
		# divide mother's age by 100
		try:
			if record.agepreg != 'NA':
				record.agepreg /= 100.0
		except AttributeError:
			pass
		# convert weight at birth from lbs/oz to total ounces
		# note: there are some very low birthweights
		# that are almost certainly errors, but for now I am not
		# filtering
		try:
			if (record.birthwgt_lb != 'NA' and record.birthwgt_lb < 20 and record.birthwgt_oz != 'NA' and record.birthwgt_oz <= 16):
				record.totalwgt_oz = record.birthwgt_lb * 16 + record.birthwgt_oz
			else:
				record.totalwgt_oz = 'NA'
		except AttributeError:
			pass
	return records
