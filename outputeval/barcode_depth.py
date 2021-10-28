#coding=utf-8
import os
import json
import time
import csv
import subprocess
import sys

#sample_sheet_dir ='/data/users/yangbo/task/'
#target_dir = '/thinker/nfs2/longrw/runPipelineInfo/task/target-dir/'
target_dir = sys.argv[1]
#data_dir = '/data/users/yangbo/data/novaseq_sz02/211014_A00250_0057_AHHV2LDSX2/'
#raw_dir = '/data/users/yangbo/rawfq/'
mode_dir = {'88a-8-8':['C168.1','-r 24 -p 24 -w 24 --tiles s_[1-8] --barcode-mismatches=0 --use-bases-mask Yn150,I*,I*,N150n -l TRACE'],
           '88a-10-10':['C172.1','-r 24 -p 24 -w 24 --tiles s_[1-8] --barcode-mismatches=0 --use-bases-mask Yn150,I8nn,I8nn,N150n -l TRACE'],
           '80a-8-8':['C160.1','-r 24 -p 24 -w 24 --tiles s_[1-8] --barcode-mismatches=0 --use-bases-mask Yn150,I*,N*,N150n -l TRACE'],
           '88b-8-8':['C168.1','-r 24 -p 24 -w 24 --tiles s_[1-8] --barcode-mismatches=1 --use-bases-mask Yn150,I*,I*,N150n -l TRACE'],
           '88b-17-8':['C177.1','-r 24 -p 24 -w 24 --tiles s_[1-8] --barcode-mismatches=1 --use-bases-mask Yn150,I8n9,I8,N150n -l TRACE --mask-short-adapter-reads=0 --minimum-trimmed-read-length=0']} #use-bases-mask参数

def main():
    #=======================读取target_dir======================     
    #target目录下需要存在文件 machine=batch=mode=service
    if os.listdir(target_dir) != []:
        data = open(target_dir + 'task1.csv')
        data_info = csv.reader(data)
        for info in data_info:
            if info[0] == 'batch':
                continue
            batch = info[0]     #批次号
            mode = info[1]      #bcl2fastq模式
            sample_sheet_name = info[2]
            mode2=os.path.basename(sample_sheet_name).split(".csv")[0].split("SampleSheet_")[-1]
            data_dir = info[3]  #bcl目录
            raw_dir = info[4] #拆分输出目录
            lane_num = info[5]
            output_dir = raw_dir +"/" +batch + '_' + mode2 + '_barcode'
#======================更改samplesheet===============            
            samplesheet_csv = []
            with open(sample_sheet_name,'r') as f:  #将samplesheet的reads从151改成1
                for read in csv.reader(f):
                    if read[0] == '151':
                        read[0] = '1'
                    samplesheet_csv.append(read)
            with open(target_dir + ("%s_%s" % (batch,sample_sheet_name.split('/')[-1])), "w") as w:
                writer = csv.writer(w)
                writer.writerows(samplesheet_csv)

            new_sample_sheet_name = target_dir + sample_sheet_name.split('/')[-1]

        #======================bcl2fastq===================
            #if os.path.isfile('{S3}{S1}/{S2}/Data/Intensities/BaseCalls/L001/0160.bcl.bgzf'.format(S1=machine,S2=batch,S3=data_dir)) \#550平台目录名
            if os.path.isdir('{S1}/Data/Intensities/BaseCalls/L001/{S2}'.format(S1=data_dir,S2=mode_dir[mode][0])) \
                and os.path.isfile(new_sample_sheet_name):   #检查是否存在BCL,samplesheet
                if os.path.isdir(output_dir) == 0:
                    os.system("mkdir -p %s" % output_dir) #创建输出文件夹
                print('bcl2fastq -R {S1} --sample-sheet {S4} -o {S5}/ \
                --stats-dir {S5}/html/ --reports-dir {S5}/html/ --interop-dir={S5}/Interop_html/ \
                {S3} > {S5}/bcl2fastq.txt'.format(S1=data_dir,S3=mode_dir[mode][1],S4=new_sample_sheet_name,S5=output_dir))
                
                os.system('bcl2fastq -R {S1} --sample-sheet {S4} -o {S5}/ \
                --stats-dir {S5}/html/ --reports-dir {S5}/html/ --interop-dir={S5}/Interop_html/ \
                {S3} > {S5}/bcl2fastq.txt'.format(S1=data_dir,S3=mode_dir[mode][1],S4=new_sample_sheet_name,S5=output_dir))
                    
        #======================解析json=======================
            if os.path.isfile('{S5}/html/Stats.json'.format(S5=output_dir)):
                output_csv = []
                with open('{S5}/html/Stats.json'.format(S5=output_dir),'r') as f:
                    data = json.load(f)
                    for lane in range(len(data['ConversionResults'])):
                        output_csv.append([data['ConversionResults'][lane]['LaneNumber']])  #lane数
                        tmp_sample = []
                        tmp_reads = []
                        for sample in range(len(data['ConversionResults'][lane]['DemuxResults'])):
                            tmp_sample.append(data['ConversionResults'][lane]['DemuxResults'][sample]['SampleId'])
                            tmp_reads.append(int(data['ConversionResults'][lane]['DemuxResults'][sample]['NumberReads']) * 300 // 1000000)
                        output_csv.append(tmp_sample+","+tmp_reads+"\n")             #样本名
                        #output_csv.append(tmp_reads)              #预测数据量
                with open(raw_dir + ("%s_%s" % (batch,sample_sheet_name.split('/')[-1])) + '-barcode.csv','w') as w:
                    writer = csv.writer(w)
                    writer.writerows(output_csv)
                    


if __name__ == "__main__":
    main()
