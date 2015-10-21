# Report


Use only Javascript and SVG to produce a data analysis / visualization report.
{% data src="../fcq/fcq.clean.json" %}{% enddata %}
# Authors
This report is prepared by
* [Satchel Spencer](https://github.com/satchelspencer)
* [John Murphy](https://github.com/johnmurph27)
* [Nicole Woytarowicz](https://github.com/nicolele)
* [Tristan Wagar](https://github.com/twagar95)
* [Sushant Mittal](https://github.com/sumi6109)



* 1.How does bird size relate to the cost of the incident?
* 2.What month has the most bird strikes?
* 3.How much of the collected wildlife was sent to the Smithsonian?
* 4.What is distribution of number of hrs worked for each department?


<a name="top"/>
<div id="autonav"></div>
{% data src="../../learning/week5/birdstrike.json" %}{% enddata %}

{% viz %}

{% title %}

How does bird size relate to the cost of the incident?

{% solution %}

var sizeCosts = _(data).map(function(incident){
    return {
        cost : parseInt(incident['Cost: Total $'].toString().replace(',', '')),
        size : incident['Wildlife: Size']
    }
}).filter(function(incident){
    return incident.cost && incident.size;
}).value();

var maxCost = _(sizeCosts).pluck('cost').max();
var sizes = ['Small', 'Medium', 'Large'];

var result = _.map(sizeCosts, function(sizeCost){
    return template({
        y : (sizes.indexOf(sizeCost.size)*20)+10,
        x : (sizeCost.cost*(620/maxCost))+80
    });
})

_.each(sizes, function(size, i){
   result.push("<text y='"+((i*20)+15)+"'>"+size+"</text>"); 
});

return result.join('\n\n');

{% template %}
<circle cx="${x}" cy="${y}" r="5" style="fill:rgba(0,0,0,0.5);"/>
{% endviz %}


{% viz %}

{% title %}

What month has the most bird strikes?
{% solution %}
var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November']
var dates = _.groupBy(data, function(item){
	 return item['FlightDate'].split('/')[0] })


console.log(dates)
var counts = _(dates).map(function(group, name){
    return {
        name : months[name-1]+ ' ' + group.length,
        count : group.length
    };
}).value();

var max = _(counts).pluck('count').max();
function computeWidth(d, i) {
    return d.count*(500/max);
}

var result = _.map(counts, function(count, i){
    return template({
        y : 25*i,
        width : count.count*(600/max),
        name : count.name
    });
})

return result.join('')


{% template %}

<rect y="${y}" height="20" width="${width}" style="fill:red;"/>
<text y="${y+15}" x="${width+10}">${name}</text>

{% endviz %}
# How much of the collected wildlife was sent to the Smithsonian?
{% viz %}

{% title %}

How much of the collected wildlife was sent to the Smithsonian?

{% solution %}
var collected = _.filter(data, function(d){
    return d["Remains of wildlife collected?"] == "TRUE"
})

var smiths = _.groupBy(collected, function(d) {
    return d["Remains of wildlife sent to Smithsonian"]
});

// TODO: modify the code below to produce a nice vertical bar charts

function computeX(d, i) {
return 0
}

function computeHeightCollected(d, i) {
return _.size(collected)
}

function computeHeight(d, i) {
return _.size(smiths)*2
}

function computeY(d, i) {
return 0
}

function computeColor(d, i) {
return 'red'
}

function computeSentColor(d, i) {
return 'blue'
}

var viz = _.map(smiths, function(d, i){
return {
    x: computeX(d, i),
    y: computeY(d, i),
    height: computeHeight(d, i),
    collectedColor: computeColor(d, i),
    collectedHeight: computeHeightCollected(d, i),
    sentColor: computeSentColor(d, i)
}
})
console.log(viz)

var result = _.map(viz, function(d){
    return template({d: d})
})
return result.join('\n')

{% template %}

<rect
    x="0"
    width="20"
    height="${d.collectedHeight}"
    style="fill:${d.collectedColor};
    stroke-width:1;
    stroke:rgb(0,0,0)" />

<rect
    x="0"
    width="20"
    height="${d.height}"
    style="fill:${d.sentColor};
    stroke-width:1;
    stroke:rgb(0,0,0)" />

{% endviz %}

{% data src="../fcq/fcq.clean.json" %}{% enddata %}
#What is distribution of Number of Hrs worked for each department ?

{% viz %}

{% title %}


{% solution %}

var grps= _.groupBy(data,'CrsPBADept')

 var values =_.mapValues(grps,function(d){
 hrs= _.pluck(d,'Workload')
 
  var hrs_string=_.map(hrs,function(d){return d.Hrs_Wk})
  var total_hrs=_.map(hrs_string,function(d){ return d.split('-')[1]})
  return _.sum(total_hrs)
 })
 var values =_.pick(values,function(d){return d>0})
 console.log(values)
var data1=_.map(values,function(group,name){return { course_name:name ,hrswork:group}})
var max= _.max(_.pluck(data1,'hrswork'))
//console.log(data1)


function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
      return 20
}

function computeY(d, i) {
    return 20*i
}
function computeWidth(d, i) {
      return d.hrswork/4
}
function computeColor(d, i) {
    return 'red'
}
function computeName(d, i) {
    return d.course_name
}

var viz = _.map(data1, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                color: computeColor(d, i),
                width: computeWidth(d,i),
                name:computeName(d,i)
            }
         })
console.log(data1)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')



{% template %}

<g transform="translate(0 ${d.y})">
    <rect         
         width="${d.width}"
         height="20"
         style="fill:${d.color};
                stroke-width:3;
                stroke:rgb(0,0,0)" />
                 <text transform="translate(0 15)">
        ${d.name}
    </text>
              <text transform="translate(80 15)">
        ${d.width*4}
    </text>
</g>
   
{% endviz %}



# (Question 2)

Use the warmup exercise as the template to produce an answer here.

# (Question 3)

Use the warmup exercise as the template to produce an answer here. Remove this
question if you work as a unit of two.
