#!/usr/bin/expect
spawn /data/users/longrw/tools/hpycli/hpycli.py login
expect "*Username*"
send "chouyk@haplox.com\r"
sleep 2
expect "*Password*"
send "Jkrt5013\r"
expect eof
