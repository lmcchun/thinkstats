# -*- coding: utf-8 -*-

import os
import sys

from survey import ReadRespondents, ReadPregnancies
from thinkstats import Mean

def main(name, data_dir='.'):
	respondents = ReadRespondents(data_dir, '2002FemResp.dat.gz')
	print 'Number of respondents', len(respondents)

	pregnancies = ReadPregnancies(data_dir, '2002FemPreg.dat.gz')
	print 'Number of pregnancies', len(pregnancies)

	success = [pregnancy for pregnancy in pregnancies if pregnancy.outcome == 1]
	first = [pregnancy for pregnancy in success if pregnancy.birthord == 1]
	other = [pregnancy for pregnancy in success if pregnancy.birthord != 1]
	print('first: {0}'.format(Mean([pregnancy.prglength for pregnancy in first])))
	print('other: {0}'.format(Mean([pregnancy.prglength for pregnancy in other])))

if __name__ == '__main__':
	os.chdir('E:\\thinkstats')
	main(*sys.argv)