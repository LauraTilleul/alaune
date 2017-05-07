# -*- coding:utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

def simple_form():
        page_content = ''
        page_content+='<!DOCTYPE html> <html lang="fr"> <head> <meta charset="utf-8" /><title>Unes </title> '
        page_content+= '<link href="static/styles/style1.css" rel="stylesheet" type="text/css" media="all"/>'
        page_content+='<h1> A la Une Aujourd\'hui </h1><nav> <ul class=\"menu\">'
        page_content+='<li class=\"menuitem\"> <a href=\"/unes"> Unes </a> </li>'
        page_content+='<li class=\"menuitem\"> <a href=\"/StreamGraph"> StreamGraph </a> </li> <br/> </ul> <br/> </nav> </head><body>'
        return page_content



def htmlize2(titles_and_href):
	html = ''
	for item in titles_and_href:
		html += '<h2>'
		html += '<a href="' + item[1] + '">' + item[0].strip() + '</a></h2>\n'
        return html


def htmlUnes():
        page_content = ''
        page_content +='<!DOCTYPE html> <html lang="fr"> <head> <meta charset="utf-8" /><title>Unes </title> '
        page_content += '<link href="static/styles/style1.css" rel="stylesheet" type="text/css" media="all"/>'
        page_content +='<h1> A la Une Aujourd\'hui </h1><nav> <ul class=\"menu\">'
        page_content +='<li class=\"menuitem\">  Unes </li>'
        page_content +='<li class=\"menuitem\"> <a href=\"/StreamGraph"> StreamGraph </a> </li> <br/> </ul> <br/> </nav> </head><body>'
        page_content += '<fieldset> <legend> '
        page_content += '<h2>Choisissez votre journal:</h2> </legend>'
        page_content += '<form action="/quel_journal" method="post">'
        page_content += '<select name="journal">'
        page_content += '<option value="lemonde">LeMonde</option>'
        page_content += '<option value="figaro">Le Figaro</option>'
        page_content += '<option value="lejournaldunet">Le Journal du Net</option>'
        page_content += '<option value="lepoint">Le Point</option>'
        page_content += '<option value="courrier">Courrier International</option>'
        page_content += '<option value="lesechos">Les Echos</option>'
        page_content += '<option value="latribune">La Tribune</option>'
        page_content += '<option value="ledauphine"> Le Dauphiné Libéré </option>'
        page_content += '<option value="ouestfrance">Ouest France</option>'
        page_content += '<option value="sudouest"> Le Sud Ouest </option>'
        page_content += '<option value="leparisien">Le Parisien</option>'
        page_content += '<option value="20min">20 minutes</option>'
        page_content += '</select>'
        page_content += '<input type="submit" value="Envoyer"></input>'
        page_content += '</form>'
        page_content += '</fieldset>'
        return page_content

def htmlQuelJournal(unes,journal):
        page_content = ''
        page_content+='<!DOCTYPE html> <html lang="fr"> <head> <meta charset="utf-8" /><title>Unes </title> '
        page_content+= '<link href="static/styles/style.css" rel="stylesheet" type="text/css" media="all"/>'
        page_content+='<h1> A la Une Aujourd\'hui </h1><nav> <ul class=\"menu\">'
        page_content+='<li class=\"menuitem\"> <a href=\"/unes">  Unes </a> </li>'
        page_content+='<li class=\"menuitem\"> <a href=\"/StreamGraph"> StreamGraph </a> </li> <br/> </ul> <br/> </nav> </head><body>'
        page_content+='<h3> A la une de <em>' + rewrite(journal) + '</em></h3>'
        page_content+= htmlize2(unes)
        return page_content

#permet d'obtenir le nom du journal au propre ( lemonde => Le Monde )
def rewrite(journal):
        dico={}
        dico['lemonde']= 'Le Monde'
        dico['lejournaldunet']='Le Journal du Net'
        dico['figaro']='Le Figaro'
        dico['lepoint']='Le Point'
        dico['courrier']='Courrier International'
        dico['lesechos']= 'Les échos'
        dico['latribune']='La Tribune'
        dico['ledauphine']='Le Dauphiné Libéré'
        dico['ouestfrance']='Ouest France'
        dico['sudouest']= 'Sud Ouest'
        dico['leparisien']='Le Parisien'
        dico['20min']= '20 Minutes'
        return dico[journal]

# HTML STREAMGRAPH
def htmlStreamGraph():
        page_content='<!DOCTYPE html> <html lang="fr"> <head> <meta charset="utf-8" /><title>Unes </title> '
        page_content+= '<link href="static/styles/style.css" rel="stylesheet" type="text/css" media="all"/>'
        page_content+='<h1> A la Une Aujourd\'hui </h1><nav> <ul class=\"menu\">'
        page_content+='<li class=\"menuitem\"> <a href=\"/unes">  Unes </a> </li>'
        page_content+='<li class=\"menuitem\"> StreamGraph  </li> <br/> </ul> <br/> </nav> </head><body>'    
        page_content+= """<!DOCTYPE html>

                        <meta charset="utf-8">
                        <link href="static/styles/style.css" rel="stylesheet" type="text/css" media="all"/>
                        <style>

                        body {
                          font: 10px courier
                          text-color: blue;
                        }

                        .chart { 
                          background: #dee7e8;
                          
                        }

                        p {
                          color:#06052d;
                          font: 18px helvetica;
                        }


                        .axis path, .axis line {
                          fill: none;
                          stroke: #06052d;
                          stroke-width: 2px;
                          shape-rendering: crisperEdges;
                        }

                        button {
                          position: absolute;
                          right: 50px;
                          top: 10px;
                        }

                        </style>
                        <body>
                        <h3> Les candidats à la présidentielle </h3>
                        <p style="color:gray;"> Cliquez sur le graphe pour accéder aux unes du candidat sélectionné!</p>
                        <script src="http://d3js.org/d3.v2.js"></script>


                        <div class="chart">
                        </div>

                        <script>

                        chart("static/politiques.csv", "blue");

                        var datearray = [];
                        var colorrange = [];


                        function chart(csvpath, color) {

                        if (color == "blue") {
                          colorrange = ["#045A8D", "#2B8CBE", "#74A9CF", "#A6BDDB", "#D0D1E6", "#F1EEF6"];
                        }
                        else if (color == "pink") {
                          colorrange = ["#980043", "#DD1C77", "#DF65B0", "#C994C7", "#D4B9DA", "#F1EEF6"];
                        }
                        else if (color == "orange") {
                          colorrange = ["#B30000", "#E34A33", "#FC8D59", "#FDBB84", "#FDD49E", "#FEF0D9"];
                        }
                        strokecolor = colorrange[0];

                        var format = d3.time.format("%Y-%m-%d");

                        var margin = {top: 20, right: 50, bottom: 30, left: 50};
                        var width = 1200 - margin.left - margin.right;
                        var height = 400 - margin.top - margin.bottom;

                        var tooltip = d3.select("body")
                            .append("div")
                            .attr("class", "remove")
                            .style("position", "absolute")
                            .style("z-index", "20")
                            .style("visibility", "hidden")
                            .style("top", "260px")
                            .style("left", "148px");

                        var x = d3.time.scale()
                            .range([0, width]);

                        var y = d3.scale.linear()
                            .range([height-10, 0]);

                        var z = d3.scale.ordinal()
                            .range(colorrange);

                        var xAxis = d3.svg.axis()
                            .scale(x)
                            .orient("bottom")
                            .ticks(d3.time.weeks);

                        var yAxis = d3.svg.axis()
                            .scale(y);
                            

                        var yAxisr = d3.svg.axis()
                            .scale(y);

                        var stack = d3.layout.stack()
                            .offset("silhouette")
                            .values(function(d) { return d.values; })
                            .x(function(d) { return d.date; })
                            .y(function(d) { return d.value; });

                        var nest = d3.nest()
                            .key(function(d) { return d.key; });

                        var area = d3.svg.area()
                            .interpolate("cardinal")
                            .x(function(d) { return x(d.date); })
                            .y0(function(d) { return y(d.y0); })
                            .y1(function(d) { return y(d.y0 + d.y); });

                        var svg = d3.select(".chart").append("svg")
                            .style('fill', '#0D1A66')
                            .attr("width", width + margin.left + margin.right)
                            .attr("height",20+ height + margin.top + margin.bottom)
                          .append("g")
                            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

                        var graph = d3.csv(csvpath, function(data) {
                          data.forEach(function(d) {
                            d.date = format.parse(d.date);
                            d.value = +d.value;
                          });

                          var layers = stack(nest.entries(data));

                          x.domain(d3.extent(data, function(d) { return d.date; }));
                          y.domain([0, d3.max(data, function(d) { return d.y0 + d.y; })]);

                          svg.selectAll(".layer")
                              .data(layers)
                            .enter().append("path")
                              .attr("class", "layer")
                              .attr("d", function(d) { return area(d.values); })
                              .style("fill", function(d, i) { return z(i); });


                          svg.append("g")
                              .attr("class", "x axis")
                              .attr("transform", "translate(0," + height + ")")
                              .call(xAxis);

                          svg.append("g")
                              .attr("class", "y axis")
                              .attr("transform", "translate(" + width + ", 0)")
                              .call(yAxis.orient("right"));

                          svg.append("g")
                              .attr("class", "y axis")
                              .call(yAxis.orient("left"));

                          svg.selectAll(".layer")
                            .attr("opacity", 1)
                            .on("mouseover", function(d, i) {
                              svg.selectAll(".layer").transition()
                              .duration(250)
                              .attr("opacity", function(d, j) {
                                return j != i ? 0.6 : 1;
                            })})

                            .on("mousemove", function(d, i) {
                              mousex = d3.mouse(this);
                              mousex = mousex[0];
                              var invertedx = x.invert(mousex);
                              invertedx = invertedx.getDay() + invertedx.getDate();
                              var selected = (d.values);
                              for (var k = 0; k < selected.length; k++) {
                                datearray[k] = selected[k].date
                                datearray[k] = datearray[k].getDay() + datearray[k].getDate();
                              }

                              mousedate = datearray.indexOf(invertedx);
                              pro = d.values[mousedate].value;

                              d3.select(this)
                              .classed("hover", true)
                              .attr("stroke", strokecolor)
                              .attr("stroke-width", "0.5px"), 
                              tooltip.html( "<p>" + d.key + "<br>" + pro + "</p>" ).style("visibility", "visible");
                              
                            })
                            
                            .on("click", function (d,i){
                            window.location.href="/candidat?name="+ d.key +'&date=00';
                        })
                            
                            
                            .on("mouseout", function(d, i) {
                             svg.selectAll(".layer")
                              .transition()
                              .duration(250)
                              .attr("opacity", "1");
                              d3.select(this)
                              .classed("hover", false)
                              .attr("stroke-width", "0px"), tooltip.html( "<p>" + d.key + "<br>" + pro + "</p>" ).style("visibility", "hidden");
                          })
                          
                            
                          var vertical = d3.select(".chart")
                                .append("div")
                                .attr("class", "remove")
                                .style("position", "absolute")
                                .style("z-index", "19")
                                .style("width", "1px")
                                .style("height", "380px")
                                .style("top", "260px")
                                .style("bottom", "30px")
                                .style("left", "0px")
                                .style("background", "#ffff");

                          d3.select(".chart")
                              .on("mousemove", function(){  
                                 mousex = d3.mouse(this);
                                 mousex = mousex[0] + 5;
                                 vertical.style("left", mousex + "px" )})
                              .on("mouseover", function(){  
                                 mousex = d3.mouse(this);
                                 mousex = mousex[0] + 5;
                                 vertical.style("left", mousex + "px")});
                         
                                
                        });
                        }

                        </script>"""
        return page_content

def htmlCandidat(name):
        page_content = ''
        page_content+='<!DOCTYPE html> <html lang="fr"> <head> <meta charset="utf-8" /><title>Unes</title> '
        page_content+= '<link href="static/styles/style.css" rel="stylesheet" type="text/css" media="all"/>'
        page_content+='<nav> <ul class=\"menu\">'
        page_content+='<li id=00 class=\"menuitem\"> <a href=\"/unes">  Unes </a></li>'
        page_content+='<li class=\"menuitem\"> <a href=\"/StreamGraph"> StreamGraph </a> </li> <br/> </ul> <br/> </nav> </head><body>'
        page_content+='<h3> Toutes les unes sur ' + name.capitalize() +'</h3>'
        page_content+='<p style="color:gray;"> Cliquez sur une barre pour acceder aux unes du jour choisi!</p>'
        return page_content

def htmlBarchart(name):
    return """<!DOCTYPE html>
<style>

.bar {
  fill: steelblue;
}

.bar:hover {
  fill: cadetblue;
}
.axis path, .axis line {
                  fill: none;
                  stroke: #06052D;
                  stroke-width: 2px;
                  shape-rendering: crisperEdges;
                }
.axis--x path {
  display: none;
}
text{fill:#06052D; font-size:10px;}

</style>
<svg width="1250" height="500"></svg>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script>

var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("static/barchart_"""+name+""".csv", function(d) {
  d.frequency = +d.frequency;
  return d;
}, function(error, data) {
  if (error) throw error;

  x.domain(data.map(function(d) { return d.letter; }));
  y.domain([0, d3.max(data, function(d) { return d.frequency; })]);
  
  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y).ticks(10, "%"))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Frequency");
      
  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.letter); })
      .attr("y", function(d) { return y(d.frequency); })
      .attr("width", x.bandwidth())
      .attr("height", function(d) { return height - y(d.frequency); })
      .on("click", function(d){window.location.href='?name="""+name+"""&date=' + d.letter+'#unes';});
  
});
    

</script>"""

