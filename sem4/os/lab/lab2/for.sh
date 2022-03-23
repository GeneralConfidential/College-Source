echo "Enter Size:"
read a
sum=0
echo "Enter Numbers"
for((i=1;i<=a;i++))
do
  read num
  sum=$((sum + num))
done
echo "Sum = $sum"