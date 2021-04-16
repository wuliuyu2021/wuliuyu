#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import time

def targetdir_exists(runfolderdir, laneid):
	targetdir = os.path.join(runfolderdir, "Data/Intensities/BaseCalls/L00%s" % laneid)
	while True:
		if  os.path.isdir(targetdir):
			print("%s :Targetdir exists: %s" % (targetdir, time.ctime()))
		else:
			print("Please waitting, targetdir not exists!!!")
			time.sleep(300)
			continue
		return False
	return targetdir
	
	

def check_upload(runfolderdir, laneid, expdir, totalcycle):
	if not os.path.exists('%s/L00%s' % (expdir, laneid)):
		os.makedirs('%s/L00%s' % (expdir, laneid))
	time_txt='%s/L00%s/time.txt' % (expdir, laneid)
	if not os.path.exists(time_txt):
		os.system("touch %s" %(time_txt))
	targetdir=targetdir_exists(runfolderdir, laneid)
	lsts=sorted([int(x) for x in range(1, int(totalcycle)+1)])
	for lst in range(1, int(totalcycle)+1):
		if os.path.exists("%s/Data/Intensities/BaseCalls/L00%s/C%s.1" % (runfolderdir, laneid, lst)) and not os.path.exists("%s/L00%s/%s.exp" % (expdir, laneid, lst)):
			os.system("sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/bcl_ftp_cycles.sh %s %s %s %s/Data/Intensities/BaseCalls/L00%s/C%s.1 %s" %
				(expdir, laneid, lst, runfolderdir, laneid, lst, os.path.basename(runfolderdir)))
			os.system("echo  '[%s]: L00%s:%s sequencing complete' >> %s" %(time.ctime(), laneid, lst, time_txt))
			#time.sleep(900)
			#os.system("/usr/expect/bin/expect %s/L00%s/%s.exp" %(expdir, laneid, lst))
			os.system("echo  '[%s]: L00%s:%s is uploaded by sftp' >> %s" %(time.ctime(), laneid, lst, time_txt))
	if os.path.exists("%s/SequencingComplete.txt" %runfolderdir) or  os.path.exists("%s/SequenceComplete.txt" %runfolderdir):
		os.system("sh /thinker/nfs5/public/wuliuyu/wuliuyu/shell/bcl_ftp_config.sh %s %s %s %s "%(expdir, laneid, runfolderdir, os.path.basename(runfolderdir) ))
		#os.system("/usr/expect/bin/expect  %s/L00%s/config.exp" % (expdir, laneid))
		os.system("echo '[%s]: Sequencing Complete' >> %s" %(time.ctime(), time_txt))
		print("Sequencing Complete!!!")
		os.system("echo '[%s]: Uploading Complete' >> %s" %(time.ctime(), time_txt))
		#sys.exit(0)
	return lsts
	
		
def main():
	runfolderdir=sys.argv[1]
	laneid=sys.argv[2]
	totalcycle=sys.argv[3]
	expdir=sys.argv[4]
	check_upload(runfolderdir, laneid, expdir, totalcycle)
	while True:
		lsts=check_upload(runfolderdir, laneid, expdir, totalcycle)
		
		if lsts != "":
			time.sleep(300)
			check_upload(runfolderdir, laneid, expdir, totalcycle)
		else:
			print("Seqencing complete!!!")
			break



if __name__ == '__main__':
	main()