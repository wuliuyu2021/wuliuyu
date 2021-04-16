#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
import sys
import csv

csv='C:\\Users\\User\\Desktop\\wuliuyu\\csv_file\\HGC-info.csv'

def hgc_info():
	d1={}
	d2={}
	for line in open(csv, 'r'):
		lst = line.strip().split(',')
		d1[lst[0]]=lst[1]
		d2[lst[0]]=lst[4]
	return d1, d2

def excel_input(excel, outdir):
	d1=hgc_info()[0]
	d2=hgc_info()[1]
	out_excel=os.path.join(outdir, 'new_%s' % os.path.basename(excel))
	data1 = xlrd.open_workbook(excel, 'r')
	table1 = data1.sheets()[0]
	data2=xlwt.Workbook()
	table2 = data2.add_sheet("Haplox")
	sheet_1_name = data1.sheet_names()[0]
	nrows = table1.nrows
	ncols = table1.ncols
	print('行总数为%d, 列总数为%d' % (nrows, ncols))
	table2.write(0,0, '%s' % table1.col_values(0)[0])
	table2.write(0,1, '%s' % table1.col_values(1)[0])
	table2.write(0,2, '%s' % table1.col_values(2)[0])
	table2.write(0,3, '%s' % table1.col_values(3)[0])
	table2.write(0,4, '%s' % table1.col_values(4)[0])
	table2.write(0,5, '%s' % table1.col_values(5)[0])
	table2.write(0,6, '%s' % table1.col_values(6)[0])
	table2.write(0,7, '%s' % table1.col_values(7)[0])
	table2.write(0,8, '%s' % table1.col_values(8)[0])
	table2.write(0,9, '%s' % table1.col_values(9)[0])
	table2.write(0,10, '%s' % table1.col_values(10)[0])
	table2.write(0,11, '%s' % table1.col_values(11)[0])
	table2.write(0,12, '%s' % table1.col_values(12)[0])
	table2.write(0,13, '%s' % table1.col_values(13)[0])
	table2.write(0,14, '%s' % table1.col_values(14)[0])
	table2.write(0,15, '%s' % table1.col_values(15)[0])
	table2.write(0,16, '%s' % table1.col_values(16)[0])
	table2.write(0,17, '%s' % table1.col_values(17)[0])
	table2.write(0,18, '%s' % table1.col_values(18)[0])
	table2.write(0,19, '%s' % table1.col_values(19)[0])
	table2.write(0,20, '%s' % table1.col_values(20)[0])
	table2.write(0,21, '%s' % table1.col_values(21)[0])
	table2.write(0,22, '%s' % table1.col_values(22)[0])
	table2.write(0,23, '%s' % table1.col_values(23)[0])
	table2.write(0,24, '%s' % table1.col_values(24)[0])
	table2.write(0,25, '%s' % table1.col_values(25)[0])
	table2.write(0,26, '%s' % table1.col_values(26)[0])
	table2.write(0,27, '%s' % table1.col_values(27)[0])
	table2.write(0,28, '%s' % table1.col_values(28)[0])
	table2.write(0,29, '%s' % table1.col_values(29)[0])
	table2.write(0,30, '%s' % table1.col_values(30)[0])
	table2.write(0,31, '%s' % table1.col_values(31)[0])
	table2.write(0,32, '%s' % table1.col_values(32)[0])
	for i in range(1, int(nrows)):
		lt0 = table1.col_values(0)[i]
		lt1 = table1.col_values(1)[i]
		lt2 = table1.col_values(2)[i]
		lt3 = table1.col_values(3)[i]
		lt4 = table1.col_values(4)[i]
		lt5 = table1.col_values(5)[i]
		lt6 = table1.col_values(6)[i]
		lt7 = table1.col_values(7)[i]
		lt8 = table1.col_values(8)[i]
		lt9 = table1.col_values(9)[i]
		lt10 = table1.col_values(10)[i]
		lt11 = int(table1.col_values(11)[i])
		lt12 = table1.col_values(12)[i]
		lt13 = table1.col_values(13)[i]
		lt14 = table1.col_values(14)[i]
		lt15 = table1.col_values(15)[i]
		lt16 = table1.col_values(16)[i]
		lt17 = table1.col_values(17)[i]
		lt18 = table1.col_values(18)[i]
		lt19 = table1.col_values(19)[i]
		lt20 = table1.col_values(20)[i]
		lt21 = table1.col_values(21)[i]
		lt22 = float(table1.col_values(22)[i])
		lt23 = table1.col_values(23)[i]
		lt24 = table1.col_values(24)[i]
		lt25 = table1.col_values(25)[i]
		lt26 = table1.col_values(26)[i]
		lt27 = table1.col_values(27)[i]
		lt28 = table1.col_values(28)[i]
		lt29 = table1.col_values(29)[i]
		lt30 = table1.col_values(30)[i]
		lt31 = table1.col_values(31)[i]
		lt32 = table1.col_values(32)[i]
		if lt6 in d1.keys():
			table2.write(i,0, '%s' % lt0)
			table2.write(i,1, '%s' % lt1)
			table2.write(i,2, '%s' % lt2)
			table2.write(i,3, '%s' % lt3)
			table2.write(i,4, '%s' % lt4)
			table2.write(i,5, '%s' % lt5)
			table2.write(i,6, '%s' % d1[lt6])
			table2.write(i,7, '%s' % d2[lt6])
			table2.write(i,8, '%s' % lt8)
			table2.write(i,9, '%s' % lt9)
			table2.write(i,10, '%s' % lt10)
			table2.write(i,11, '%d' % lt11)
			table2.write(i,12, '%s' % lt12)
			table2.write(i,13, '%s' % lt13)
			table2.write(i,14, '%s' % lt14)
			table2.write(i,15, '%s' % lt15)
			table2.write(i,16, '%s' % lt16)
			table2.write(i,17, '%s' % lt17)
			table2.write(i,18, '%s' % lt18)
			table2.write(i,19, '%s' % lt19)
			table2.write(i,20, '%s' % lt20)
			table2.write(i,21, '%s' % lt21)
			table2.write(i,22, '%.2f' % lt22)
			table2.write(i,23, '%s' % lt23)
			table2.write(i,24, '%s' % lt24)
			table2.write(i,25, '%s' % lt25)
			table2.write(i,26, '%s' % lt26)
			table2.write(i,27, '%s' % lt27)
			table2.write(i,28, '%s' % lt28)
			table2.write(i,29, '%s' % lt29)
			table2.write(i,30, '%s' % lt30)
			table2.write(i,31, '%s' % lt31)
			table2.write(i,32, '%s' % lt32)
		else:
			table2.write(i,0, '%s' % lt0)
			table2.write(i,1, '%s' % lt1)
			table2.write(i,2, '%s' % lt2)
			table2.write(i,3, '%s' % lt3)
			table2.write(i,4, '%s' % lt4)
			table2.write(i,5, '%s' % lt5)
			table2.write(i,6, '%s' % lt6)
			table2.write(i,7, '%s' % lt7)
			table2.write(i,8, '%s' % lt8)
			table2.write(i,9, '%s' % lt9)
			table2.write(i,10, '%s' % lt10)
			table2.write(i,11, '%d' % lt11)
			table2.write(i,12, '%s' % lt12)
			table2.write(i,13, '%s' % lt13)
			table2.write(i,14, '%s' % lt14)
			table2.write(i,15, '%s' % lt15)
			table2.write(i,16, '%s' % lt16)
			table2.write(i,17, '%s' % lt17)
			table2.write(i,18, '%s' % lt18)
			table2.write(i,19, '%s' % lt19)
			table2.write(i,20, '%s' % lt20)
			table2.write(i,21, '%s' % lt21)
			table2.write(i,22, '%.2f' % lt22)
			table2.write(i,23, '%s' % lt23)
			table2.write(i,24, '%s' % lt24)
			table2.write(i,25, '%s' % lt25)
			table2.write(i,26, '%s' % lt26)
			table2.write(i,27, '%s' % lt27)
			table2.write(i,28, '%s' % lt28)
			table2.write(i,29, '%s' % lt29)
			table2.write(i,30, '%s' % lt30)
			table2.write(i,31, '%s' % lt31)
			table2.write(i,32, '%s' % lt32)
			print('Waring, %s_%s is not in HGC-info.csv, please check or add!\n' % (lt0, lt6))
	data2.save(out_excel)

def main():
	outdir=sys.argv[1]
	excel=sys.argv[2]
	excel_input(excel, outdir)

if __name__ == '__main__':
	main()