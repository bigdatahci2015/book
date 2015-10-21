{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
var subject = _.map(data,function(d){
    return d['Subject']
})

return _.size(_.uniq(subject))
    
{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
// TODO: replace with code that computes the actual result
var cs = _.filter(data,function(d){
    return d['CrsPBADept'] == 'CSCI'
})
return _.size(cs)
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result

var subject = _.groupBy(data,'Subject')

var result = _.mapValues(subject,function(n){
    return n.length
})
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
/*var ret = _.pick(_.mapValues(grps, function(d){
    return d.length
}), function(x){
    return x > 100
})*/
var result = _.mapValues(grps,function(n){
    return n.length 
})

return _.pick(result,function(n){
    return n > 100
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

## What subset of these subject codes have more than 5000 total enrollments?

{% lodash %}
// TODO: replace with code that computes the actual result
//return {"IPHY": 5507,"MATH": 8725,"PHIL": 5672,"PHYS": 8099,"PSCI": 5491}

var groups = _.groupBy(data,function(n){
    return n['Subject']
})

var enroll = _.mapValues(groups, function(a){
    return _.map(a,function(b){
        return b['N']['ENROLL']
    })
})

var total = _.mapValues(enroll, function(n){
    return _.sum(n)
})

return _.pick(total,function(tot){
    return tot > 5000
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

## What are the course numbers of the courses Tom (PEI HSIU) Yeh taught?

{% lodash %}
// TODO: replace with code that computes the actual result
//return ['4830','4830']

var courses= _.filter(data, function(course){
  var instructor= _.filter(course['Instructors'], function(instructor){
    return instructor['name'] == 'YEH, PEI HSIU'
  })
  return _.size(instructor) > 0
})
return _.map(courses, function(course){
  return course['Course']
})
{% endlodash %}



They are {{result}}.
