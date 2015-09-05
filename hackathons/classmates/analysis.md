# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}

return _.size(_.filter(data.comments,function(n) {
return _.contains(n.body,'Sushi')
}))

{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}

return _.pluck(_.filter(data.comments,function(n) {return _.contains(n.body,'Python')}),'user.login')

{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
a = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,'Javascript')}))
b = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,'Java')}))
if (_.isEqual(a,b))
return 'Neither'
else if (_.gt(a,b))
return 'Javascript'
else
return 'Java'
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}

food = _.last(_.find(data.comments, {user: {login: 'kjblakemore'}}).body.split('Favorite Food: '))

return _.pluck(_.filter(data.comments,function(n) { return _.contains(n.body,food) }),'user.login')
{% endlodash %}

Their names are {{result}}.
