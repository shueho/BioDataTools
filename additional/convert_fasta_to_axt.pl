#!/usr/bin/perl
#The function of this perl script converts the fasta format of MEGA software into the axt format required by the KaKs_Calculator software.
#Usage: perl convert_fasta_to_axt.pl example.fasta.

use warnings;
use strict;

open IN,"$ARGV[0]"; 
my ($name) = $ARGV[0] =~ /(.*)\.fas/;
open OUT,">$name.axt";

my %seq = ();
local $/ = ">";
<IN>;
while (<IN>) {
  s/>//;
  my @a = split/\n/,$_,2;
  $a[1] =~ s/\n//g;
  my @b = split/\s+/,$a[0];
  $seq{$b[0]} = $a[1];
}
close IN;

my @keys = keys %seq;
foreach my $i (0..$#keys) {
  foreach my $j (0..$#keys) {
    if ($i < $j) {
      print OUT "$keys[$i]-$keys[$j]\n$seq{$keys[$i]}\n$seq{$keys[$j]}\n\n";
    }
  }
}
close OUT;