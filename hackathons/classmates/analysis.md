# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?


{% lodash %}


var body = _.pluck(data.comments,"body")
 
 var noOfSushiLover =_.size(_.filter(body,function(n){return _.contains(n,"Sushi")}))
 

return noOfSushiLover


{% endlodash %}

The Number of studen who likes the Sushi as their faviorate food  are {{result}}.

## Who are the students liking Python the most?

{% lodash %}
var names_array="";
var body = _.pluck(data.comments,"body")
 
 var python =_.filter(body,function(n){return _.contains(n,"Python")})
var py=_.forEach(python, function(n) {
n=_.trimLeft(n,"Name: ");
n= _.first(n.split('\n')) ;
console.log(n);
 names_array=_(names_array).concat(n);
} );
 

return names_array; 

{% endlodash %}

Their names of persons who likes the python are:- {{result}}.

## Are there more Javascript lovers or Java lovers?

var check;
{% lodash %}

var body = _.pluck(data.comments,"body")
 
 var Javascript =_.size(_.filter(body,function(n){return _.contains(n,"Javascript")}))
 var javascript =_.size(_.filter(body,function(n){return _.contains(n,"javascript")}))
 var Javascript_total=_.add(Javascript,javascript)
 var Java =_.size(_.filter(body,function(n){return _.contains(n,"Java")}))
 
 var language =[{'lang' : 'Java' ,'size' : Java},{'lang' : 'Javascript' ,'size' : Javascript_total}]
 check=_.pluck(_.sortBy(language,'size'),'lang');
return _.last(check)
{% endlodash %}

There are more {{result}} lover.




## Who like the same food as `kjblakemore`?

{% lodash %}

 
 var user_kjblakemore =_.filter(data.comments,function(n){return (n.user.login =="kjblakemore");});

 
  var food=_.last(user_kjblakemore[0].body.split('\r'));

var user_samefood =_.filter(data.comments,function(n){return _.contains(n.body,food);});
var nameSameFoodPerson=_.first(user_samefood[0].body.split('\r'));
 return nameSameFoodPerson;

{% endlodash %}


The person who like the same food as kjblakemore are {{result}}.
