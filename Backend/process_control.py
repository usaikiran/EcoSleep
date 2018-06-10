import os
import json
import main
import sys
import process_list

class ProcessControl:

    def __init__( self ):

        with open( "config.json" ) as fh:
            self.config = json.loads( fh.read() )
        
        # self.pause_list = self.config[ "PAUSE_PROCESS_LIST" ]
        self.pause_list = self.config[ "PAUSE_PROCESS_LIST" ]
        self.paused_pid_list = []

        self.commands = main.load_commands()

    def getPauseList( self ):

        return self.pause_list

    def get_process_list( self ):

        self.commands = main.load_commands()
        out = process_list.getList()
        self.process_list = out.split( "\n" )

    def pause_processes( self ):

        self.get_process_list()

        self.commands = main.load_commands()
        
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
        
        else :

            print "\n".join( pc.getPauseList() )