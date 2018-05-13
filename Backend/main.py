
'''

MAIN SCRIPT , CONTROLS < BRIGHTNESS / MONITOR STATE / BACKGROUND PROCESSES >

Terminal Commands used :

Display Port : xrandr | sed '2!d' | awk '{print $1}'
'''

from __future__ import division

import sys
import os
import threading
import json
import time
from collections import namedtuple
from datetime import datetime

try:

    import dlib
    import cv2
    import keyboard
    from pynput import mouse

except Exception as err:

    import install_dependencies

try:

    from detector import *
    import mouse_listener
    import process_control

except Exception as err:

    print err


def state_handler( state=None ):

    global monitor_state

    if state is None:
        return monitor_state
    else:
        monitor_state = state


def load_commands( path="commands.json" ):

    global commands
    
    with open( path ) as fh:
        commands = json.loads( fh.read() )

    display_port = os.popen( commands[ "GET_DISPLAY_PORT" ] ).read().strip("\n")
    
    brightness = commands[ "SET_BRIGHTNESS" ].encode('ascii','ignore')
    brightness = brightness.replace( "#DISPLAY_PORT", display_port )
    commands[ "SET_BRIGHTNESS" ] = brightness

    return commands


def init():

    load_commands()


def set_brightness( value=1.0 ):

    os.system( commands[ "SET_BRIGHTNESS" ] + str( value ) )
    

# interval-unit -> seconds
def brightness_transition(  action="OFF", time_period=3, target_brightness=0, current_brightness=None ):

    global pc

    if current_brightness == None:
        current_brightness = float( os.popen( commands[ "GET_BRIGHTNESS" ] ).read() )
    
    diff = abs( target_brightness - current_brightness )
    delay = 0.05

    while True:    

        current_brightness += ( 2*monitor_state-1 )*0.03
        if current_brightness<0 or current_brightness>1 :
            break
        
        time.sleep( delay )

        if monitor_state == 1 and action == "OFF":
            set_brightness(1.0)
            #brightness_transition( "ON", 1, 1, current_brightness )
            return

        set_brightness( current_brightness )

    if current_brightness<0 and action=="OFF":
        set_brightness( 0 )

    os.system( commands[ "MONITOR_"+action ] )
    pc.pause_processes()


def init_brightness_transition():

    threading.Thread( target = brightness_transition ).start()
    print "init brightness_transition", datetime.now()


def reset_monitor_state( *args ):    

    global monitor_state, pc, dlib_detector

    monitor_state = 1
    dlib_detector.non_face_count = 0

    set_brightness( 1.0 )
    os.system( commands[ "MONITOR_ON" ] )

    pc.resume_processes()

    print "on", datetime.now()


if __name__ == "__main__":

    global monitor_state, dlib_detector, pc
    
    monitor_state = 1
    init()

    pc = process_control.ProcessControl()
    #mouse = mouse_listener.MouseListener()

    keyboard.on_press( reset_monitor_state )
    #mouse.on_mouse_action( reset_monitor_state )
    
    dlib_detector = Detector()
    dlib_detector.wait_time = 4
    dlib_detector.run_detector( on = reset_monitor_state, off = init_brightness_transition, state = state_handler )

    reset_monitor_state()
    