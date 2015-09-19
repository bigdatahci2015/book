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

# (Question 1) What should my major be if I want have a high gpa (AndreySHprengel)
{% lodash %}
var grps = _.groupBy(data, function(c){return c.Subject})
var grades = _.mapValues(grps, function(grp){return _.compact(_.pluck(grp, 'AVG_GRD'))})
var grades = _.mapValues(grades, function(group){
var total = 0
_.map(group, function(n){
//console.log()
total += n
return total
}
)
return total/(_.size(group))})
grades = _.map(grades, function(value, key){
return {"subject": key, "grade":value}})
return _.sortBy(grades, "grade").reverse()
{% endlodash %}
{{result | json}}


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

# (Question 5) by (Name)

{% lodash %}
var grps = _.groupBy(data, function(n) {
        return n.Subject})

var hours = _.mapValues(grps, function(grp) {
        return _.pluck(grp, 'Hrs_Wk')})

var hours = _.mapValues(hours, function(grp) {
        total = 0
        _.map(grp, function(n) {
        total += n
        return total })
        return total/(_.size(grp))
})

return "[answer]"
{% endlodash %}
