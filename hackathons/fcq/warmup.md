{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
return _.compact(_.uniq(_.pluck(data, 'Subject')))

{% endlodash %}

They are {{ result.length }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}

return _.size(_.filter(data,'Subject','CSCI'))


{% endlodash %}

There are {{ result | json }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}

var grps = _.groupBy(data, 'Subject')
return _.mapValues(grps, function(d){
    return d.length
})

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
var grps = _.groupBy(data, 'Subject')
var ret = _.pick(_.mapValues(grps, function(d){
    return d.length
}), function(x){
    return x > 100
})
var ret1 = _.pick(_.mapValues(grps, function(d){
  var enrollNumbers = _.pluck(d, 'N.ENROLL')
  return _.sum(enrollNumbers)
  }), function(x){
    return x > 5000
  })
return ret1

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
var tomClass = _.filter(data, function(d){
  x = _.where(d['Instructors'], {'name':"YEH, PEI HSIU"})
  return _.size(x)
  })
  return _.pluck(tomClass, 'Course')

{% endlodash %}

They are {{result }}.
