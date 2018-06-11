
var ipcRenderer = require('electron').ipcRenderer;

window.onload = function()
{
    $('[data-toggle="tooltip"]').tooltip();
    onNavIconClick( 1 );
}