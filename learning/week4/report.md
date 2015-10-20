{% data src="../../hackathons/fcq/fcq.clean.json" %}
{% enddata %}


# Report

As a class, we brainstormed and came up with a long list of further questions we
can ask based on the FCQ data. Out of these questions, our team chose to tackle on
the following questions. Each member on our team is reponsible for one question.

# How many instructors have taught each subject? Kari

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

# Does the instruction tends to give out higher grades if they teach more classes? or the reverse? Ming

{% lodash %}

var graded = _.filter(data,function(d){
	return d.hasOwnProperty("AVG_GRD");
})

var smallData = _.map(graded, function(d){
	var avg_grd = d.AVG_GRD;
	var nameArr = _.pluck(d.Instructors, 'name');
 	var objArray = _.map(nameArr, function(d){
 		var obj = {name:d,AVG_GRD:avg_grd};
 		return obj;
 	})
 	return objArray;
});

var groups = _.groupBy(_.flatten(smallData),'name');
var groups2 = _.map(groups, function(d){
	var avg = _.reduce(d, function(total,e){
		return total+e.AVG_GRD;
	},0)/_.size(d);
	var obj = {classcount:_.size(d),AVG_GRD:avg,name:_.first(d).name}
	return obj;
});

var groups3 = _.groupBy(groups2,'classcount');
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


# Which department has the lowest enrollment? John

{% lodash %}
var grps = _.groupBy(data, 'CrsPBADept')
var ret1 = _.mapValues(grps, function(d){
  var enrollNumbers = _.pluck(d, 'N.ENROLL')
  return _.sum(enrollNumbers)
  })
  var min = _.min(ret1)
  var dept = _.pick(ret1, function(d){
    return d == min
    })

return dept

{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


# Which subject is most in demand,based on the total number of enrollment? Sussant

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

# Which course has the highest enrollment? Andrew

{% lodash %}
var grps = _.groupBy(data, 'CourseTitle')
var ret1 = _.mapValues(grps, function(d){
  var enrollNumbers = _.pluck(d, 'N.ENROLL')
  return _.sum(enrollNumbers)
  })
  var max = _.max(ret1)
  var bigClass = _.pick(ret1, function(d){
    return d == max
    })

return bigClass

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

