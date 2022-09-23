#!/usr/expect/bin/expect
spawn python2 /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py login
expect "*Username*"
send "liangshu@haplox.com\r"
sleep 2
expect "*Password*"
send "Liang18877547082\r"
expect eof
