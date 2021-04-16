@ARGV = qw# larry more curly #;
while (<STDIN>){
chomp;
print "it was $_ that I saw in some stooge-like file!\n";
}