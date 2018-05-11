
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

                if( data["track_keyboard"] == true )
                    $('#keyboard').trigger('click');

                if( data["track_mouse"] == true )
                    $('#mouse').trigger('click');
            }
        }
    }
    rawFile.send(null);
}

window.onload = function()
{
    var settings_filename = "data/settings.json";
    read( settings_filename );


    var file = new File( "tes.dat" );
    file.write( "test" );
    file.close();
}