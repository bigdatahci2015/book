{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# How many students are in Computer Science?

{% lodash %}
var text = data.comments
var major = _.filter(_.pluck(text,'body'),function(n){
	return _.includes(n,"Computer Science") || _.includes(n,"CS")
})

return _.size(major)

return "[answer]"
{% endlodash %}

The answer is {{result}}.


# How many student's name starts with 'A'?

{% lodash %}


var list=_.filter(_.pluck(data.comments, 'body'), function(text){ 
	var a=text.split("\r\n")[0] 
	var name=_.last(text.split("Name:")) 
	return name.charAt(1) == 'A' 
}) 

return _.size(list)

{% endlodash %}

The answer is {{result}}


# How many students are not in Computer Science major?

{% lodash %}

var text = data.comments
var major = _.filter(_.pluck(text,'body'),function(n){
	return _.includes(n,"Computer Science") || _.includes(n,"CS")
})

return data.comments.length - _.size(major)


return "[answer]"
{% endlodash %}
The answer is {{result}}

# What is the ID number of Zhilli(zhya215)?

{% lodash %}
var text = data.comments
var a = _.filter(text,function(n){
	return _.includes(n.user,"zhya215")
})

var y = _.pluck(a,'user.id')

return y



return "[answer]"
{% endlodash %}

The answer is {{result}}
