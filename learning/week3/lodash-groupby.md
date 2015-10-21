# Lodash GroupBy

In this section, you will learn to utilize Lodash `_.groupBy` to perform some simple
aggregate analysis.

Some of the Lodash functions you will use are:

* [_.groupBy](https://lodash.com/docs#groupBy)
* [_.keys](https://lodash.com/docs#keys)
* [_.mapValues](https://lodash.com/docs#mapValues)

First, study the working examples below carefully. Then, complete the exercises that follow.

## Examples

{% lodashexercise %}

{% title %}

Group people by age (teens, 20s, 30s, 40s, 50s)

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{"1":[{"name":"Peter Pan","age":15}],"3":[{"name":"Kelly Fan","age":35},{"name":"Ben Smith","age":35}],"4":[{"name":"Mary Smith","age":42},{"name":"Adam Potts","age":42},{"name":"Joe Johnson","age":46}],"5":[{"name":"John Smith","age":54}]}

{% solution %}

var result = _.groupBy(data, function(d){
        return Math.floor(d.age / 10)    
    })
return result

{% endlodashexercise %}






{% lodashexercise %}

{% title %}

What are the age groups?

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

["1","3","4","5"]

{% solution %}

var groups = _.groupBy(data, function(d){
        return Math.floor(d.age / 10)    
    })

var result = _.keys(groups)
return result

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

How many people are in each age group?

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{"1":1,"3":2,"4":3,"5":1}

{% solution %}

var groups = _.groupBy(data, function(d){
        return Math.floor(d.age / 10)    
    })

var result = _.mapValues(groups, function(value){
        return value.length
    })
return result

{% endlodashexercise %}



## Exercises


{% lodashexercise %}

{% title %}

Who is the first person in each age group?

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{"1":"Peter Pan","3":"Kelly Fan","4":"Mary Smith","5":"John Smith"}

{% solution %}
var groups = _.groupBy(data, function(d){
        return Math.floor(d.age / 10)    
    })
var result = _.mapValues(groups, function(value){
        return _.first(value).name;
    })
return result

{% endlodashexercise %}


{% lodashexercise %}

{% title %}

Group people by their last name

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{
  "Smith": [
    {
      "name": "John Smith",
      "age": 54
    },
    {
      "name": "Mary Smith",
      "age": 42
    },
    {
      "name": "Ben Smith",
      "age": 35
    }
  ],
  "Pan": [
    {
      "name": "Peter Pan",
      "age": 15
    }
  ],
  "Fan": [
    {
      "name": "Kelly Fan",
      "age": 35
    }
  ],
  "Potts": [
    {
      "name": "Adam Potts",
      "age": 42
    }
  ],
  "Johnson": [
    {
      "name": "Joe Johnson",
      "age": 46
    }
  ]
}

{% solution %}
var groups = _.groupBy(data, function(d){
  var nameArr = _.words(d.name);
  var lastName = _.rest(nameArr).join(' ');
  return lastName;
    })

return groups;

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

How many people are in each last-name group?

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{
  "Smith": 3,
  "Pan": 1,
  "Fan": 1,
  "Potts": 1,
  "Johnson": 1
}

{% solution %}

var groups = _.groupBy(data, function(d){
  var nameArr = _.words(d.name);
  var lastName = _.rest(nameArr).join(' ');
  return lastName;
    })

var result = _.mapValues(groups, function(value){
        return value.length
    })
return result
{% endlodashexercise %}






{% lodashexercise %}

{% title %}

Who is the first person in each last-name group?

{% data %}

[{name: 'John Smith', age: 54},
 {name: 'Mary Smith', age: 42},
 {name: 'Peter Pan', age: 15},
 {name: 'Kelly Fan', age: 35},
 {name: 'Adam Potts', age: 42},
 {name: 'Joe Johnson', age: 46},
 {name: 'Ben Smith', age: 35}]

{% output %}

{
  "Smith": "John Smith",
  "Pan": "Peter Pan",
  "Fan": "Kelly Fan",
  "Potts": "Adam Potts",
  "Johnson": "Joe Johnson"
}

{% solution %}
var groups = _.groupBy(data, function(d){
  var nameArr = _.words(d.name);
  var lastName = _.rest(nameArr).join(' ');
  return lastName;
    })
var result = _.mapValues(groups, function(value){
        return _.first(value).name;
    })
return result

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

What are all person-favorite pairs?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel']},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening']},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming']},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food']},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music']},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming']}]

{% output %}

[
  {
    "name": "John Smith",
    "favorite": "food"
  },
  {
    "name": "John Smith",
    "favorite": "travel"
  },
  {
    "name": "Mary Smith",
    "favorite": "sports"
  },
  {
    "name": "Mary Smith",
    "favorite": "travel"
  },
  {
    "name": "Peter Pan",
    "favorite": "movies"
  },
  {
    "name": "Peter Pan",
    "favorite": "tv"
  },
  {
    "name": "Peter Pan",
    "favorite": "gardening"
  },
  {
    "name": "Kelly Fan",
    "favorite": "movies"
  },
  {
    "name": "Kelly Fan",
    "favorite": "travel"
  },
  {
    "name": "Kelly Fan",
    "favorite": "programming"
  },
  {
    "name": "Adam Potts",
    "favorite": "sports"
  },
  {
    "name": "Adam Potts",
    "favorite": "food"
  },
  {
    "name": "Joe Johnson",
    "favorite": "tv"
  },
  {
    "name": "Joe Johnson",
    "favorite": "sports"
  },
  {
    "name": "Joe Johnson",
    "favorite": "music"
  },
  {
    "name": "Ben Smith",
    "favorite": "movies"
  },
  {
    "name": "Ben Smith",
    "favorite": "tv"
  },
  {
    "name": "Ben Smith",
    "favorite": "programming"
  }
]

{% solution %}

// hint: use nested _.map, then  _.flatten
// hint: use nested _.map, then  _.flatten
var pairs = _.map(data, function(d){
  var favpairs = _.map(d.favorites, function(f){
    return {name:d.name,favorite:f};
  });
  return favpairs;
});
return _.flatten(pairs);

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

What are all age-favorite pairs (in ascending order)?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel']},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening']},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming']},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food']},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music']},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming']}]

{% output %}

[
  {
    "age": 15,
    "favorite": "movies"
  },
  {
    "age": 15,
    "favorite": "tv"
  },
  {
    "age": 15,
    "favorite": "gardening"
  },
  {
    "age": 35,
    "favorite": "movies"
  },
  {
    "age": 35,
    "favorite": "travel"
  },
  {
    "age": 35,
    "favorite": "programming"
  },
  {
    "age": 35,
    "favorite": "movies"
  },
  {
    "age": 35,
    "favorite": "tv"
  },
  {
    "age": 35,
    "favorite": "programming"
  },
  {
    "age": 42,
    "favorite": "sports"
  },
  {
    "age": 42,
    "favorite": "travel"
  },
  {
    "age": 42,
    "favorite": "sports"
  },
  {
    "age": 42,
    "favorite": "food"
  },
  {
    "age": 46,
    "favorite": "tv"
  },
  {
    "age": 46,
    "favorite": "sports"
  },
  {
    "age": 46,
    "favorite": "music"
  },
  {
    "age": 54,
    "favorite": "food"
  },
  {
    "age": 54,
    "favorite": "travel"
  }
]

{% solution %}

var ageSorted = _.sortBy(data,'age');
var pairs = _.map(ageSorted, function(d){
  var favpairs = _.map(d.favorites, function(f){
    return {age:d.age,favorite:f};
  });
  return favpairs;
});
return _.flatten(pairs);

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

Group people by their favorites.

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel']},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening']},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming']},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food']},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music']},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming']}]

{% output %}

{
  "food": [
    {
      "name": "John Smith",
      "favorite": "food"
    },
    {
      "name": "Adam Potts",
      "favorite": "food"
    }
  ],
  "travel": [
    {
      "name": "John Smith",
      "favorite": "travel"
    },
    {
      "name": "Mary Smith",
      "favorite": "travel"
    },
    {
      "name": "Kelly Fan",
      "favorite": "travel"
    }
  ],
  "sports": [
    {
      "name": "Mary Smith",
      "favorite": "sports"
    },
    {
      "name": "Adam Potts",
      "favorite": "sports"
    },
    {
      "name": "Joe Johnson",
      "favorite": "sports"
    }
  ],
  "movies": [
    {
      "name": "Peter Pan",
      "favorite": "movies"
    },
    {
      "name": "Kelly Fan",
      "favorite": "movies"
    },
    {
      "name": "Ben Smith",
      "favorite": "movies"
    }
  ],
  "tv": [
    {
      "name": "Peter Pan",
      "favorite": "tv"
    },
    {
      "name": "Joe Johnson",
      "favorite": "tv"
    },
    {
      "name": "Ben Smith",
      "favorite": "tv"
    }
  ],
  "gardening": [
    {
      "name": "Peter Pan",
      "favorite": "gardening"
    }
  ],
  "programming": [
    {
      "name": "Kelly Fan",
      "favorite": "programming"
    },
    {
      "name": "Ben Smith",
      "favorite": "programming"
    }
  ],
  "music": [
    {
      "name": "Joe Johnson",
      "favorite": "music"
    }
  ]
}

{% solution %}

// hint: first, apply _.groupBy to the name-favovrite pairs computed earlier
var pairs = _.map(data, function(d){
  var favpairs = _.map(d.favorites, function(f){
    return {name:d.name,favorite:f};
  });
  return favpairs;
});

var flpairs  = _.flatten(pairs);

var groups = _.groupBy(flpairs, function(d){
        return d.favorite;  
    })

return groups;

{% endlodashexercise %}






{% lodashexercise %}

{% title %}

What are the names of the people in these 'favorite' groups?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel']},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening']},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming']},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food']},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music']},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming']}]

{% output %}

{
  "food": [
    "John Smith",
    "Adam Potts"
  ],
  "travel": [
    "John Smith",
    "Mary Smith",
    "Kelly Fan"
  ],
  "sports": [
    "Mary Smith",
    "Adam Potts",
    "Joe Johnson"
  ],
  "movies": [
    "Peter Pan",
    "Kelly Fan",
    "Ben Smith"
  ],
  "tv": [
    "Peter Pan",
    "Joe Johnson",
    "Ben Smith"
  ],
  "gardening": [
    "Peter Pan"
  ],
  "programming": [
    "Kelly Fan",
    "Ben Smith"
  ],
  "music": [
    "Joe Johnson"
  ]
}

{% solution %}
var pairs = _.map(data, function(d){
  var favpairs = _.map(d.favorites, function(f){
    return {name:d.name,favorite:f};
  });
  return favpairs;
});

var flpairs  = _.flatten(pairs);

var groups = _.groupBy(flpairs, function(d){
        return d.favorite;  
    });

var result =  _.mapValues(groups, function(d) {
  var names = _.pluck(d,'name') 
  return names; 
});

return result;


{% endlodashexercise %}



{% lodashexercise %}

{% title %}

What are the sizes of these 'favorite' groups?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel']},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening']},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming']},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food']},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music']},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming']}]

{% output %}

{
  "food": 2,
  "travel": 3,
  "sports": 3,
  "movies": 3,
  "tv": 3,
  "gardening": 1,
  "programming": 2,
  "music": 1
}

{% solution %}
var pairs = _.map(data, function(d){
  var favpairs = _.map(d.favorites, function(f){
    return {name:d.name,favorite:f};
  });
  return favpairs;
});

var flpairs  = _.flatten(pairs);

var groups = _.groupBy(flpairs, function(d){
        return d.favorite;  
    });

var result =  _.mapValues(groups, function(d) {
  
  return d.length; 
});

return result;


{% endlodashexercise %}






{% lodashexercise %}

{% title %}

Group people by city

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel'], city: 'Denver'},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel'], city: 'Boulder'},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening'], city: 'Denver'},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming'], city: 'Boulder'},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food'], city: 'Denver'},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music'], city: 'Denver'},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming'], city: 'Boulder'}]

{% output %}

{
  "Denver": [
    {
      "name": "John Smith",
      "age": 54,
      "favorites": [
        "food",
        "travel"
      ],
      "city": "Denver"
    },
    {
      "name": "Peter Pan",
      "age": 15,
      "favorites": [
        "movies",
        "tv",
        "gardening"
      ],
      "city": "Denver"
    },
    {
      "name": "Adam Potts",
      "age": 42,
      "favorites": [
        "sports",
        "food"
      ],
      "city": "Denver"
    },
    {
      "name": "Joe Johnson",
      "age": 46,
      "favorites": [
        "tv",
        "sports",
        "music"
      ],
      "city": "Denver"
    }
  ],
  "Boulder": [
    {
      "name": "Mary Smith",
      "age": 42,
      "favorites": [
        "sports",
        "travel"
      ],
      "city": "Boulder"
    },
    {
      "name": "Kelly Fan",
      "age": 35,
      "favorites": [
        "movies",
        "travel",
        "programming"
      ],
      "city": "Boulder"
    },
    {
      "name": "Ben Smith",
      "age": 35,
      "favorites": [
        "movies",
        "tv",
        "programming"
      ],
      "city": "Boulder"
    }
  ]
}
{% solution %}
var groups = _.groupBy(data, function(d){
        return d.city;  
    });
return groups;

{% endlodashexercise %}






{% lodashexercise %}

{% title %}

Group people by city and count how many people in each city

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel'], city: 'Denver'},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel'], city: 'Boulder'},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening'], city: 'Denver'},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming'], city: 'Boulder'},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food'], city: 'Denver'},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music'], city: 'Denver'},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming'], city: 'Boulder'}]

{% output %}

{
  "Denver": 4,
  "Boulder": 3
}

{% solution %}
var groups = _.groupBy(data, function(d){
        return d.city;  
    });
var result =  _.mapValues(groups, function(d) {
  
  return _.size(d); 
});

return result;

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

What is the oldest age in each city?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel'], city: 'Denver'},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel'], city: 'Boulder'},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening'], city: 'Denver'},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming'], city: 'Boulder'},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food'], city: 'Denver'},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music'], city: 'Denver'},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming'], city: 'Boulder'}]

{% output %}

{
  "Denver": 54,
  "Boulder": 42
}

{% solution %}
var groups = _.groupBy(data, function(d){
        return d.city;  
    });
var result =  _.mapValues(groups, function(d) {
  var largest = _.reduce(_.pluck(d, 'age'), function(largest,n) {
    return largest >= n? largest: n
  })
  return largest
});

return result;


{% endlodashexercise %}





{% lodashexercise %}

{% title %}

How many Smith's are in each city?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'travel'], city: 'Denver'},
 {name: 'Mary Smith', age: 42, favorites: ['sports', 'travel'], city: 'Boulder'},
 {name: 'Peter Pan', age: 15, favorites: ['movies', 'tv', 'gardening'], city: 'Denver'},
 {name: 'Kelly Fan', age: 35, favorites: ['movies', 'travel', 'programming'], city: 'Boulder'},
 {name: 'Adam Potts', age: 42, favorites: ['sports', 'food'], city: 'Denver'},
 {name: 'Joe Johnson', age: 46, favorites: ['tv', 'sports','music'], city: 'Denver'},
 {name: 'Ben Smith', age: 35, favorites: ['movies', 'tv', 'programming'], city: 'Boulder'}]

{% output %}

{
  "Denver": 1,
  "Boulder": 2
}

{% solution %}
var groups = _.groupBy(data, function(d){
        return d.city;  
    });

var result =  _.mapValues(groups, function(d) {
  var names = _.pluck(d, 'name');
  var smithNames = _.partition(names, function(name) {
    var nameArr = _.words(name);
    var lastName = _.last(nameArr);
    return (lastName == 'Smith') 
  });
  return smithNames[0].length;
});

return result;

{% endlodashexercise %}
