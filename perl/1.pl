
@fred = qw(eating rocks is wrong);
$fred = "right";
print "this is $fred[3]\n";
print "this is ${fred}[3]\n";
print "this is $fred"."[3]\n";
print "this is $fred\[3]\n";

foreach $rock (qw(bedrock slate lava)){
print "one rock is $rock.\n";
}

@rock = qw(bedrock slate lava);
foreach $rock (@rock){
$rock = "\t$rock";
$rock .= "\n";
}
print "the rock are:\n", @rock;

sub sum_of_fred_barney {
print "Hey, you called the sum_of_fred_barney!\n";
$fred + $barney;
}
$fred = 3;
$barney = 4;
$wilma = &sum_of_fred_barney;
print "\$wilma is $wilma.\n"

sub list_from_fred_to_barney {
	if ($fred < $barney){
		$fred..$barney;
} else {
		reverse $barney..$fred;
	}
}
$fred = 11;
$barney = 6;
@c = &list_from_fred_to_barney;
print "@c";