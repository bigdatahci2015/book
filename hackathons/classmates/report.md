{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:



# who has used their last name as the user github id?


{% lodash %}
var lastnamebody=[];
var final =_.filter(data.comments,function(n){var lastnamebody=n.body.split('\r')[0].split(' ')[2];
if(lastnamebody!=undefined)
lastnamebody=lastnamebody.toLowerCase();
//console.log(lastnamebody)
var login=n.user.login.toLowerCase();
//console.log(login)

if(login.indexOf(lastnamebody)>-1)return true;
else
return false;})
return _.size(final)
 
 
{% endlodash %}

the number of people ,who have used their last name in their id are {{result}}

# who has the id 13950166


{% lodash %}

var idname =_.filter(data.comments,function(n){
return n.user.id==13950166
})


var body=_.first(idname[0].body.split('\n'));
return body
{% endlodash %}

{{result}} has the id 13950166
# How many people are from  computer science major

{% lodash %}
var body = _.pluck(data.comments,"body")
 
 var food =_.size(_.filter(body,function(n){return _.contains(n,"Computer")||_.contains(n,"CS")||_.contains(n,"cs\r")}))
return food
{% endlodash %}

Number of people from the computer science are {{result}}
# How many ppl submitted on and befor the deadline 8/24/15

{% lodash %}

return _.size(_.pluck(_.filter(data.comments,function(chr){
                            return chr.created_at.split('T')[0].split('-')[2] <=24;}),"body"))

{% endlodash %}
the number of people who submitted before the deadline are  {{result}}

