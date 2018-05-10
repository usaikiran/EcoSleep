import os
import json
import main
import sys

class ProcessControl:

    def __init__( self ):

        with open( "config.json" ) as fh:
            self.config = json.loads( fh.read() )
        
        self.pause_list = self.config[ "PAUSE_PROCESS_LIST" ]
        self.paused_pid_list = []


    def get_process_list( self ):

        self.commands = main.load_commands()
        out = os.popen( self.commands[ "GET_PROCESS_LIST" ] ).read()
        self.process_list = out.split( "\n" )


    def pause_processes( self ):

        self.get_process_list()

        for process in self.process_list:

            if process in self.pause_list:

                cmd = self.commands[ "GET_PROCESS_ID" ].replace( "#PROCESS_NAME", process )
                out = os.popen( cmd ).read().split( "\n" )

                for pid in out:
                    print os.popen( self.commands[ "PAUSE_PROCESS" ] + pid ).read()
                    self.paused_pid_list.append( pid )


    def resume_processes( self ):
        
        for pid in self.paused_pid_list:

            os.system( self.commands[ "RESUME_PROCESS" ] + pid )
        
        self.paused_pid_list = []


if __name__ == "__main__":

    
    pc = ProcessControl()

    '''
    pc.pause_processes()
    import time
    time.sleep( 3 )
    pc.resume_processes()
    '''

    if len( sys.argv ) > 1:

        if sys.argv[1] == "-l":
            
            pc.get_process_list()

            out = open( "../UI/process_list.dat", "w" )
            out.write( "\n".join( pc.process_list ) )


