#! /bin/bash
#ctn.sh
PID=$(ps -ef|grep ctn.py|gawk '$0 !~/grep/ {print $2}' |tr -s '\n' ' ')
if [ "$PID" = "" ]
then
  nohup python3 ctn.py &
else
  kill -9 $(ps -ef|grep ctn.py|gawk '$0 !~/grep/ {print $2}' |tr -s '\n' ' ')
  nohup python3 ctn.py &
fi
