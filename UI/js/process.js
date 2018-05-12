
var out = ipcRenderer.sendSync('get-process-list', 'test').split( ':' );
var process_list, pause_list;

process_list = out[0].split( "\n" );
pause_list = out[1].split( "\n" );

console.log( process_list + " , " + pause_list );
htmlContent = ""

for( var i=0; i<pause_list.length-1; i++ )
{
    console.log( "hello" );

    htmlContent += "<tr id='"+i+"'>\
        <td><button class='material-icons delete'>&#xe909;</button></td>\
        <td class='caps-text'>"+ pause_list[i].toUpperCase() +"</td>\
        </tr>";
}

$( "#table-paused-process" ).html( htmlContent );

htmlContent = ""

for( var i=0; i<process_list.length-1; i++ )
{
    htmlContent += '<tr id='+i+'> \
        <td> \
            <label class="container"><span class="elipsis">'+process_list[i].toUpperCase()+'</span>\
                <input id="checkbox-process-'+i+'" type="checkbox" checked="checked" > \
                <span class="checkmark" id="checkmark-"'+i+'"></span> \
            </label> \
        </td> \
    </tr>';

    if( pause_list.indexOf( process_list[i].toLowerCase() ) == -1 )
    {
        console.log( "-> "+process_list[i] );
        $("#checkbox-process-"+i ).removeAttr('checked'); ;
    }
}

$( "#table-running-process" ).html( htmlContent );
