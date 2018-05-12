import json
import os
import sys

def init( path="commands.json" ):

    global commands
    
    with open( path ) as fh:
        commands = json.loads( fh.read() )

def set_brightness( val ):

    display_port = os.popen( commands[ "GET_DISPLAY_PORT" ] ).read().strip("\n")
    brightness = commands[ "SET_BRIGHTNESS" ].encode('ascii','ignore')
    brightness = brightness.replace( "#DISPLAY_PORT", display_port )
    commands[ "SET_BRIGHTNESS" ] = brightness

    os.system( brightness+" "+str( val ) )

def get_brightness():

    val = os.popen( commands[ "GET_BRIGHTNESS" ] ).read()
    return val

init()

if len( sys.argv ) > 1:
    if sys.argv[1] == "-s":
        val = float( sys.argv[2] )

        if val <1.0 and val>0.0:
            set_brightness( val )
    
else:
    print get_brightness()

