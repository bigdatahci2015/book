{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# How many students are Computer Science major?

{% lodash %}
var list=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Computer Science") || _.includes(text, "CS")
})
return _.size(list)
{% endlodash %}
The answer is {{result}}.

# How many students' names start with 'A'?

{% lodash %}
var list=_.filter(_.pluck(data.comments, 'body'), function(text){
	var a=text.split("\r\n")[0]
	var name=_.last(text.split("Name:"))
	return name.charAt(1) == 'A'
})
return _.size(list)
{% endlodash %}
The answer is {{result}}.

# How many students are not Computer Science major?

{% lodash %}
var list=_.filter(_.pluck(data.comments, 'body'), function(text){
	return _.includes(text, "Computer Science") || _.includes(text, "CS")
})
return data.comments.length-_.size(list)
{% endlodash %}
The answer is {{result}}.

# What's the github id of zhya215?

{% lodash %}
var list=_.filter(data.comments, function(text){
	return _.includes(text.user, "zhya215")
})
return _.pluck(list, 'user.id')
{% endlodash %}
The answer is {{result}}.