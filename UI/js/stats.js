
var ctx = $("#chart");
var presets = window.chartColors;

var seconds = 0;
var xAxisLen = 20;

var chartLabels = [];
var chartValues = [];

var esChartLabels = [];
var esChartValues = [10, 20, 10];

var chartState = true;
var chartPaused = true;

var avg_power_consumed = 0;
var total_readings = 0;

var avg_power_conserved = 0;
var total_es_readings = 0;

Chart.plugins.register({
    beforeDraw: function(chart) {
       var ctx = chart.chart.ctx,
           x_axis = chart.scales['x-axis-0'],
           topY = chart.scales['y-axis-0'].top,
           bottomY = chart.scales['y-axis-0'].bottom;
       x_axis.options.gridLines.display = false;
       x_axis.ticks.forEach(function(label, index) {
          if (index === 0) return;
          var x = x_axis.getPixelForValue(label);
          ctx.save();
          ctx.beginPath();
          ctx.strokeStyle = x_axis.options.gridLines.color;
          ctx.moveTo(x, topY);
          ctx.lineTo(x, bottomY);
          ctx.stroke();
          ctx.restore();
       });
    }
 });


var chart = new Chart( ctx, {

    type: 'line',
    data: {
        labels: chartLabels,
        datasets: [{
            data: chartValues,
            backgroundColor: 'rgba(33, 150, 243, 0.7)',
            label: 'Power Consumed',
            fill: 'start'
        }]
    },
    options: {
        tooltips: {
            callbacks: {
                title: function(tooltipItem, data) {
                    return "Elapsed time : "+data['labels'][tooltipItem[0]['index']]+" sec";
                },
                label: function(tooltipItem, data) {
                    return "Consuming "+data['datasets'][0]['data'][tooltipItem['index']]+" watts";
                }
            },
            backgroundColor: 'rgba( 255, 255, 255, 0.7 )',

            titleFontSize: 12,
            titleFontColor: '#000',
            titleFontFamily: "monaco",
            titleFontWeight: "normal",

            bodyFontColor: '#000',
            bodyFontFamily: "monaco",
            bodyFontSize: 12,
            displayColors: false
        },
        legend: {
            labels: {
                // This more specific font property overrides the global property
                fontColor: 'white',
                fontFamily: 'monaco',
                fontWeight: 'bold',
                letterSpacing: '1px'
            },

            display: false
        },

        maintainAspectRatio: false,
        spanGaps: false,
        elements: {
            line: {
                tension: 0.4
            }
        },
        plugins: {
            filler: {
                propagate: false
            }
        },
        scales: {
            xAxes: [{
                ticks: {
                    display: false,
                    autoSkip: false,
                    maxRotation: 0,
                    fontColor: "#fff",
                    fontFamily: 'monaco'
                },
                gridLines: {
                    display: true,
                    color: "#333"
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Time (seconds)',
                    fontColor: "#fff",
                    fontFamily: "monaco"
                }
            }],
            yAxes: [{

                ticks: {
                    min: 0,
                    suggestedMax: 30,
                    stepSize: 5,
                    fontColor: "#fff",
                    fontFamily: 'monaco'
                },
                gridLines: {
                    display: true,
                    beginAtZero: true,
                    color: "#333"
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Energy (Joules)',
                    fontColor: "#fff",
                    fontFamily: "monaco"
                },
                afterFit: function(scale) {
                   scale.width = 65
                }
            }]

        }
    }
});

function genArray( start, len ){
    var arr = [];
    console.log( "start : "+start+" len : "+len );
    for( var i=start; i<start+len; i++ )
        arr.push( i );
    return arr;
}

function fillArray(value, len) {
    var arr = [];
    for (var i = 0; i < len; i++) {
      arr.push(value);
    }
    return arr;
}

function toggleChartState()
{
    chartState = !chartState;
}

function updateChart()
{
    
    var val = ipcRenderer.sendSync('get-stats', 1).split(":");
    var out = parseFloat( val[0] );
    var state = parseInt( val[1] );
    var tempLables=[], tempValues=[]

    //console.log( out+" : "+state );
    if( true || out != null )
    {
        chartLabels.push( ++seconds );
        chartValues.push( out );
    }
    
    if( chartValues.length > xAxisLen )
    {
        chartLabels.shift();
        chartValues.shift();

        tempValues = chartValues;
        tempLables = chartLabels;
    }
    else
    {
        len = chartValues.length;
        tempValues = chartValues.concat( fillArray( NaN, xAxisLen-len ) );
        tempLables = chartLabels.concat( genArray( len, xAxisLen-len ) );
    }

    if( active_frame==4 && chartPaused==false )
        setTimeout( updateChart, 1000 )
    
    //console.log( tempValues, tempLables );

    chart.data.datasets[0].data = tempValues;
    chart.data.labels = tempLables;

    if( out != NaN )
    {
        chart.update();

        avg_power_consumed = ( avg_power_consumed*total_readings + out )/( total_readings+1 )

        if( state==0 )
        {
            avg_power_conserved = ( avg_power_conserved*total_es_readings + (avg_power_consumed-out) )/( total_es_readings+1 )
            total_es_readings +=1;
        }
        
        $( "#power-consumed" ).html( avg_power_consumed.toFixed(2) );
        $( "#power-conserved" ).html( avg_power_conserved.toFixed(2) );

        console.log( "parameters : "+avg_power_consumed+" "+avg_power_conserved +" out : "+out+" diff"+avg_power_consumed-out);
        total_readings += 1;
    }

    //console.log( chartLabels );
}

function resetChart()
{
    seconds = 0;
    chartLabels = [];
    chartValues = [];

    chart.data.datasets[0].data = chartLabels;
    chart.data.labels = chartLabels;
    chart.update();

    /*if( chartPaused == true )
    {
        chartPaused = false;
        setTimeout( updateChart, 1000);
    }*/
}

function flow_control()
{
    chartPaused = !chartPaused;

    if( chartPaused == false )
    {
        $( "#control-icon" ).html( "stop" );
        setTimeout( updateChart, 1000);
    }
    else
        $( "#control-icon" ).html( "play_arrow" );
}
