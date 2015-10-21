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

# Which course has the highest enrollment? by Andrew Berumen

{% lodash %}
var groups = _.groupBy(data, 'CourseTitle');
var coursesEnroll = _.mapValues(groups, function(d){
    var enrollNumbers = _.pluck(d, 'N.ENROLL')
    return _.sum(enrollNumbers)
})
var max = _.max(coursesEnroll);
var bigClass =  _.pick(coursesEnroll, function(d){
    return d == max;
});


return bigClass;

{% endlodash %}

<table><tr><td>Class Title</td>
	<td>Enrollment</td></tr>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# Which department has the lowest enrollment?  by John

{% lodash %}
var groups = _.groupBy(data, 'CrsPBADept');
var coursesEnroll = _.mapValues(groups, function(d){
    var enrollNumbers = _.pluck(d, 'N.ENROLL')
    return _.sum(enrollNumbers)
})
var min = _.min(coursesEnroll);
var smallDept =  _.pick(coursesEnroll, function(d){
    return d == min;
});
return smallDept;
{% endlodash %}

<table><tr><td>Department</td>
	<td>Enrollment</td></tr>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# How many instructors have taught each subject? by Kari

{% lodash %}



var groups = _.groupBy(data, 'Subject');
// collect all the instructor names for each class and count uniq
var ret1 = _.mapValues(groups, function(d){
 	var instrArr = _.pluck(d, 'Instructors');
 	//var j = 0;
 	var nameArr = _.map(instrArr, function(d){
 		var names = _.pluck(d, 'name');
 		//if (j==0){console.log(names); j++}
 		return names;
 	});
 	return _.size(_.uniq(_.flatten(nameArr)));
});

return ret1;

{% endlodash %}

<table><tr><td>Subject</td>
	<td>Num Instructors</td></tr>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# Does the instruction tends to give out higher grades if they teach more classes? or the reverse? by Ming
{% lodash %}
//var i = 0;  // for console.log
//var j = 0;  // for console.log
  // first I need to remove all entries that don't have an AVG_GRD (I have seen a couple!)
var graded = _.filter(data,function(d){
	return d.hasOwnProperty("AVG_GRD");
})
//console.log(_.size(graded))
var smallData = _.map(graded, function(d){
	// only want avg grade grade and instructor name
	// but there can be multiple instructors - return array of obj (grade,instructor)
	var avg_grd = d.AVG_GRD;
	//if (i==0){console.log(d.Instructors); i++}
	var nameArr = _.pluck(d.Instructors, 'name');
   //if (j==0){console.log(nameArr); j++}
 	// now take that array of names and map to an array of obj, each with a name and an avg grade
 	// this brought #entries from 5000 -> 4854
 	var objArray = _.map(nameArr, function(d){
 		var obj = {name:d,AVG_GRD:avg_grd};
 		return obj;
 	})
 	return objArray;
});

// smallData has array of arrays of obj, so flatten, then group by name
var groups = _.groupBy(_.flatten(smallData),'name');
//console.log(_.size(groups));
// groups are by name, with an array of obj containing name and avg grade
// we want convert each to an obj with class count and avg of avg, we don't even need name any more...
var groups2 = _.map(groups, function(d){
	var avg = _.reduce(d, function(total,e){
		return total+e.AVG_GRD;
	},0)/_.size(d);
	var obj = {classcount:_.size(d),AVG_GRD:avg,name:_.first(d).name}
	return obj;
});

var groups3 = _.groupBy(groups2,'classcount');
// each group has all of the instructors/grades that taught key # of classes.
// to finish, average all the grades together for each key, then done!
var avgbyCount = _.mapValues(groups3, function(d){
	var avg = _.round(_.reduce(d, function(total,e){
		return total+e.AVG_GRD;
	},0)/_.size(d),2);
	var obj = {classcount:_.first(d).classcount,AVG_GRD:avg,instrCount:_.size(d)}
	return obj;
});


return avgbyCount
{% endlodash %}
Based on the table below, there does not seem to be a trend between the number of classes taught and average grade.
<table><tr><td>Num Classes Taught</td>
	<td>Avg Grade</td><td>Num Instructors</td>
	</tr>
{% for num, obj in result %}
    <tr>
        <td>{{num}}</td>
        <td>{{obj.AVG_GRD}}</td>
        <td>{{obj.instrCount}}
    </tr>
{% endfor %}
</table>


# Which subject is most in demand,based on the total number of enrollment?  by Sussant

{% lodash %}
var group = _.groupBy(data, "Subject")
var sum = _.mapValues(group, function(n){
    var enroll = _.pluck(n, "N.ENROLL")
    return _.sum(enroll)
})
var max = _.max(sum)
var result = _.pick(sum, function(x){
    return x == max
})
return result
{% endlodash %}
{{result | json}}
{% for key, val in result %}
{{key}} is the subject most in demand with {{val}} enrollments.
{% endfor %}
