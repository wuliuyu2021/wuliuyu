#!/usr/bin/expect
spawn /data/users/longrw/tools/hpycli/hpycli.py login
expect "*Username*"
send "gancw@haplox.com\r"
sleep 2
expect "*Password*"
send "HaploX2022\r"
expect eof
