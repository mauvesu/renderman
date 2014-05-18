"""
use this module to clean the files in the failed job
"""

import os
from .config import cleanLogFile, hostNames
from ..cloudComputing.config import hdfsFolder

redirectCommand = ' >>' + cleanLogFile + ' 2>>' + cleanLogFile

def cleanFiles(job):
	if job.getJobType() == 'Render':
		jobName = job.getJobName()
		os.system("hadoop fs -rmr " + jobName + redirectCommand)
		# here the input suffix needs to change to config file maybe
		os.system('rm -rf ' + hdfsFolder + jobName + '-input')
		for hostName in hostNames:
			cleanCommand = ('''ssh %s "rm -rf %s%s"''') % (hostName, hdfsFolder, jobName)
			os.system(cleanCommand + redirectCommand)