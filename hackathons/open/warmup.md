{% data src="../fcq/fcq.clean.json" %}{% enddata %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}

var counts = _(data).groupBy('CrsPBAColl').map(function(group, name){
    return {
        name : name,
        count : group.length
    };
}).value();

var max = _(counts).pluck('count').max();
function computeWidth(d, i) {
    return d.count*(700/max);
}

var result = _.map(counts, function(count, i){
    return template({
        y : 25*i,
        width : count.count*(700/max),
        name : count.name
    });
})

return result.join('\n\n')

{% template %}

<rect y="${y}" height="20" width="${width}" style="fill:red;"/>
<text y="${y+15}" x="${width+10}">${name}</text>

{% endviz %}