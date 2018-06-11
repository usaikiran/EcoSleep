
var ipcRenderer = require('electron').ipcRenderer;

var prev_active_icon = 0, active_frame=0;
var iframe_src = [ "dashboard.html", "settings.html", "processes.html", "stats.html" ]

var state = 0;
var msg = [ "ACTIVATE", "DISABLE" ];

function toggle()
{
    state = (state+1)%2;
    $( "#toggle-state" ).text( msg[state] )

    console.log( ipcRenderer.sendSync('toggle-action', ''+state) );
}

function onNavIconClick( id )
{
    $( "#"+prev_active_icon ).removeClass( "active" );
    $( "#"+id ).addClass( "active" );

    prev_active_icon = id;
    active_frame = id;

    $( "#content-div" ).empty();
    $( "#content-div" ).load( iframe_src[id] );
}

window.onload = function()
{
    onNavIconClick( 2 );
    $('[data-toggle="tooltip"]').tooltip();
    
    /*out = ipcRenderer.sendSync('brightness', 'get');
    if( out > 0 )
        state = 0;
    else
        state = 1;

    toogle();*/
}