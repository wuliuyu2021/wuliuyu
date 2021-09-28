#!/usr/bin/perl -w
use strict;
use FindBin '$Bin';
use Cwd 'abs_path';
my ($indir,$odir)=@ARGV;
if(@ARGV!=2){
        print "perl $0 <indir> <odir>\n";
        exit;
}
$indir=abs_path($indir);
$odir=abs_path($odir);
open IN,"$indir";
open O,">$odir/plink.matrix";
select O;
<IN>;
my @sample;
my (%plink,%mark);
while(<IN>){
	chomp;
	my @c=split/\s+/;
    $c[1]="$c[1]_$c[2]";
    $c[3]="$c[3]_$c[4]";
	$plink{$c[1]}{$c[3]}=$c[-5];
	$plink{$c[3]}{$c[1]}=$c[-5];
	if(!defined $mark{$c[1]}){
		push @sample,$c[1];
		$mark{$c[1]}=1;
	}
	if(!defined $mark{$c[3]}){
		push @sample,$c[3];
		$mark{$c[3]}=1;
	}
}
my @sort = sort @sample;
print "ID";
for my $s(@sort){
	print "\t$s";
}
print "\n";
for my $s(@sort){
	print $s;
	for my $s2(@sort){
		if($s eq $s2){
			print "\t1";
		}else{
			print "\t$plink{$s}{$s2}";
		}
	}
	print "\n";
}
close IN;
`Rscript $Bin/heat.R $odir/plink.matrix $odir/plink && convert -density 300 -alpha off -resize 50% $odir/plink.heatmap.pdf $odir/plink.heatmap.png`;
