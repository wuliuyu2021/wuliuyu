#!/usr/expect/bin/expect
spawn /thinker/nfs5/public/wuliuyu/wuliuyu/WES_hapyun_task_deliver_SR/hpycli.py login
expect "*Username*"
send "gancw@haplox.com\r"
sleep 2
expect "*Password*"
send "HaploX2022\r"
expect eof
