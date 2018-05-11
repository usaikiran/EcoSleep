
//const ipcRenderer = require('electron').ipcRenderer;

console.log("hello");

window.onload = function()
{
    require(['electron'], function (foo) {
        
        //const ipcRenderer = foo.ipcRenderer;
        //console.log( "test : " + ipcRenderer.sendSync('get-process-list', '') );

    });
}
