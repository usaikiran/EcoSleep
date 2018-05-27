
var ipcRenderer = require('electron').ipcRenderer;

function get_pause_html( title )
{
    return "<tr id='pause-"+title+"'>\
    <td><i name='pause-checkbox' id="+title+" class='material-icons delete'>&#xe892;</i></td>\
    <td class='caps-text'>"+ title +"</td>\
    </tr>";
}

Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};

var out = ipcRenderer.sendSync('get-process-list', 'test').split( ':' );
var process_list, pause_list;

process_list = out[0].split( "\n" );
pause_list = out[1].split( "\n" );

pause_list.remove( "" );

console.log( process_list + " , " + pause_list );
htmlContent = ""

for( var i=0; i<pause_list.length; i++ )
{
    console.log( "hello" );

    htmlContent += get_pause_html( pause_list[i].toUpperCase() );
}

$( "#table-paused-process" ).html( htmlContent );

htmlContent = ""

for( var i=0; i<process_list.length-1; i++ )
{
    tag = "";
    if( pause_list.indexOf( process_list[i].toLowerCase() ) != -1 )
    {
        tag = "checked"
    }

    htmlContent += '<tr id='+i+'> \
        <td> \
            <label class="container"><span class="elipsis">'+process_list[i].toUpperCase()+'</span>\
                <input id="checkbox-process-'+i+'" class="process-checkbox" name="'+process_list[i].toUpperCase()+'" type="checkbox" '+tag+'> \
                <span class="checkmark" id="checkmark-"'+i+'"></span> \
            </label> \
        </td> \
    </tr>';
}

$( "#table-running-process" ).html( htmlContent );

$('.process-checkbox').change(
    function(){
        if ($(this).is(':checked')) {
            $( "#table-paused-process" ).html( $( "#table-paused-process" ).html()+get_pause_html( $(this).attr( "name" ) ) );
            pause_list.push( $(this).attr( "name" ).toLowerCase() );
        }
        else
        {
            $( "#pause-"+$(this).attr( "name" ) ).remove();    
            pause_list.remove( $(this).attr( "name" ).toLowerCase() );
        }

        console.log( ipcRenderer.sendSync('set-process-list', pause_list) );
    });

$('button[name=pause-checkbox]').click(
    /*function(){
        $( "#pause-"+$(this).attr( "id" ) ).remove();   
    }*/
);