#!/bin/bash

ossdir1=$1
ossdir2=$2
receiver=$3

ossutil cp -ru $ossdir1 $ossdir2
echo $ossdir1 upload to $ossdir2

python /data/users/wuliuyu/wuliuyu/python/dingtalkChatbot.py $ossdir2 $receiver
