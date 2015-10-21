# Lodash Drills

Complete the following Lodash exercises. The goal is to become really good at
functional programming paradigm (e.g., `_.map`, `_.filter`, `_.all`, `_.any` ...etc) and
a number of really useful Lodash methods (e.g., `_.find`, `_.pluck` ... etc).

* enter your solution in the `solution` block
* utilize lodash functions as much as possible
* no `for/while` loop is allowed

Familiarity with programming in this way will not only make you a super productive
programmer but also will pave the way for you to learn MapReduce and MongoDB.

# Examples

{% lodashexercise %}

{% title %}

How many people?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

4

{% solution %}

return data.length

{% endlodashexercise %}


{% lodashexercise %}

{% title %}

What are the names?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

['John', 'Mary','Joe','Ben']

{% solution %}

return _.map(data, function(d){
    return d.name
})

{% endlodashexercise %}

# Exercises

{% lodashexercise %}

{% title %}

What names begin with the letter J?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

['John','Joe']

{% solution %}

var result = _.filter(data, function(d){
    return d.name.charAt(0) == 'J'
})

var result1 = _.map(result,function(n){
  return n.name
})
  

return result1

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

How many Johns?

{% data %}

[{name: 'John'}, {name: 'John'}, {name: 'John'}, {name: 'Ben'}]

{% output %}

3

{% solution %}
var result = _.size(_.filter(data,function(d){
  return d.name == 'John'

}));
return result

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

What are all the first names?

{% data %}

[{name: 'John Smith'}, {name: 'Mary Kay'}, {name: 'Peter Pan'}, {name: 'Ben Franklin'}]

{% output %}

["John","Mary","Peter","Ben"]

{% solution %}
var result = _.map(data,function(d){
  var n = d.name.split(" ")
  return n[0]
});
return result

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

What are the first names of Smith?

{% data %}

[{name: 'John Smith'}, {name: 'Mary Smith'}, {name: 'Peter Pan'}, {name: 'Ben Smith'}]

{% output %}

["John","Mary","Ben"]

{% solution %}
var result = _.filter(data,function(d){
  var n = d.name.split(" ")
  if(n[1] == 'Smith')
    return n
})


var result1 = _.map(result,function(n){
  var names = n.name.split(" ")
  return names[0]
})



return result1
{% endlodashexercise %}







{% lodashexercise %}

{% title %}

Change the format to lastname, firstname

{% data %}

[{name: 'John Smith'}, {name: 'Mary Kay'}, {name: 'Peter Pan'}]

{% output %}

[{name: 'Smith, John'}, {name: 'Kay, Mary'}, {name: 'Pan, Peter'}]

{% solution %}
var result = _.map(data,function(n){
  var name = n.name.split(" ")
  return {"name":name[1] + ", " + name[0]}

})
return result
{% endlodashexercise %}



{% lodashexercise %}

{% title %}

How many women?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

1

{% solution %}

var result = _.size(_.filter(data,function(d){
    return d.gender == 'f';
}));
return result

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

How many men whose last name is Smith?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

2

{% solution %}

var result = _.filter(data,function(d){
  var n = d.name.split(" ")
  if(n[1] == 'Smith')
    return n
})

var male = _.filter(result,function(n){
  return n.gender == 'm'
})

return _.size(male)

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

Are there more men than women?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

true

{% solution %}

var male = _.filter(data,function(n){
  return n.gender == 'm'
})

var female = _.filter(data,function(n){
  return n.gender == 'f'
})

var a = _.size(male)
var b = _.size(female)

var result = false
if(a > b){
  result = true;
} else {
  result = false;
}


return result

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

What is Peter Pan's gender?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

'm'

{% solution %}

var result = _.pluck(_.filter(data,{'name':'Peter Pan'}),'gender')

return result[0]

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

What is the oldest age?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

54

{% solution %}


var age = _.pluck(_.sortBy(data,'age'),'age')
var oldest = age.length - 1
return age[oldest]

{% endlodashexercise %}






{% lodashexercise %}

{% title %}

Is it true everyone is younger than 60?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

true

{% solution %}

// use _.all
var result = _.all(data,function(n){
  return n.age < 60
})
return result

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

Is it true someone is not an adult (younger than 18)?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

true

{% solution %}

// use _.some
var result = _.some(data,function(n){
  return n.age < 18
})
return result

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

How many people whose favorites include food?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

3

{% solution %}
var result = _.filter(data,function(n){
    return _.includes(n.favorites,'food')
})

return _.size(result)

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

Who are over 40 and love travel?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

['Mary Smith', 'Joe Johnson']

{% solution %}

var a = _.filter(data,function(n){
  return n.age > 40
})

var b = _.filter(a,function(n){
  return _.includes(n.favorites,'travel')
})

var result = _.map(b,function(n){
  return n.name
})
return result

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

Who is the oldest person loving food?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

'John Smith'

{% solution %}

var food = _.filter(data,function(n){
    return _.includes(n.favorites,'food')
})

var age = _.pluck(_.sortBy(food,'age'),'name')
var oldest = age.length - 1
return age[oldest]

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

What are all the unique favorites?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

[
  "food",
  "movies",
  "travel",
  "minecraft",
  "pokemo",
  "craft"
]

{% solution %}

// hint: use _.pluck, _.uniq, _.flatten in some order

var a = _.pluck(data,'favorites')
var result = _.uniq(_.flatten(a))

return result

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

What are all the unique last names?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

[
  "Smith",
  "Pan",
  "Johnson"
]

{% solution %}

var lastName = _.map(data,function(n){
  var a = n.name.split(" ")
  return a[1]
})

var result = _.uniq(lastName)
return result

{% endlodashexercise %}
