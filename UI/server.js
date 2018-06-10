
var electron = require('electron')
var app = electron.app
var BrowserWindow = electron.BrowserWindow
var http = require('http')
var net = require('net')
const ipc = require('electron-ipc')
var sleep = require('system-sleep')

var fs = require('fs');
    
var exec = require('child_process').exec;
var mainWindow = null;

const ipcMain = require('electron').ipcMain;

ipcMain.on('get-stats', function(event, arg) {

    console.log( "\n@ipc-get-stats  args=[ "+arg+" ]" );

    exec( "cd ../Backend/ && python power_stat.py", function(error, stdout, stderr){ 
        
        watts = parseFloat( stdout ); 
        exec( "cd ../Backend/ && python brightness.py", function(error, stdout, stderr){ 
            
            state = parseFloat( stdout ); 
            console.log( "interval : "+arg+" energy consumed : "+watts+" brightness : "+stdout );
            event.returnValue = watts+":"+state;
        });
    });

});

ipcMain.on('get-process-list', function(event, arg) {
    
    console.log( "\n@ipc-get-process-list args=[ "+arg+" ]" );

    process_list = ""
    pause_list = ""

    exec( "cd ../Backend/ && python process_control.py -l", function(error, stdout, stderr){ 
        process_list = stdout; 
        console.log( stdout, error );

        exec( "cd ../Backend/ && python process_control.py -p", function(error, stdout, stderr){ 
            pause_list = stdout; 

            res = process_list + " :" + pause_list;
            console.log( res );
            event.returnValue = res;
            });
    });

});

ipcMain.on('set-process-list', function(event, arg) {
    
    console.log( "\n@ipc-set-process-list args=[ "+arg+" ]" );

    data = { "PAUSE_PROCESS_LIST" : arg }
    data = JSON.stringify( data );

    fs.writeFile("../Backend/config.json", data, function(err) {
        if(err) {
            event.returnValue = "error";
        }
        else{
            console.log("data : "+data);
            event.returnValue = "success";
        }
    });

});

ipcMain.on('brightness', function(event, arg) {

    console.log( "\n@ipc-brightness args=[ "+arg+" ]" );

    if( arg=="get" )
    {
        exec( "cd ../Backend/ && python brightness.py", function(error, stdout, stderr){     
            event.returnValue = stdout;
        });
    }
    else
    {
        exec( "cd ../Backend/ && python brightness.py -s "+arg, function(error, stdout, stderr){ 
            event.returnValue = "set";
        });
    } 

});

ipcMain.on('save-settings', function(event, arg) {

    console.log( "\n@ipc-save-settings args=[ "+arg+" ]" );

    data = JSON.stringify( arg );

    fs.writeFile("data/settings.json", data, function(err) {
        if(err) {
            event.returnValue = "error";
        }
        else{
            console.log("data : "+data);
            event.returnValue = "success";
        }
    }); 

});

ipcMain.on('toggle-action', function(event, arg) {
    console.log( "\n@ipc-toggle-action args=[ "+arg+" ]" );

    if( arg=="1" )
        cmd = "./start &"
    else
        cmd = "./kill"

    exec( cmd, function(error, stdout, stderr){ 

        console.log( "stdout : "+stdout+" \nstderr : "+stderr );
        event.returnValue = stdout;
    });
  
    event.returnValue = "NA";

});

app.on('ready', function() {
    mainWindow = new BrowserWindow({
        height: 600,
        width: 850
    });

    mainWindow.loadURL('file://' + __dirname + '/index.html');

});
