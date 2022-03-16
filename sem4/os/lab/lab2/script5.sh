myfunc()
{
	echo "as $@"
	x=2
}
echo "with $@"
x=1
echo "x is $x"
myfunc 1 2 3
echo "x is $x"
