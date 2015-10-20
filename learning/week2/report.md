{% import '../../hackathons/classmates/data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# How many submitted on or before the deadline? (8/24/15)

{% lodash %}
return _.size(_.filter(data.comments, function(n) {
    var date = n.created_at.split('T')[0].split('-')[2]
    if (date <= "24") {
        return true
    }
}))
{% endlodash %}

The answer is {{result}}.


# How many submitted after the deadline?

{% lodash %}
return _.size(_.filter(data.comments, function(n) {
    var date = n.created_at.split('T')[0].split('-')[2]
    if (date > 24) {
        return true
    }
}))
{% endlodash %}

The answer is {{result}}.


# How many people are CSCI majors?

{% lodash %}
var text = data.comments
var major = _.filter(_.pluck(text,'body'),function(n){
	return _.includes(n,"Computer") || _.includes(n,"CS") || _.includes(n, "cs\r")
})

return _.size(major)

return "[answer]"
{% endlodash %}

The answer is {{result}}.

# Who has the ID "13950166"?

{% lodash %}

var text = _.filter(data.comments, function(n){
	return _.includes(n.user,13950166)
});

var foo = _.pluck(text,'body')
var bar = _.map(foo,function(name){
	var foobar = name.split("\r\n")[0]
	return _.last(foobar.split("Name:"))
});

return bar

{% endlodash %}

The answer is {{result}}.
