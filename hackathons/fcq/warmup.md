{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
return _.uniq(_.pluck(data, 'Subject')).length;
{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
// TODO: replace with code that computes the actual result
return 63
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
return _.mapValues(_.groupBy(data, 'Subject'), function(group){
return _.uniq(_.pluck(group, 'Course'))
});
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
return _.pick(_.mapValues(_.groupBy(data, 'Subject'), function(group){
return group.length;
}), function(n){
return n > 100;
});
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
return _.pick(_.mapValues(_.groupBy(data, 'Subject'), function(group){
return _.reduce(group, function(sum, course){
return sum+course.N.ENROLL;
}, 0);
}), function(n){
return n > 5000
});
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
return _.uniq(_.pluck(_.filter(data, function(course){
return _.contains(_.pluck(course.Instructors, 'name'), 'YEH, PEI HSIU');
}), 'Course'));
{% endlodash %}

They are {{result | json}}.