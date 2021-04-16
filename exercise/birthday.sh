#!/bin/bash
read -p "Please input your birthday (MMDD, ex>0709):" birthday
now=`date + %m%d`
echo "$now"
if [ "$birthday" = "$now" ]; then
echo "Happy birthday to you!!!"
elif [ "$birthday" -gt "$now" ];then
year=`date + %y`
total_day=$(($((`date --date="$Year$birthday + %s"`-`date + %s`))/60/60/24))
echo "Your birthday will be $total_day later"
else
year=$((`date + y%` + 1))
total_day=$(($((`date --date="$Year$birthday + %s"`-`date + %s`))/60/60/24))
echo "Your birthday will be $total_day later"
fi
