# candump-py
This script works like the command "candump [port]" from Linux CAN-UTILS<br/>
the difference is that it will also init your **CAN** name, set up to a specific **baudrate** and on a specific **bus type**<br/>
you can also choose the time format (timestamp or human)<br/>

# Parameters
You can change thoses differents parameter at the top of the file candump.py :<br/>
**can_name** = 'can0'<br/>
**bus_type** = 'socketcan'<br/>
**baudrate** = '1000000'<br/>
**human_time** = True<br/>
**add_buffer** = False<br/>

# how to launch
To launch it, you just have to do :<br/>
python3 candump.py<br/>

