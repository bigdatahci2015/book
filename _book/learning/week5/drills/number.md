{% vizexercise %}

{% title %}

Display a number next to each bar

{% data %}

[{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 252812243}]

{% solution %}

function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i, scale) {
    
    return d.pop * scale;
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}

function computeLabel(d, i) {
    return d.pop
}

function computeLabelX(d, i, width) {
    
    return width+30;
}
var viz = _.map(data, function(d, i, data){
            var width = 300; // max desired width
            var maxPop = _.max(data,function(d){
                return d.pop;
                });
            var scale = width / maxPop.pop;
            
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i, scale),
                color: computeColor(d, i),
                label: computeLabel(d, i),
                labelx: computeLabelX(d,i,width)
            }
         })
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<g transform="translate(${d.x} ${d.y})">
<rect width="${d.width}"
     height="${d.height}"
     style="fill:${d.color};
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<text x="${d.labelx}" y="10">${d.label}</text>
</g>

{% output %}

<g transform="translate(0 0)">
<rect width="300"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<text x="330" y="10">1393783836</text>
</g>
<g transform="translate(0 20)">
<rect width="272.79736274685854"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<text x="330" y="10">1267401849</text>
</g>
<g transform="translate(0 40)">
<rect width="69.43322149418297"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<text x="330" y="10">322583006</text>
</g>
<g transform="translate(0 60)">
<rect width="54.415663993968145"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<text x="330" y="10">252812243</text>
</g>

{% endvizexercise %}
