{% import '../../hackathons/classmates/data.html' as data %}

# Report

There are {{ data.comments.length }} students who gave a self-introduction. As a
class, we brainstormed and came up with a long list of further questions we can
ask based on this data. Our team chose to tackle on the following:

# How many students submitted personal information on or before the class deadline of 8/24/15?

{% lodash %}
var dueDate = new Date(2015, 7, 25);  // start of sept 25 2015 

// filter array to inculde only students whose create date was before Sept 25 0hrs
var students = _.filter(data.comments, function(item) {
	var createDate = new Date(item.created_at)
	return (createDate <= dueDate)
   
  });

return students.length
{% endlodash %}

{{result}} students submitted their personal information by the end of Sept 24, 2015.

# How many students have the term "computer" or "cs" in the description of the department or major?

{% lodash %}
// find all the comment bodies that have "cs" or csci, then pull out the names into an array
var bodies = _.pluck(data.comments,'body')
var major = _.filter(bodies, function(str) {
	// get the major
	var strArray = str.split('\n') ;
	// Major is element 1
	var major = strArray[1];
	
   var lower = major.toLowerCase();
   // space added in front of term to avoid words where "cs" in middle of word
   return (lower.indexOf(' computer') > 0) | (lower.indexOf(' cs') > 0);
  });

return major.length;
{% endlodash %}

{{result}} students have the term "computer", "cs" or "csci" in the description of the department or major

# Who has the user id 13950166?

{% lodash %}
x = _.find(data.comments, _.matchesProperty("user.id", 13950166));
var nameStr = _.first(x.body.split('\r'));
var name = _.last(nameStr.split(': '))
return name
{% endlodash %}

The person's name is {{result}}.


# Who used their lastname as part of their github user ID?

{% lodash %}

var names = []
var students = _.filter(data.comments, function(item) {
	
	var nameStr = _.first(item.body.split('\r'));
	var lastName = _.last(nameStr.split(' '));
	var lowerCaseLastName = lastName.toLowerCase();
	var lowerCaseLogin = item.user.login.toLowerCase();
	return (lowerCaseLogin.indexOf(lowerCaseLastName) >= 0) //is true if last name is in user login 
  });


var names = [];
// get full name out of body string and add to names[]
function addName(obj) {
  var name = _.last(_.first(obj.body.split('\r')).split(':'));
  names.push(name);
}
students.forEach(addName)

return names.toString();
  
{% endlodash %}

{{result}} are the students who used their last name as part of their github user id.

