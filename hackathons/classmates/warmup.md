{% import './data.html' as data %}

# Warmup

As warmup, let's being with some simple questions.

The comments data is imported as `data.comments`.

## How many people have submitted comments?

{% lodash %}
// TODO: write code to answer this question
return data.comments.length
{% endlodash %}

There are {{result}} submissions.

## Who is the first person submitting a comment?

We can get the data of the first comment by

{% lodash %}
// TODO: use lodash's method instead of direct array access via [0]
return _.first(data.comments)
{% endlodash %}

The result is

{{ result | json }}

The person's name is {{ result.user.login }}.

{% set name = result.user.login %}

## What is {{name}}'s favorite food?

We will need to parse the comment to retrieve this data.

The comment text is
{{ result.body | json }}

The code to retrieve the data about the favorite food is (hint: use [split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)).

{% lodash %}
var text = _.first(data.comments).body
console.log(text)
var comment = text.split('\n'); 
console.log(comment)
var foodComment = _.last(comment);
console.log(foodComment)
var food = _.last(foodComment.split(': '))
console.log(food)

// TODO: add code to process text to get the person's favorite food

return food
{% endlodash %}

So, {{name}}'s favorite food is {{result}}.
