
window.onload = function()
{
    $('[data-toggle="tooltip"]').tooltip()

    onNavIconClick( 2 );
}

var state = 0;
var msg = [ "OFF", "ON" ];

function toggle()
{
    state = (state+1)%2;
    $( "#toggle-state" ).text( msg[state] )
}