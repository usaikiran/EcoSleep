
var prev_active_icon = 0;
var iframe_src = [ "dashboard.html", "webcam.html", "settings.html", "processes.html", "stats.html" ]

window.onload = function()
{
    $('[data-toggle="tooltip"]').tooltip()
    onNavIconClick( 3 )
}

function onNavIconClick( id )
{
    $( "#"+prev_active_icon ).removeClass( "active" );
    $( "#"+id ).addClass( "active" );

    prev_active_icon = id;

    $( "#content-div" ).attr( "src", iframe_src[id] );
}