#!/bin/bash
BG=$(df -h /home |tail -n 1 |awk -F" " '{print $3}' |awk -F"G" '{print $1}')
while [ 0 ];
do
if [ BG > 40 ];then

echo "echo "gm55a-1 /home ram unusual!""
python3 /thinker/nfs5/public/wuliuyu/wuliuyu/python/dingtalkChatbot.py gm55a-1\ home\ ram\ larger\ than\ 100G! wly
sleep 1min
else

echo "gm55a-1 /home ram normal!"
sleep 1min
fi
done
