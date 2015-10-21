# Lodash 101

[Lodash](https://lodash.com/docs) is one of the most popular utility-belt library.
It can make you very productive and effective in writing Javascript programs.

Read Lodash's page on npm [here](https://www.npmjs.com/package/lodash). How many times
was it downloaded just last week alone?

## Examples

### Array of numbers

{% set data = [1,2,3,4,5] %}
 var result
Let's create a data array withthe contents: {{data}}. This array has {{ data.length }} items.

To get the first item, we can use lodash's [_.first](https://lodash.com/docs#first).

{% lodash %} return _.first(data) {% endlodash %}

The result is {{ result }}.


To get the first 3 elements, we can use lodash's [_.take](https://lodash.com/docs#take)

{% lodash %}
 var result=_.take(data, 3)
 return result
{% endlodash %}

The result is {{ result }}.

### Array of objects

Let's create a data array consisting of objects.

{% set data = [{name: 'John', age: 45}, {name: 'Mary', age: 32}, {name: 'Peter', age: 54}] %}

We can dump the content using the `dump` filter.

{{ data | dump }}

To retrieve the name field from each object in this array, lodash's
[_.pluck](https://lodash.com/docs#pluck) is very handy.

{% lodash %}
var result= _.pluck(data, 'name')
return result
{% endlodash %}

The result is {{ result }}.

We can even display the result nicely as a bullet list

<ul>
{% for d in result %}
<li>
    {{d}}
</li>
{% endfor %}
</ul>

Using [_.find](https://lodash.com/docs#find), we can look up an object by its field.

Let's try to find out how old Mary is.

{% lodash %}
var result= _.find(data, {name: 'Mary'})
return result
{% endlodash %}

Mary is {{ result.age }} years-old.

## Challenges

Now it's your turn to take the following learning challenges.

### Data

{% set data = [{name: 'John', age: 45}, {name: 'Mary', age: 32}, {name: 'Peter', age: 54}, {name: 'Jane', age: 12}] %}

The data is

{{ data | dump}}

### Q: What are the ages of these people?

{% lodash %}

var result=_.pluck(data, 'age')
return result
{% endlodash %}

<ul>
{% for  d1 in result %}
<li>
    THe age is {{d1}}
</li>
{% endfor %}
</ul>

### Q. What is the youngest age?

{% lodash %}
var result=_.pluck(data, 'age')
var min_age=_.min(result)

return min_age

{% endlodash %}

The youngest age is {{ result }}.

### Q. What is the oldest age?

{% lodash %}
var result=_.pluck(data, 'age')
var max_age= _.max(result)
return max_age
{% endlodash %}

The oldest age is {{ result }}.

### Q. Who is the youngest person?

{% lodash %}
// replace this code with your solution that uses lodash
// hint: use your previous solution with _.find
var result=_.pluck(data, 'age')
var min_age=_.min(result)
var y= _.find(data, {age: min_age})
return y 
{% endlodash %}

The youngest person is {{ result.name }}.
