{% data src="../../bs.json" %}
{% enddata %}

# Report

As a team, answer a subset of the questions submitted during the hackathon.
But instead of using Tableau, you will need to write Javascript/Lodash code
to derive your answers. Similar to before, each team member is responsible for
one question. But everyone should work together to come up with a good solution.
Your answer should consist of Lodash code and a brief writeup.
Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not se any for loop.

This time, the data is not already prepared for you in a nice JSON format. You
will need to do it on your own, replacing the placeholder `birdstrike.json` with
real data.

# Which airlines have the worst luck with birdstrikes in terms of damage caused? 
This question was asked by (calebhsu).

{% lodash %}
var groups = _.groupBy(data, function(n) {
    return n['Aircraft: Airline/Operator'];
});
var i = 0;
var costs = _.mapValues(groups, function(d){
    var total = _.reduce(d, function(total,e){
        // some of the costs are in quotes and have commas...
        var cost = e['Cost: Total $'];
        if (_.isString(cost)){
            // remove commas
            var temp1 = cost.replace(/,/g,'');
            var temp2 = _.parseInt(temp1);
            cost = temp2;
        }
        return total+cost;
    },0);
    return total;
    
});

var sorted = _.sortBy(_.pairs(costs), function(d) {
    return d[1];
});
var desc = _(sorted).reverse().value()
return _.slice(desc,0,10);

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


# What is the most common flight phase where a birdstrike occurred?
This question was asked by (KevinKGifford).

{% lodash %}

var group = _.groupBy(data,function(n){
	return n["When: Phase of flight"]
})

var result = _.mapValues(group,function(n){
	return _.map(n,function(d){
		return d["When: Phase of flight"]
	}).length
})


return result
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


# What airports have the most expensive average accident?

This question was asked by (satchelspencer ).

{% lodash %}

var groups = _.groupBy(data, function(n) {
    return n['Airport: Name'];
});
var i = 0;
var costs = _.mapValues(groups, function(d){
    var avg = _.reduce(d, function(total,e){
        // some of the costs are in quotes and have commas...
        var cost = e['Cost: Total $'];
        if (_.isString(cost)){
            // remove commas and convert to int
            var temp1 = cost.replace(/,/g,'');
            cost = _.parseInt(temp1);           
        }
        return total+cost;
    },0)/_.size(d);
    return avg;
}); 
var sorted = _.sortBy(_.pairs(costs), function(d) {
    return d[1];
});
var desc = _(sorted).reverse().value()
return _.slice(desc,0,10);
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# Which plane strikes the most birds?

This question was asked by (twagar95).

{% lodash %}
var groups = _.groupBy(data, function(n) {
    return n['Aircraft: Make/Model'];
});

var counts = _.mapValues(groups, function(d){
    return d.length;
});

var sorted = _.sortBy(_.pairs(counts), function(d) {
    return d[1];
});

var desc = _(sorted).reverse().value()

return _.slice(desc, 0,10);
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>


# What state had the highest number of bird strikes? (Departure State)

This question was asked by (drewdinger).

{% lodash %}
var grps = _.groupBy(data, 'Origin State')

var map = _.mapValues(grps, function(d){
    return d.length
})

var newvar = _.map(map, function(v,k){
	return {"state": k, "count":v}
})

_.remove(newvar, function(n){
 	return n.state == 'N/A'	
})
var sorted = _.sortBy(newvar, "count").reverse()
return _.slice(sorted,0,10)
{% endlodash %}

{{ data | json }}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>