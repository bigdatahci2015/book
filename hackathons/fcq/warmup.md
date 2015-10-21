{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
return _.compact(_.uniq(_.pluck(data, 'Subject')))
{% endlodash %}

They are {{ result.length }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
// TODO: replace with code that computes the actual result
var size = _.size(_.filter(data,'Subject','CSCI'));
return size
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
var groups = _.groupBy(data, 'Subject');
var subjCount = _.mapValues(groups, function(d){
    return d.length;
})
return subjCount
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
var groups = _.groupBy(data, 'Subject');
var subjCount = _.mapValues(groups, function(d){
    return d.length;
});
var subj100 =  _.pick(subjCount, function(d){
    return d > 100;
});
return subj100;

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
var groups = _.groupBy(data, 'Subject');
var subjCount = _.mapValues(groups, function(d){
    var enrollNumbers = _.pluck(d, 'N.ENROLL')
    return _.sum(enrollNumbers)
})

var subj5000 =  _.pick(subjCount, function(d){
    return d > 5000;
});
return subj5000;
// TODO: replace with code that computes the actual result
return {"IPHY": 5507,"MATH": 8725,"PHIL": 5672,"PHYS": 8099,"PSCI": 5491}
{% endlodash %}

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
