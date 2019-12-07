#!/usr/bin/env python
#this will list the network in the machine

import subprocess #here importing the subprocess
subprocess.call("ifconfig",shell=True)  #calling the availab;le network in using the subprocess funstion
#here are we are downing the the usb using wifi usb name taht is "wlan0"
subprocess.call("ifconfig wlan0 down",shell=True)
#here after downing the wifi usb i am changing the mac addresses u need to addad only 6 mac addressess
subprocess.call("ifconfig wlan0 hw ether 00:11:33:44:55:66",shell=True)
#here fter changing the mac addresses i am making to change into a available state like active
subprocess.call("ifconfig wlan0 up",shell=True)
#for my confirmation here i am whether  did that mac addr changed or not
subprocess.call("macchanger -s wlan0",shell=True)






