{% data src="birdstrike.json" %}
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

# What type of aircraft has the most instances of damaged caused by bird strikes? by (nicolele)

{% lodash %}
var filter=_.filter(data, function(air){
	return air['Effect: Indicated Damage'] == "Caused damage"
})
var groups=_.groupBy(filter, function(air){
	return air['Aircraft: Type']
})
var maxGroups=_.mapValues(groups, function(g){
	return _.size(g)
})
var maxType=_.pick(maxGroups, function(g){
	return g == _.max(maxGroups)
})
return maxType
{% endlodash %}
{{result | json}}

# What are the top 5 bird species that are involved? (ZachLamb)

{% lodash %}
/*var filter=_.filter(data, function(air){
	return !_.includes(air['Wildlife: Species'], "Unknown bird")
})*/
var groups=_.groupBy(data, function(air){
	return air['Wildlife: Species']
})
var countGroup=_.mapValues(groups, function(g){
	return _.size(g)
})
var keys=_.keys(countGroup)
var list=_.map(keys, function(key){
	return {"name": key, "count": countGroup[key]}
})

return _.sortBy(list, function(e){
	return e["count"]
}).reverse()
{% endlodash %}
<table>
	<tr>
		<th>Name</th>
		<th>Count</th>
	</tr>
{% for value in result %}
    <tr>
        <td>{{value['name']}}</td>
        <td>{{value['count']}}</td>
    </tr>
{% endfor %}
</table>


# What is the most common flight phase where a birdstrike occurred? by (KevinKGifford)

{% lodash %}
var groups=_.groupBy(data, function(air){
	return air['When: Phase of flight']
})
var countGroup=_.mapValues(groups, function(g){
	return _.size(g)
})
var keys=_.keys(countGroup)
var list=_.map(keys, function(key){
	return {"Phase": key, "Count": countGroup[key]}
})
return list
{% endlodash %}
<table>
	<tr>
		<th>Phase</th>
		<th>Count</th>
	</tr>
{% for value in result %}
    <tr>
        <td>{{value['Phase']}}</td>
        <td>{{value['Count']}}</td>
    </tr>
{% endfor %}
</table>

# How many flights have been cancelled by birdstrikes? by (pail4944)

{% lodash %}
var filter=_.filter(data, function(air){
	return air['Effect: Impact to flight'] != "None" && air['Effect: Impact to flight'] != ""
})
var groups=_.groupBy(filter, function(air){
	return air['Effect: Impact to flight']
})
var countGroup=_.mapValues(groups, function(g){
	return _.size(g)
})
var keys=_.keys(countGroup)
var list=_.map(keys, function(key){
	return {"Impact": key, "Count": countGroup[key]}
})
return list
{% endlodash %}
<table>
	<tr>
		<th>Impact</th>
		<th>Count</th>
	</tr>
{% for value in result %}
    <tr>
        <td>{{value['Impact']}}</td>
        <td>{{value['Count']}}</td>
    </tr>
{% endfor %}
</table>

# What states cost the airlines the most money?(Cost and location) by willzfarmer

{% lodash %}

var groups=_.groupBy(data, function(air){
	return air['Origin State']
})
var sumGroup=_.mapValues(groups, function(g){
	return _.sum(g, function(e){
		return e['Cost: Total $']
	})
})
var keys=_.keys(sumGroup)
var list=_.map(keys, function(key){
	return {"State": key, "Total cost $": sumGroup[key]}
})
return _.sortBy(list, function(e){
	return e["Total cost $"]
}).reverse()
{% endlodash %}
<table>
	<tr>
		<th>State</th>
		<th>Total cost $</th>
	</tr>
{% for value in result %}
    <tr>
        <td>{{value['State']}}</td>
        <td>{{value['Total cost $']}}</td>
    </tr>
{% endfor %}
</table>
