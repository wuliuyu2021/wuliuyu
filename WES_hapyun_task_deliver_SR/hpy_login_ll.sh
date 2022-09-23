#!/usr/bin/expect
spawn /data/users/longrw/tools/hpycli/hpycli.py login
expect "*Username*"
send "liangshu@haplox.com\r"
sleep 2
expect "*Password*"
send "Liang18877547082\r"
expect eof
