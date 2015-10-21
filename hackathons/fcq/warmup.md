{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
var result =_.size(_.uniq(_.pluck(data,"Subject")))
return result
{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
return _.size(_.filter(data,'Subject','CSCI'))

{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
var groups =_.groupBy(data,function(d){return d.Subject})
var result =_.mapValues(groups,function(t){return t.length})

return result
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 100 courses?

{% lodash %}
// TODO: replace with code that computes the actual result
var grps = _.groupBy(data, 'Subject')
var ret = _.pick(_.mapValues(grps, function(d){
    return d.length
}), function(x){
    return x > 100
})
return ret
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 5000 total enrollments?

{% lodash %}
// TODO: replace with code that computes the actual result
var grps = _.groupBy(data, 'Subject')
//console.log(grps)
var ret= _.mapValues(grps,function(d){return _.sum(_.pluck(d,'N.ENROLL'))

})
ret1=_.pick(ret,function(x){
    return x > 5000
})

return ret1{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What are the course numbers of the courses Tom (PEI HSIU) Yeh taught?

{% lodash %}
// TODO: replace with code that computes the actual result
var tomClass = _.filter(data,function(d){ 
   x = _.where(d['Instructors'], { 'name': "YEH, PEI HSIU" });
   //if (_.size(x) >0) {console.log(x)}
   return _.size(x);
});

//console.log (tomClass)

return _.pluck(tomClass,'Course')
{% endlodash %}

They are {{result}}.
