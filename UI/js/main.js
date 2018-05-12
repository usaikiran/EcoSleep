
const ipcRenderer = require('electron').ipcRenderer;

var prev_active_icon = 0;
var iframe_src = [ "dashboard.html", "webcam.html", "settings.html", "processes.html", "stats.html" ]

var state = 0;
var msg = [ "ON", "OFF" ];

function toggle()
{
    state = (state+1)%2;
    $( "#toggle-state" ).text( msg[state] )

    console.log( ipcRenderer.sendSync('toggle-action', ''+state) );

}

window.onload = function()
{
    $('[data-toggle="tooltip"]').tooltip()
    onNavIconClick( 3 );
    
    
    //console.log( "test : " + ipcRenderer.sendSync('get-process-list', '') );
}

function onNavIconClick( id )
{
    $( "#"+prev_active_icon ).removeClass( "active" );
    $( "#"+id ).addClass( "active" );

    prev_active_icon = id;

    $( "#content-div" ).load( iframe_src[id] );
}