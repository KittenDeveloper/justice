use CGI qw(:all);
print "Content-type: text/html\n\n"; #<-- common http header
{
local $/ = undef;
open FILE, "chat.txt" or die "Couldn't open file: $!";
binmode FILE;
$text = <FILE>;
close FILE;
}
{
local $/ = undef;
open FILE, "curse.txt" or die "Couldn't open file: $!";
binmode FILE;
$curselist = <FILE>;
close FILE;
}
my $message = <<'END_LINE';
<form action=chatrec.pl method=post>
	<p>
<input type="radio" name="filter" value="yes" > Filter<br>
<input type="radio" name="filter" value="no"> No Filter<br>
<input type="submit" name="sumbit">
<p>
</form>
END_LINE
print $message;
if (param('filter') eq yes)
{
my $cookie = CGI->new->cookie(-name=>'filterstate',
			 -value=>'yes',
			 -expires=>'+10h',
			 -path=>'/');
print cookie("filterstate");
}
elsif (param('filter') eq 'no')
{
my $q = CGI->new;
my $cookie = $q->cookie (
                -name    => 'filterstate',
                -value   => '',
                -path    => '/',
                -expires => '-1d'
 );
}

#try{
@cursearray=split(' ',$curselist);
@textarray=split(' ',$text);
#print join(' ',@textarray);
$theCookie = cookie('filterstate');
print $theCookie;
if ($theCookie eq 'yes')
{
for my $i (@cursearray) {
for my $i1 (@textarray) {
if ($i eq $i1)
{
$i1 = '~CENSORED~'
}
}
}
print join(' ',@textarray)
}
else
{
print join(' ',@textarray);
}
#}
#catch{
#print $_;
#}
print '<meta http-equiv="refresh" content="2; url=/cgi-bin/chatrec.pl" />'