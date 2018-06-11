import os
import json
import sys
import time
import process_list

class ProcessControl:

    def __init__( self ):

        with open( "config.json" ) as fh:
            self.config = json.loads( fh.read() )
        
        # self.pause_list = self.config[ "PAUSE_PROCESS_LIST" ]
        self.pause_list = self.config[ "PAUSE_PROCESS_LIST" ]
        self.paused_pid_list = []

        self.commands = self.load_commands()

    def load_commands( self, path="commands.json" ):
        
        try:
            self.commands = {}
            
            with open( path ) as fh:
                self.commands = json.loads( fh.read() )

            display_port = os.popen( self.commands[ "GET_DISPLAY_PORT" ] ).read().strip("\n")
            
            brightness = self.commands[ "SET_BRIGHTNESS" ].encode('ascii','ignore')
            brightness = brightness.replace( "#DISPLAY_PORT", display_port )
            self.commands[ "SET_BRIGHTNESS" ] = brightness

            return self.commands

        except Exception as err:

            print "Exception @loadCommands : ", err

        return 
        
    def getPauseList( self ):

        return self.pause_list

    def get_process_list( self ):

        out = process_list.getList()
        self.process_list = out.split( "\n" )

    def pause_processes( self ):

        self.get_process_list()
        
        for process in self.process_list:

            if process in self.pause_list:
                
                for pid in process_list.getPidList(process) :
                    print os.popen( self.commands[ "PAUSE_PROCESS" ] + pid ).read()
                    self.paused_pid_list.append( pid )                    
                    
    def resume_processes( self ):
        
        for pid in self.paused_pid_list:

            os.system( self.commands[ "RESUME_PROCESS" ] + pid )
        
        self.paused_pid_list = []

if __name__ == "__main__":

    pc = ProcessControl()

    # pc.pause_processes()
    # import time
    # time.sleep( 5 )
    # pc.resume_processes()

    if len( sys.argv ) > 1:

        if sys.argv[1] == "-l":
            
            pc.get_process_list()
            print "\n".join( pc.process_list )
        
        elif sys.argv[1] == "-h":            
            pc.pause_processes()
            time.sleep( 3 )           
            pc.resume_processes()

        else :

            print "\n".join( pc.getPauseList() )