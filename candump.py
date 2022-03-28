#!/usr/bin/env python3

import logging
import time
from datetime import datetime
import can
import os


can_name = 'can0'
bus_type = 'socketcan'
baudrate = '1000000'
human_time = True
add_buffer = False
step = 0

#setup part
print(str(step) + ' - Set ' + can_name + ' down')
os.system('sudo /sbin/ip link set ' + can_name + ' down')
step += 1
if add_buffer != False:
  print(str(step) + '- Set a bigger buffer')
  os.system('sudo ifconfig ' + can_name + ' txqueuelen 1000')
  step += 1

print(str(step) + ' - Set ' + can_name + ' parameters')
os.system('sudo ip link set ' + can_name + ' type can bitrate ' + baudrate + ' loopback on')
step += 1

print(str(step) + ' - set ' + can_name + ' up')
os.system('sudo ip link set ' + can_name + ' up')
step += 1

print(str(step) + ' - Details of ' + can_name + ' :')
os.system('sudo ip -details link show ' + can_name)
step += 1

time.sleep(0.1)

#connection part
try:
    bus = can.interface.Bus(channel=can_name, bustype=bus_type)
except OSError:
    print('Cannot find PiCAN \"' + can_name + '\" with bus type \"' + bus_type + '\"')
    exit()
print(str(step) + ' - Ready to receive...')

#receive and print part
try:
    while True:
        message = bus.recv()
        timestamp = '{0:f}'.format(message.timestamp)
        if human_time == True:
          ts = int(message.timestamp)
          timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        head = '{0:x} {1:x} '.format(message.arbitration_id, message.dlc)
        head = timestamp + ' ' + head
        content=''
        for i in range(message.dlc):
          content +=  '{0:x} '.format(message.data[i])
        print(' {}'.format(head+content))

# Exit event part
except KeyboardInterrupt:
    os.system('sudo ip link set ' + can_name + ' down')
    print('\n\rExit with keyboard succeed.')
