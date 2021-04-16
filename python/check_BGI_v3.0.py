#!/usr/bin/python
# -*- coding:utf-8 -*-
###check_bgi.py

import os
import sys
import csv

def read_file_getsampleinfo(sampleinfo,sampleid,contractid):
    list_infos = [] 
    with open(sampleinfo,'r') as csv_file:    
        all_lines = csv.reader(csv_file)
        for one_line in all_lines:
            list_infos.append("%s,%s,%s,%s" % (one_line[0],one_line[1],one_line[6],one_line[5]))            
    samplename_contractids = []
    for list_info in list_infos:        
        if sampleid == list_info.split(",")[2]:
            samplename_contractids.append("%s,%s" % (list_info.split(",")[1],list_info.split(",")[3]))    
    samplename = []
    for samplename_contractid in samplename_contractids:
        if contractid == samplename_contractid.split(",")[1]:
            samplename.append("%s" % samplename_contractid.split(",")[0])
    list_sort = sorted(set(samplename),key=samplename.index)
    return list_sort

def get_dirinfo(dirpath):
    dirinfo = []
    for root,dirs,files in os.walk(dirpath): 
        for dir in dirs:
            dirinfo.append("%s" % (dir))
    return dirinfo

def main():
    sampleinfo = sys.argv[1]  # sequence_171205_E00602_0040_AH5GGYCCXY.csv
    dirpath = sys.argv[2]  # /home/hanjie/exercise/check/
    contractid = sys.argv[3]# 20171016F1A1_17
    sampleid = sys.argv[4] #BGI-WH
    
    list_sampleinfos = read_file_getsampleinfo(sampleinfo,sampleid,contractid)
    list_dirinfos = get_dirinfo(dirpath)
    list1, list2 = [], []     
    for list_sampleinfo in list_sampleinfos:
        if list_sampleinfo in list_dirinfos:
            list1.append("%s" % list_sampleinfo)
        else:
            list2.append("%s" % list_sampleinfo)    
    for x in list1: 
        count = 0
        eachdirpath = dirpath+x
        list3=[]
        for root,dirs,files in os.walk(eachdirpath):    #遍历统计
            for each in files:
                count += 1   #统计文件夹下文件个数
                if x == each.split('_')[0]:
                    list3.append(each.split('_')[4])
                    list3.append(each.split('_')[0]) 
        print(x,"Ok",count,list3)
    for y in list2:
        print(y,"False")   
    for z in list_dirinfos:
        if z not in list_sampleinfos:
            print(z,"Redundant")  

if __name__ == "__main__":
    main()