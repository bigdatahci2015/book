# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}
var text = _.pluck(data.comments, 'body')
var bodies = _.filter(text, function(str) {
  return str.indexOf('Sushi') > 0
  });
return bodies.length
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
var text = _.filter(data.comments, function(n){
	return _.includes(n.body,"Python")
});

var foo = _.pluck(text,'body')
var bar = _.map(foo,function(name){
	var foobar = name.split("\r\n")[0]
	return _.last(foobar.split("Name:"))
});

return bar


{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
var text = _.size(_.filter(data.comments, function(n){
	return _.includes(n.body,"Java");
}))

var bar = _.size(_.filter(data.comments, function(n){
	return _.includes(n.body,"Javascript");
}))
if(text > bar)
	return "Java"
else
	return "Javascript"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
var text = _.filter(data.comments, function(n){
	return _.includes(n.body,"Vegan");
})


var text1 = _.pluck(text, "body")
console.log(text1)
var name = []
var finalName = []
for(i = 0; i < _.size(text1);i++){
	name.push(_.first(text1[i].split("\r\n")))
	finalName.push(_.last(name[i].split('Name:')))
}
console.log(name)
return finalName

{% endlodash %}

Their names are {{result}}.
