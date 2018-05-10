
var electron = require('electron')
var app = electron.app
var BrowserWindow = electron.BrowserWindow
var http = require('http')
var net = require('net')

var exec = require('child_process').execSync;

var mainWindow = null;

app.on('ready', function() {
    mainWindow = new BrowserWindow({
        height: 600,
        width: 850
    });

    mainWindow.loadURL('file://' + __dirname + '/index.html');

    console.log( exec( "ls -l" ).toString() );
});

