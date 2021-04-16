#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys

#outdir='/thinker/nfs5/public/rawdata'

def sample_lane_count(timedir, outdir):
	lsts=[]
	
	for root, dirnames, files in os.walk('/thinker/nfs2/longrw/runPipelineInfo/%s' % timedir):
		for dirname in dirnames:
			lsts.append(os.path.basename(dirname))
	return lsts

if __name__ == '__main__':
	timedir=sys.argv[1]
	outdir=sys.argv[2]
	lsts = sample_lane_count(timedir, outdir)
	out_sample_csv=os.path.join(outdir, 'sample_%s_merge.csv' % timedir)
	out_lane_csv=os.path.join(outdir, 'lane_%s_merge.csv' % timedir)
	out_fast_lane_csv=os.path.join(outdir, 'lane_all_%s_merge.csv' % timedir)
	out_seqcsv=os.path.join(outdir, 'seqcsv_all_%s_merge.csv' % timedir)
	if os.path.exists(out_sample_csv):
		os.remove(out_sample_csv)
	if os.path.exists(out_lane_csv):
		os.remove(out_lane_csv)
	out_sample_file=open(out_sample_csv, 'w')
	out_fast_lane_file=open(out_fast_lane_csv, 'w')
	out_seqcsvs=open(out_seqcsv, 'w')
	os.system('cat /thinker/nfs2/longrw/runPipelineInfo/%s/*/07_qc_o/*A_fast_lane_qc.csv /thinker/nfs2/longrw/runPipelineInfo/%s/*/07_qc_o/*B_fast_lane_qc.csv  /thinker/nfs2/longrw/runPipelineInfo/%s/*/07_qc_o/*C_fast_lane_qc.csv > %s/%s_fast_lane_qc.csv' % 
		(timedir, timedir, timedir, outdir, timedir))
	for lst in sorted(lsts):
		f = '/thinker/nfs2/longrw/runPipelineInfo/%s/%s/07_qc_o/%s_sample_qc.csv' % (timedir, lst, lst)
		#d = '/thinker/nfs2/longrw/runPipelineInfo/%s/%s/07_qc_o/%s_lane_qc.csv' % (timedir, lst, lst)
		e = '/thinker/nfs2/longrw/runPipelineInfo/%s/%s/07_qc_o/%s_all_lane_qc.csv' % (timedir, lst, lst)
		g = '/thinker/nfs2/longrw/runPipelineInfo/%s/%s/sequence_%s_utf-8.csv' % (timedir, lst, lst)
		if os.path.exists(f):
			for line in open(f):
				out_sample_file.write("%s\n" % line.strip())
		if os.path.exists(e):
			for line in open(e):
				out_fast_lane_file.write("%s\n" % line.strip())
		if os.path.exists(g):
			for line in open(g):
				out_seqcsvs.write("%s\n" % line.strip())
	out_sample_file.close()
	out_fast_lane_file.close()