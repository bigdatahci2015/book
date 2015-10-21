{% data src="../../hackathons/fcq/fcq.clean.json" %}
{% enddata %}


# Report

As a class, we brainstormed and came up with a long list of further questions we
can ask based on the FCQ data. Out of these questions, our team chose to tackle on
the following questions. Each member on our team is reponsible for one question.

# (Question 1)# Which department has the lowest enrollment? by John Raesly



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

# How many instructors have taught each subject?
 by (KariSantos)

{% lodash %}

var groups =_.groupBy(data,function(d){return d.Subject})
var result =_.mapValues(groups,function(t){ 
var pluckinst=_.pluck(t,'Instructors')
return _.size(_.uniq(_.flatten( _.map(pluckinst,function(t){return _.pluck(t,'name')}))))


})
return result

{% endlodash %}
{{result|json}}


<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


# (Question 3) Which course has the highest enrollment?by andrew


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

# (Question 4)Which subject is most in demand,based on the total number of enrollment?by Sushant Mittal

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
  
  <table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# (Question 5) Does the instruction tends to give out higher grades if they teach more classes? or the reverse?
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
	var avg = _.reduce(d, function(total,e){
		return total+e.AVG_GRD;
	},0)/_.size(d);
	var obj = {classcount:_.first(d).classcount,AVG_GRD:avg,instrCount:_.size(d)}
	return obj;
});
return avgbyCount
{% endlodash %}


{{result|json}}
