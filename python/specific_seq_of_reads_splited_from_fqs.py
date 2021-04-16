import pysam
from optparse import OptionParser
import os,sys,re
import gzip
import regex
from multiprocessing import Pool

'''
read 1 contain yhy specific sequence
requrie python2
'''

'''def parse_cmd():
	usage="To split the reads of Specific sequences from fq files!"
	version="%prog 1.0"
	parser = OptionParser(usage=usage, version=version)
	parser.add_option("-i","--indir",dest="indir",default=None,help="fq indirs")
	parser.add_option("-s","--seq",dest="seq",default=None,help="the Specific sequences")
	#parser.add_option("-p","--outfile",dest="outfile",default=None,help="input ccc")
	parser.add_option("-o","--outdir",dest="outdir",default=None,help="fq outdirs")
	
	return parser.parse_args()'''


def get_file(indir):
	l1=[]
	l2=[]
	pattern=re.compile(r"(.+)(_R1)(.+)(001.fastq.gz|fastq.gz|fq.gz)$")
	srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))
	for sr1 in srs:
		if os.path.exists(sr1.replace("_R1", "_R2")) and not os.path.exists(sr1.replace("_R1", "_R3")):
			l2.append(sr1)
		if os.path.exists(sr1.replace("_R1", "_R2")) and os.path.exists(sr1.replace("_R1", "_R3")):
			l1.append(sr1)
	print(l1)
	print(l2)
	return l1, l2

def multi_process(func, args, n=None):
	p=Pool(n)
	p.map(func, args)
	p.close()
	p.join()

def reads_split_multi1(args):
	r1=args[0]
	r2=args[1]
	r3=args[2]
	indir=args[3]
	seq=args[4]
	outdir=args[5]

	reads_split1(r1, r2, r3, indir, seq, outdir)

def reads_split_multi2(args):
	r1=args[0]
	r2=args[1]
	indir=args[2]
	seq=args[3]
	outdir=args[4]

	reads_split2(r1, r2, indir, seq, outdir)

def reads_split1(r1, r2, r3, indir, seq, outdir):

	read1="%s/%s" % (indir, r1)
	read2="%s/%s" % (indir, r2)
	read3="%s/%s" % (indir, r3)
	
	outfiles = ("%s/%s_aa_R1.fastq.gz" % (outdir, r1.split('_R1')[0]), 
	"%s/%s_aa_R2.fastq.gz" % (outdir, r2.split('_R2')[0]), 
	"%s/%s_aa_R3.fastq.gz" % (outdir, r3.split('_R3')[0]), 
	"%s/%s_bb_R1.fastq.gz" % (outdir, r1.split('_R1')[0]),
	"%s/%s_bb_R2.fastq.gz" % (outdir, r2.split('_R2')[0]))
	
	fouts = [ gzip.open(f,'wb') for f in outfiles]
	c,j,k = 0,0,0
	kk = 0
	with pysam.FastxFile(read1) as fin_a, pysam.FastxFile(read2) as fin_b, pysam.FastxFile(read3) as fin_c:
		for reada in fin_a:
			readb = fin_b.next()
			readc = fin_c.next()
			c += 1
			if c % 5000000 == 0:
				print('processed %d' %c)
			if reada.name != readb.name:
				print("read names not equal.")
				os.exit()
			else:
				read1 = reada.sequence
				p1=regex.findall(r'(%s){s<=2}' % seq, read1)
				if p1:
					k += 1
					fouts[3].write(str(reada)+'\n')
					fouts[4].write(str(readc)+'\n')
				else:
					j += 1
					fouts[0].write(str(reada)+'\n')
					fouts[1].write(str(readb)+'\n')
					fouts[2].write(str(readc)+'\n')
	print('processed %d' %c)
	print('%d, %d, %d' %(c,j,k))
	[x.close() for x in fouts]

def reads_split2(r1, r2, indir, seq, outdir):

	read1="%s/%s" % (indir, r1)
	read2="%s/%s" % (indir, r2)

	outfiles = ("%s/%s_aa_R1.fastq.gz" % (outdir, r1.split('_R1')[0]), 
	"%s/%s_aa_R2.fastq.gz" % (outdir, r2.split('_R2')[0]), 
	"%s/%s_bb_R1.fastq.gz" % (outdir, r1.split('_R1')[0]),
	"%s/%s_bb_R2.fastq.gz" % (outdir, r2.split('_R2')[0]))
	
	fouts = [ gzip.open(f,'wb') for f in outfiles]
	c,j,k = 0,0,0
	kk = 0
	with pysam.FastxFile(read1) as fin_a, pysam.FastxFile(read2) as fin_b:
		for reada in fin_a:
			readb = fin_b.next()
			#readc = fin_c.next()
			c += 1
			if c % 5000000 == 0:
				print('processed %d' %c)
			if reada.name != readb.name:
				print("read names not equal.")
				os.exit()
			else:
				read1 = reada.sequence
				p1=regex.findall(r'(%s){s<=2}' % seq,read1)
				if p1:
					k += 1
					fouts[2].write(str(reada)+'\n')
					fouts[3].write(str(readb)+'\n')
				else:
					j += 1
					fouts[0].write(str(reada)+'\n')
					fouts[1].write(str(readb)+'\n')
				
	print('processed %d' %c)
	print('%d, %d, %d' %(c,j,k))
	[x.close() for x in fouts]		

def main():
	#(options, args) = parse_cmd()
	indir=sys.argv[1]
	seq=sys.argv[2]
	outdir=sys.argv[3]
	num=sys.argv[4]
	argv1s=[]
	argv2s=[]
	ls1=get_file(indir)[0]
	ls2=get_file(indir)[1]
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	os.chdir(indir)
	for read1 in ls1:
		read2=read1.replace("_R1", "_R2")
		read3=read1.replace("_R1", "_R3")	
		argv1s.append((read1, read2, read3, indir, seq, outdir))
	multi_process(reads_split_multi1, argv1s, int(num))
	print(argv1s)
	for read1 in ls2:
		read2=read1.replace("_R1", "_R2")
		argv2s.append((read1, read2, indir, seq, outdir))
	multi_process(reads_split_multi2, argv2s, int(num))
	print(argv2s)



if __name__=="__main__":
	main() 
