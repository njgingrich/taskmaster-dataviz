function makeplot() {
  Plotly.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv", function(data){ processData(data) } );
  // I didn't take the time to get a local file working with chrome permission
  // Plotly.d3.csv('Episode 1: Melon buffet. (28 July 2015).csv', function(data){ processData(data) } );
};

function processData(allRows) {

  console.log(allRows);
  var x = [], y = []

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['AAPL_x'] );
    y.push( row['AAPL_y'] );
  }
  console.log( 'X',x, 'Y',y);
  makePlotly( x, y );
}

function makePlotly( x, y ){
  var plotDiv = document.getElementById("plot");
  var traces = [{
    x: x,
    y: y
  }];

  Plotly.newPlot('myDiv', traces,
    {title: 'Plotting CSV data from AJAX call'});
};
  makeplot();