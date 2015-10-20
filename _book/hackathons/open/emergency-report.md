{% data src="emergency.json" %}
{% enddata %}

# What borough has the highest number incidents?

{% lodash %}
return _.chain(data)
        .groupBy(function(obj) { return obj["Conditions: Sky"]; })
        .mapValues(function(arr) { return arr.length; })
        .value();
{% endlodash %}

{{ result | json }}
