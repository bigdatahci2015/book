# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}

var text = data.comments

var list = _.filter(_.pluck(text,'body'), function(text){
	var food = _.last(text.split("Favorite Food:"))
	return _.includes(food,"Sushi")
})
return _.size(list)
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
var list = _.filter(data.comments, function(n){
	return _.includes(n.body,"Python")
});

var a = _.pluck(list,'body')
var b = _.map(a,function(name){
	var ab = name.split("\r\n")[0]
	return _.last(ab.split("Name:"))
});

return b


{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
var text = data.comments
var java = _.size(_.filter(_.pluck(text,'body'), function(n){
	return _.includes(n.body,"Java")
}))

var javascr = _.size(_.filter(_.pluck(text,'body'), function(n){
	return _.includes(n.body,"Javascript")
}))

if(java > javascr)
	return "Java";
else
	return "Javascript";

return "[answer]"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
var list = _.filter(data.comments, function(n){
	return _.includes(n.body,"Vegan")
});

var a = _.pluck(list,'body')
var b = _.map(a,function(name){
	var ab = name.split("\r\n")[0]
	return _.last(ab.split("Name:"))
});

return b

return "[answer]"
{% endlodash %}

Their names are {{result}}.
