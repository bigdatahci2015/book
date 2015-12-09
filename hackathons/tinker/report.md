# Q: What are the number of commits?

## Data

|User name|Number of Commits|
|--|--|
|foober/blog|83|
|Michaeldfalleu/Git-radar|106|
|flarum/flarum|156|
|girlieMac/RPI-KittyCam|10|
|ChneuKircheu/Nq|68|
## Visualization

{% svg %}
{%set data=[["foober/blog", 83], ["Michaeldfalleu/Git-radar", 106], ["flarum/flarum", 156], ["girlieMac/RPI-KittyCam", 10], ["ChneuKircheu/Nq", 68]]%}
<!-- a barchart -->
<svg width="500" height="200">
{% for number in data %}
    <rect x="{{loop.index * 20}}" width="{{15}}" height="{{number[1]}}" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

{% endsvg %}


## Recommendation

I recommend to use svg framework, because it is easy to implement into markdown, and you generate visualization dynamically.
