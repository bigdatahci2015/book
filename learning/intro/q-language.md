# Q: Which programming language is the top favorite among the students in our class?

## Data

* Manually gather data and make a table in Markdown


| Language | # of Students |
| -- | -- |
| JS | 3 |
| Python | 8 | 
| C | 3 | 
| Java | 3 | 
| Haskell | 1 | 
| C++ | 2 | 
| C# | 1 | 



## Answer

Python is most popular programming language

## Visualization

* Create a barchart using SVG

{% svg %}

{% set numbers = [3,8,3,3,1,2,1] %}

* Below should be a bar chart to display the data: {{ numbers }}
* There should be some gaps between the bars.

<svg width="500" height="200">
{% set height = 200 %}
{% set stroke = 3 %}
{% for number in numbers %}
    <rect x="{{loop.index * 30}}" width="20" y="{{height - (number*height/10)-stroke}}" height="{{number*height/10}}" style="fill:rgb(0,0,255);stroke-width:{{stroke}};stroke:rgb(0,0,0)" />
{% endfor %}
</svg>


{% endsvg %}
