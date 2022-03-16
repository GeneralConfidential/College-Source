echo "Enter"
echo "1 Files"
echo "2 Users"
echo "3 Delete File"
read ch
case $ch in
	1) echo "Files:"
	   'ls';;
	2) echo "Users:"
	   'who';;
   	3) echo "Delete:"
	   read $fil
           'rm' $fil;;
esac
