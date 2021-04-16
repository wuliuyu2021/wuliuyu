#!/usr/bin/perl -w
use strict;
die <perl get_all_match_geneID_readscount.pl all_match_id.txt All.HTSeq.ReadsCount.xls All.HTSeq.ReadsCount.new.xls> if @ARGV==0;
my $in1=shift;
my $in2=shift;
my $out=shift;
my %hash;
my @arr;
open F,"$in1" or die;
while(<F>){
	chomp;
	my @aa=split/\t/;
	$hash{$aa[0]}=$aa[1];
}
close F;
open I,"$in2" or die;
open O,"+>$out" or die;
while(<I>){
	chomp;
	@arr=split/\t/,$_;
	if (/^GeneName/ || /^AccID/){
		print O "$_\tEnsemblID\n";
	}
	else{
		if($hash{$arr[0]}){
	      		print O "$_\t$hash{$arr[0]}\n";
		}
	}
}

close I;
close O;	
