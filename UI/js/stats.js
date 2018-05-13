
var ctx = $("#chart");
var presets = window.chartColors;

var seconds = 0;

var chartLabels = [];
var chartValues = [];

var esChartLabels = [];
var esChartValues = [10, 20, 10];

var chartState = true;
var chartPaused = true;

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
                    labelString: 'Time ( seconds )',
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
                    labelString: 'Joules',
                    fontColor: "#fff",
                    fontFamily: "monaco"
                },
                afterFit: function(scale) {
                   scale.width = 65
                }
            }]

        },
        annotation: {
            annotations: [
              {
                type: "line",
                mode: "vertical",
                scaleID: "x-axis-0",
                value: 2,
                borderColor: "red",
                label: {
                  content: "TODAY",
                  enabled: true,
                  position: "top"
                }
              }
            ]
          }
    }
});

function toggleChartState()
{
    chartState = !chartState;
}

function updateChart()
{
    
    var out = ipcRenderer.sendSync('get-stats', 1);

    console.log( out );
    if( true || out != null )
    {
        chartLabels.push( ++seconds );
        chartValues.push( out );
    }
    
    if( chartValues.length > 20 )
    {
        chartLabels.shift();
        chartValues.shift();
    }

    if( active_frame==4 && chartPaused==false )
        setTimeout( updateChart, 1000 )
    
    chart.data.datasets[0].data = chartValues;
    chart.data.labels = chartLabels;

    if( out != null )
        chart.update();

    console.log( chartLabels );
}

function resetChart()
{
    seconds = 0;
    chartLabels = [];
    chartValues = [];

    if( chartPaused == true )
    {
        chartPaused = false;
        setTimeout( updateChart, 1000);
    }
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