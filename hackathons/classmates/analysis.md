# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}
var comments = data.comments
var list=_.filter(_.pluck(comments, 'body'), function(text){
	var food=_.last(text.split("Favorite Food:"))
	return _.includes(food, "Sushi")
})

return _.size(list)
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
var pythonList=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Python") || _.includes(text, "python")
})
var names=_.map(pythonList, function(name){
	var a=name.split("\r\n")[0]
	return _.last(a.split("Name:"))
})
return names
{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
var jsList=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Javascript") || _.includes(text, "javascript")
})
var javaList=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Java") || _.includes(text, "java")
})
if(_.size(jsList) > _.size(javaList))
	return "Javascript"
else
	return "Java"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
var foodList=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Vegan")
})
var names=_.map(foodList, function(name){
	var a=name.split("\r\n")[0]
	return _.last(a.split("Name:"))
})
return names
{% endlodash %}

Their names are {{result}}.
