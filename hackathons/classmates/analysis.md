# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}
var bodies = _.pluck(data.comments,'body')
//console.log(bodies)
var foods = _.filter(bodies, function(str) {
   var lower = str.toLowerCase();
   return lower.indexOf('sushi') > 0;
  });

return foods.length
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
// find all the comment bodies that have "python", then pull out the names into an array
var bodies = _.pluck(data.comments,'body')
//console.log(bodies)
var python = _.filter(bodies, function(str) {
	// get the programming language part of the string:
	var strArray = str.split('\n') 
	// program lang is  element 2
	var progLang = strArray[2];
	
   var lower = progLang.toLowerCase();
   return lower.indexOf('python') > 0;
  });


var names = [];
function addName(str) {
  var name = _.last(_.first(str.split('\r')).split(': '));
  names.push(name);
}
python.forEach(addName)

return names.toString();


{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
// find all the comment bodies that have "python", then pull out the names into an array
var bodies = _.pluck(data.comments,'body')
var java = _.filter(bodies, function(str) {
	var strArray = str.split('\n') 
	// program lang is  element 2	
   var lower = strArray[2].toLowerCase();
   return lower.match(/java[^s]/);
  });
 

var javascript = _.filter(bodies, function(str) {
	var strArray = str.split('\n') 
	// program lang is  element 2	
   var lower = strArray[2].toLowerCase();
   return lower.match(/javascript|js/);
  });
 
  if (java.length > javascript.length) 
  	return "More people like Java ("+java.length+" vs "+javascript.length+")"
  else if (java.length < javascript.length)
  	return "More people like Javascript ("+javascript.length+" vs "+java.length+")"
  else  // equal
  	return "People like Javascript and java the same!(each had "+javascript.length+")"
return "[answer]"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
var bodies = _.pluck(data.comments,'body')
x = _.find(data.comments, _.matchesProperty("user.login", "kjblakemore"));
var food = _.last(x.body.split('Favorite Food: ')).toLowerCase();
var foodies = _.filter(bodies, function(str) {
	// get the Favorite food part of string, and make lower case
	var str = _.last(str.split('Favorite Food: '))
	var lower = str.toLowerCase();
	// do the foods match?
    return lower.indexOf(food) >= 0;
  });

// get all the names of students who matched foods
var names = [];
function addName(str) {
  var name = _.last(_.first(str.split('\r')).split(': '));
  names.push(name);
}
foodies.forEach(addName)

if (names.length <= 1) return "No one else like the same food as kjblakemore (which was "+food+").";
return names.toString()+ "liked the same food as kjblakemore (which was "+food+").";

{% endlodash %}

{{result}}.
