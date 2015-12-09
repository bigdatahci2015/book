# Warmup

Complete this warmup exercise to get an idea how to put all the different pieces
together to generate an end-to-end data analysis viz report.

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}

var groups = _.groupBy(data, function(d){
    return d['CrsPBAColl']
})

// TODO: add real code to convert groups (which is an object) into an array like below
var countsJson=_.mapValues(groups, function(group){
    return _.size(group)
})
var keys=_.keys(countsJson)
var counts=_.map(keys, function(key){
    return {"name": key, "count": countsJson[key]}
})
// This array should have a lot more elements.
/*var counts = [{"name": "AS","count": 3237},
    {"name": "BU","count": 378},
    {"name": "EB","count": 139},
    {"name": "EN","count": 573}]*/

console.log(counts)

// TODO: modify the code below to produce a nice vertical bar charts

function computeX(d, i) {
    return 50*i
}

function computeHeight(d, i) {
    return d['count']/10
}

function computeWidth(d, i) {
    return 20 
}

function computeY(d, i) {
    return 400-d['count']/10
}

function computeColor(d, i) {
    return 'red'
}



var viz = _.map(counts, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i),
                label: d
            }
         })
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<rect x="${d.x}"
      y="${d.y}"
      height="${d.height}"
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />
<text x="${d.x}" y="${d.y}">${d.label.name}</text>
<text x="${d.x}" y="${d.y-10}">${d.label.count}</text>

{% endviz %}
