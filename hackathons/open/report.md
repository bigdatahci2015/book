# Report

Use only Javascript and SVG to produce a data analysis / visualization report.

# Authors

This report is prepared by
* [Kari Santos](https://github.com/karisantos)
* [Zachary Lamb](https://github.com/ZachLamb)
* [Denis Kazakov](https://github.com/94kazakov)

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

GPA vs class type

{% solution %}
 // first I need to remove all entries that don't have an AVG_GRD (I have seen a couple!)
var graded = _.filter(data,function(d){
    return d.hasOwnProperty("AVG_GRD");
})
var groups = _.groupBy(graded, 'Activity_Type');
var gpa = _.map(groups, function(d,key){
    var avg = _.reduce(d, function(total,e){
        return total+e.AVG_GRD;
    },0)/_.size(d); 
    //var avg = 3;
    var obj = {}
    obj.type = key;
    obj.avg = avg;
    return obj;
})
console.log(gpa)


function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i,data) {
    var width = 400; // svg window width
    var max = _.max(data,function(d){
            return d.avg;
        });
    var scale = width / max.avg;
    return d.avg * scale;
    return 100
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}
function computeLabel(d){
    return d.type
}

function computeValLabel(d) {
    return _.round(d.avg,2)
}
function computeValLabelLoc(d,i,data) {
    var width = computeWidth(d,i,data);
    return width + 2;
}
var viz = _.map(gpa, function(d, i, data){

            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d,i,data),
                color: computeColor(d, i),
                label: computeLabel(d),
                valLabel : computeValLabel(d),
                valLabelLoc : computeValLabelLoc(d,i,data)
            }
         })


var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')
{% template %}
<g transform="translate(0 ${d.y})">
    <rect x="${d.x}"
         width="${d.width}"
         height="${d.height}"
         style="fill:${d.color};
                stroke-width:3;
                stroke:rgb(0,0,0)" />
    <text transform="translate(2 15)">${d.label}</text>
    <text transform="translate(${d.valLabelLoc} 15)">${d.valLabel}</text>
</g>
{% endviz %}



In the chart below. the colors represent workload per week:
yellow = 0-3 hours
orange = 4-6 hours
green = 7-9 hours
blue = 10-12 hours
red = 13-15 hours
black = 16+
{% viz %}

{% title %}

CSCI classes - Instructor Grade vs Course Grade


{% solution %}
 
var csci = _.filter(data, function(d){
    return (d.CrsPBADept == 'CSCI') && 
        d.hasOwnProperty("AvgCourse") && 
        d.hasOwnProperty("AvgInstructor")
});
console.log(_.size(csci));
var stuff = _.map(csci, function(d){
    var obj = {}
    obj.AvgCourse = d.AvgCourse;
    obj.AvgInstructor = d.AvgInstructor;
    obj.Workload = d.Workload.Hrs_Wk;
    return obj;
})
console.log(stuff[0])


function computeX(d, i) {
    
    return d.AvgCourse*60;
}

   
// 6 is max grade, need to invert so high scores on top of graph
function computeY(d, i) {
    return (6 - d.AvgInstructor) *60;
}

function computeColor(d, i) {
    if (d.Workload == "0-3")
        return 'yellow';
    if (d.Workload == "4-6")
        return 'orange';
    if (d.Workload == "7-9")
        return 'green'
    if (d.Workload == "10-12")
        return 'blue'   
    if (d.Workload == "13-15")
        return 'red'
    return 'black'  //16+
}
/*function computeLabel(d){
    return d.type
}

function computeValLabel(d) {
    return _.round(d.avg,2)
}
function computeValLabelLoc(d,i,data) {
    var width = computeWidth(d,i,data);
    return width + 2;
} */
var viz = _.map(stuff, function(d, i, data){

            return {
                x: computeX(d, i),
                y: computeY(d, i),
                color: computeColor(d, i),
               // label: computeLabel(d),
               // valLabel : computeValLabel(d),
               // valLabelLoc : computeValLabelLoc(d,i,data)
            }
         })


var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')


{% template %}
<circle cx="${d.x}"
     cy="${d.y}"
     r="4"
      stroke-width="1" 
      fill="${d.color}" />
{% endviz %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}
var clean = _.filter(data, function(n){
    return n.PCT.D != ""
})

var map = _.map(clean, function(n){
  return {dept: n.CrsPBADept, gpa: n.AVG_GRD, professor: n.AvgInstructor, name: _.pluck(n.Instructors, "name")[0]}
})

groups =  _.groupBy(map, function(n){
  return n.name
})


function computeColor(d) {
    if (d == "APPM"){
        return "rgb(179, 28, 58)"
    }
    else {
        return "rgb(182, 184, 184)"
    }
}

viz =  _.map(groups, function(n){
    return {avgGpa: _.sum(n, function(course){
                return course.gpa
            })/n.length,
            avgRating: _.sum(n, function(course){
                return course.professor
            })/n.length,
            dept: n[0].dept,
            color: computeColor(n[0].dept),
            name: n[0].name }
})
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}
<circle cx="${d.avgRating*100}" 
        cy="${500-d.avgGpa*100}" 
        r = 2
        stroke="${d.color}" 
        stroke-width="3" 
        fill="${d.color}"
        style="opacity:0.4"
        />

{% endviz %}


