import json
import os
import sys

def int( path="commands.json" ):

    global commands
    
    with open( path ) as fh:
        commands = json.loads( fh.read() )

def set_brightness( val ):

    display_port = os.popen( commands[ "GET_DISPLAY_PORT" ] ).read().strip("\n")
    brightness = commands[ "SET_BRIGHTNESS" ].encode('ascii','ignore')
    brightness = brightness.replace( "#DISPLAY_PORT", display_port )
    commands[ "SET_BRIGHTNESS" ] = brightness

    os.system( brightness+" "+val )

def get_brightness():

    val = os.popen( commands[ "GET_BRIGHTNESS" ] ).read()
    return val

if len( sys.argv ) > 1:
    if sys.argv[1] == "-s":
        val = int( sys.argv[2] )
        set_brightness( val )
    
else:
    print get_brightness

