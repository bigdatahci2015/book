{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
var codes=_.map(data, function(college){
    return college['Subject']
})
var uniqCodes=_.uniq(codes)
return _.size(uniqCodes)
{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
var courses=_.filter(data, function(college){
    return college['CrsPBADept'] == 'CSCI'
})
return _.size(courses)
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
var list=_.groupBy(data, function(college){
    return college['Subject']
})
return _.mapValues(list, function(courses){
    return courses.length
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
var groups=_.groupBy(data, function(college){
    return college['Subject']
})
var coursesSize= _.mapValues(groups, function(courses){
    return courses.length
})
return _.pick(coursesSize, function(size){
    return size > 100
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
var groups=_.groupBy(data, function(college){
    return college['Subject']
})
var coursesEnroll= _.mapValues(groups, function(courses){
    return _.map(courses, function(course){
        return course['N']['ENROLL']
    })
})
var enroll=_.mapValues(coursesEnroll, function(enrolls){
    return _.sum(enrolls)
})
return _.pick(enroll, function(number){
    return number > 5000
})
/*return {"IPHY": 5507,"MATH": 8725,"PHIL": 5672,"PHYS": 8099,"PSCI": 5491}*/
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
var courses=_.filter(data, function(course){
    var instructor=_.filter(course['Instructors'], function(instructor){
        return instructor['name'] == 'YEH, PEI HSIU'
    })
    return _.size(instructor) > 0
})
return _.map(courses, function(course){
    return course['Course']
})
//return ['4830','4830']
{% endlodash %}

They are {{result}}.
