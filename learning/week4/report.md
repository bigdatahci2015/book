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

# Which instructor's course has the highest enrollment? by Zhili Yang

{% lodash %}
var list = _.map(data, function(course){
  var instructors=course['Instructors']
  var enroll=course['N']['ENROLL']
  var courseName=course['CourseTitle']
  return _.map(instructors, function(instructor){
    return {"instructor": instructor['name'], "courseTitle": courseName, "enrollment": enroll}
  })
})

var maxGroups=_.max(_.flatten(list), function(course){
	return course['enrollment']
})
return maxGroups
{% endlodash %}
The professor is {{result['instructor']}}, the course title is {{result['courseTitle']}}.

# How many courses in IPHY that has 4 credits hours ? by Fadhil Suhendi

{% lodash %}
var course = _.filter(data,function(n){
 return n['CrsPBADept'] == 'IPHY'
})
var hour = _.filter(course,function(d){
 return d['Hours'] == 4
})

return _.size(hour)
{% endlodash %}

They are {{ result }} courses that have 4 credits hour.


# What departments offer the most 4000 level classess? By Brian

{% lodash %}
var group = _.groupBy(data,function(college){
  return college['Subject']
})

var courseLevels = _.mapValues(group,function(a){
  return _.map(a,function(b){
    return b['Course']
  })  
})
var count = 0
var levelCount = _.mapValues(courseLevels,function(level){
  count = 0
  return _.map(level,function(n){
    if(n >= 4000 && n < 5000){
    count++
  }
  return count
  })
})

var result = _.mapValues(levelCount,function(n){
  return _.max(n)
})
return _.pick(result,function(number){
  return number == _.max(result)
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

# Which department has the highest enrollment? By Tristan


{% lodash %}

var groups = _.groupBy(data,function(n){
    return n['Subject']
})

var courseEnroll = _.mapValues(groups, function(a){
    return _.map(a,function(b){
        return b['N']['ENROLL']
    })
})

var enroll = _.mapValues(courseEnroll, function(n){
    return _.sum(n)
})

return _.pick(enroll,function(number){
    return number == _.max(enroll)
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

# What instructors has the highest rating? By Andrew

{% lodash %}

var list = _.map(data, function(course){
  var instructors=course['Instructors']
  var enroll=course['AvgInstructor']
  return _.map(instructors, function(instructor){
  return {"instructor": instructor['name'], "rating": enroll}
  })
})

var maxGroups= _.max(_.flatten(list), function(course){
 return course['rating']
})
return maxGroups

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>
