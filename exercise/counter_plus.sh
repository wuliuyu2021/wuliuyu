#!/bin/bash
read -p "Please input an integer number: " number
i=0
s=0
while [ "$i" != "$number" ]
do
i=$(($i+1))
s=$(($s+$i))
done
echo "the result of '1+2+3+...+$number' is ==> $s"