echo "Enter"
read a
if [ $a -gt 0 ]
then
	echo "$a is positive"
elif [ 0 -gt $a ]
then
	echo "$a is negative"
else
	echo "$a is zero"
fi

