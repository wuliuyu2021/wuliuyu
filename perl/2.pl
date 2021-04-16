sub total{
my $sum = 0;
foreach (@_)
{
$sum = $sum + $_;
}
$sum;
}
my @fred = qw( 1 3 5 7 9);
my $fred_total = total(@fred);
print "the total of \@fred is $fred_total.\n";
#print "enter some numbers on separate lines:";
#my $user_total = total(<STDIN>);
#print "the total of those number is $user_total.\n";

my @greny = 1..1000;
my $greny_total = total(@greny);
print "the greny_total is $greny_total\n.";



greet ("fred");
greet ("barney");
greet ("alice");
sub greet {
state $last_person;
my $name = shift;
print "Hi, $name";
if (defined $last_person){
print "$last_person is also here!\n";
}else{
print "you are the first one here!\n";
}
$last_person = $name;
}




my @fred = above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = above_average(100, 1..10);
print "\@barney is @barney\n";
print "(Should be just 100)\n";
sub total {
my $sum;
foreach (@_){
$sum += $_;
}
$sum;

}
sub average{
if (@_==0){return}
my $count = @_;
my $sum = total(@_);
$sum/$count
}

sub above_average{
$average = average(@_);
my @above_number;
foreach my $element(@_){
if ($element > $average){
push @above_number, $element;
}
}
@above_number;
}