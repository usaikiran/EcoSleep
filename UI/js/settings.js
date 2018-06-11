
var ipcRenderer = require('electron').ipcRenderer;

function read(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);

    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var text = rawFile.responseText;
                data =JSON.parse( text );

                $( "#wait-time" ).val( ""+data["wait_time"] );
                $( "#fps" ).val( ""+data["fps"] );
                $( "#scale" ).val( ""+data["scale"] );
                $( "#brightness-interval" ).val( ""+data["brightness_interval"] );

                if( data["track_keyboard"] == true )
                    $('#keyboard').trigger('click');

                if( data["track_mouse"] == true )
                    $('#mouse').trigger('click');

                if( data["auto_brightness"] == true )
                    $('#auto-brightness').trigger('click');
            }
        }
    }
    rawFile.send(null);
}

function save( restart )
{
    var settings = {
        "wait_time" : $( "#wait-time" ).val(),
        "fps" : $( "#fps" ).val(),
        "scale" : $( "#scale" ).val(),
        "brightness_interval" : $( "#brightness-interval" ).val(),
        "track_keyboard" : $( "#keyboard" ).is(":checked"),
        "track_mouse" : $( "#mouse" ).is(":checked"),
        "auto_brightness" : $( "#auto-brightness" ).is(":checked"),
        "brightness" : $( "#brightness" ).val()
    }

    var out = ipcRenderer.sendSync('save-settings', settings )

    if( restart == true )
    {
        if( state ==1 )
        {
            ipcRenderer.sendSync('toggle-action', '0');
            setTimeout(function(){ 
                ipcRenderer.sendSync('toggle-action', '1');
            }, 3000); 
        }
    }
}

function brightness( val )
{
    if( val == null )
    {
        var out = ipcRenderer.sendSync('brightness', 'get' )
        return out;
    }
    else
        var out = ipcRenderer.sendSync('brightness', val )
}

$('#brightness').on('input', function () {
    brightness( $('#brightness').val()/100 );
});

var settings_filename = "data/settings.json";
read( settings_filename );

var res = brightness()
console.log( "brightness : "+res );
$( "#brightness" ).attr( "value", ""+res*100 );