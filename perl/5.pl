$family_name{'fred'} = 'flintstone';
$family_name{'barney'} = 'rubble';
foreach my $person (qw/ barney fred /){
print "I've heard of $person $family_name{$person}.\n";
}

$book{'fred'} = 3;
$book{'wilma'} = 1;
if ($book{$someone}){
print "$someone has at least one book checked out.\n";
}
if (exists $book{'fred'}){
print "there has at least one book checked out.\n";
}

