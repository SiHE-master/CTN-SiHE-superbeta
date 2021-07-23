#!/bin/bash
PING=`ping -c 3 $1 | grep '3 received' | wc -l`
echo $PING


