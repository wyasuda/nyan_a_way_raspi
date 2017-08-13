#!/bin/bash

while true
do
  sleep 60
  box_mount_ok=`df | grep box | grep -v grep | wc -l`
  if [ $box_mount_ok -eq 0 ]; then
    mount /mnt/DAV/box
  fi

  nyan_a_way_alive=`ps -ef | grep nyan_a_way.py | grep -v grep | wc -l`
  if [ $nyan_a_way_alive -eq 0 ]; then
    /home/pi/nyan_a_way_raspi/code/nyan_a_way.py &
  fi
done
