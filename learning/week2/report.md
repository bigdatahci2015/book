{% import '../../hackathons/classmates/data.html' as data %}

# Report

There are {{ data.comments.length }} students who gave a self-introduction. As a
class, we brainstormed and came up with a long list of further questions we can
ask based on this data. Our team chose to tackle on the following:

# How many people submitted comments before the first class?

{% lodash %}
return _.size(_.filter(data.comments,function(n) {
return _.gt(new Date("2015-08-24T16:00:00Z"),new Date(n.created_at))}))
{% endlodash %}

A total of {{ result }} out of {{ data.comments.length }} students submitted comments before the first class.


# What percent of students are in the CS department?

{% lodash %}
return _.size(_.filter(data.comments,function(n) {
return _.contains(n.body,'Computer Science')
}))
{% endlodash %}

A total of {{ result }} out of {{ data.comments.length }} students are in the Computer Science department.

# Who has the oldest Github account?

{% lodash %}
return (_.find(data.comments, {'user': {'id': _.min(_.pluck(data.comments,'user.id'))}})).user.login;
{% endlodash %}

{{ result }} has the oldest GitHub account.

# What is the most popular programming language?

{% lodash %}

var python = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"Python")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"python")}))


var javascript = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"Javascript")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"javascript")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"JS")}))

var java = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"Java\")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"java\")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"JAVA\")}))

var c = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"C\")}))+_.size(_.filter(data.comments,function(n) {return _.contains(n.body,"C ")}))

var cpp = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"C++")}))
var csh = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"C#"))}))
var ruby = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"Ruby")}))
var hask = _.size(_.filter(data.comments,function(n) {return _.contains(n.body,"Haskell")}))

{% endlodash %}