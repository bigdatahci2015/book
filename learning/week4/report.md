{% data src="../../hackathons/fcq/fcq.clean.json" %}
{% enddata %}

# Report

As a team, answer all the questions the team's members submitted on our
[course forum](https://github.com/bigdatahci2015/forum/issues/14). Each
team member is responsible for one question. But everyone should work together
to come up with a good solution. Your answer should consist of Lodash code
and a brief writeup. Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not
use any for loop.

It is important for everyone to understand all the solutions and make sure you
will be able to independently reproduce these solutions when asked to do so.
Coming up, we will incorporate variations of these questions into a future hackathon
 and you are expected to be capable of reproducing and adapting your solutions.

# (Question 1) by (Name)

# (Question 2) by (Name)

{% lodash %}
return "[answer]"
{% endlodash %}


# (Question 3) by (Name)

{% lodash %}
return "[answer]"
{% endlodash %}

# (Question 4) by (Name)

{% lodash %}
return "[answer]"
{% endlodash %}

# Which courses have the highest enrollment total? by Matt Schroeder

{% lodash %}
var course = _.groupBy(data, function(x) { return x.CourseTitle})
var enrolled = _.mapValues(course, function(grp) { return _.pluck(grp, 'N.ENROLL')})
var enrolled = _.mapValues(enrolled, function(grp) {
        var total = 0
        _.map(grp, function(n) {
        total += n
        return total }) 
        return total })
enrolled = _.map(enrolled, function(value, key){ return {"Course": key, "Total Enrollment": value}})
return _.sortBy(enrolled, "Total Enrollment").reverse()
{% endlodash %}
{{result | json}}