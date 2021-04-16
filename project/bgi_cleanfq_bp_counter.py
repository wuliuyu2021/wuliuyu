#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys
from sr_seqcsv import Seqcsv
from multiprocessing import Pool

def sample_info_preparation(seqcsv, pid):
	ld=[]
	for line in open(seqcsv):
		lst = Seqcsv(line.strip().split(','))
		if lst.projectID == pid:
			l_info='%s_%s_%s' % (lst.ordID, lst.projectID, lst.libID)
			ld.append(l_info)
	if ld is None:
		print('Warning, Wrong pid, Please check!!!' * 3)
	return ld

def get_dirnames(indir, pid, seqcsv):
	sr1s_new=[]
	ln=[]
	ln1=[]
	ld=sample_info_preparation(seqcsv, pid)
	pattern = re.compile(r"(^S\d+)(_%s_)(.+)(_R1)(_001.fastq.gz|_001.good.fastq.gz)$" % pid)
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr in srs:
		if '%s' % '_'.join(sr.split("_")[:3]) in ld:
			ln1.append(sr.split('_')[5][-1])
			sr1s_new.append(sr)
	ln=sorted(set(ln1))

	return sr1s_new, ln

def bp_counter(indir, f, usbdir):
	os.system('gzip -dc %s/%s | wc -l > %s/%s.txt' % (indir, f, usbdir, f))

def bp_counter_multi(args):
	indir=args[0]
	f=args[1]
	usbdir=args[2]
	bp_counter(indir, f, usbdir)

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()

def multi_gzip(indir, pid, usbdir, seqcsv):
	if not os.path.exists(usbdir):
		os.makedirs(usbdir)
	args=[]
	sr1s=get_dirnames(indir, pid, seqcsv)[0]
	for sr1 in sr1s:
		args.append((indir, sr1, usbdir))
		sr2=sr1.replace("_R1_001", "_R2_001")
		args.append((indir, sr2, usbdir))
	multi_process(bp_counter_multi, args, 2)

def info_writer(indir, seqcsv, usbdir, pid):
	os.chdir(usbdir)
	clean1,clean2,clean3,clean4,clean5,clean6,clean7,clean8=[],[],[],[],[],[],[],[]
	head_sample_line=('seqID,LaneID,Sample,libID,R1_read_num,Yes/No,R2_read_num,Clean_Yeild(G)')
	sam_lst=open('%s_%s_cleanfq_sample.csv' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), pid), 'w')
	sam_lst.write(head_sample_line+"\n")
	head_lane_line=('seqID,LaneID,Clean_Yeild(G)')
	ln=get_dirnames(indir, pid, seqcsv)[1]
	lane_lst=open('%s_%s_cleanfq_lane.csv' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), pid), 'w')
	lane_lst.write(head_lane_line+"\n")
	for root, dirs, file1s in os.walk(usbdir):
		file1s.sort()
		for file1 in file1s:
			if file1.endswith('R1_001.fastq.gz.txt') or file1.endswith('R1_001.good.fastq.gz.txt'):
				file2=file1.replace("_R1_001", "_R2_001")
				ls1=[line.strip() for line in open(file1, 'r')]
				ls2=[line.strip() for line in open(file2, 'r')]
				if ls1[0] == ls2[0]:
					int_ls1=list(map(int, ls1))
					int_ls2=list(map(int, ls2))
					fc=float(float((int_ls1[0]+int_ls2[0]) * 150 / 4) / 1000**3)
					sam_lst.write('%s,%s,%s,%s,%d,Yes,%d,%.4f\n'% ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), 
						file1.split('_')[5][-1], file1.split('_')[0], file1.split('_')[2], 
						int_ls1[0]/4, int_ls2[0]/4, fc))
				else:
					sam_lst.write('%s,%s,%s,%s,%d,No,%d,%.4f\n'% ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), 
						file1.split('_')[5][-1], file1.split('_')[0], file1.split('_')[2], 
						int_ls1[0]/4, int_ls2[0]/4, fc))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '1':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,1,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean1)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '2':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,2,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean2)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '3':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,3,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean3)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '4':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,4,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean4)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '5':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,5,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean5)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '6':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,6,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean6)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '7':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean7.append(fc)
		lane_lst.write('%s,7,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean7)))
	for root, dirs, files in os.walk(usbdir):
		files.sort()
		for file in files:
			ft=file.split('_')[5][-1]
			if ft in ln and ft == '8':
				ls=[line.strip() for line in open(file, 'r')]
				int_ls=list(map(int, ls))
				fc=float((float(int_ls[0]) * 150 / 4) / 1000**3)
				clean8.append(fc)
		lane_lst.write('%s,8,%.4f\n' % ('_'.join(os.path.basename(seqcsv).split('.csv')[0].split('_')[1:5]), sum(clean8)))	
	lane_lst.close()
	sam_lst.close()
	

def main():
	indir = sys.argv[1]
	usbdir = sys.argv[2]
	seqcsv = sys.argv[3]
	pid = sys.argv[4]
	multi_gzip(indir, pid, usbdir, seqcsv)
	info_writer(indir, seqcsv, usbdir, pid)

if __name__ == '__main__':
	main()