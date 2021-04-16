while (defined($line = <STDIN>)){
print "I saw $line"
}

while (<STDIN>){
print "I saw $_"
}