# Q: What Frameworks have the highest GitHub Scores?

## Data

| Frameworks | GitHub Score | Stack Overflow Score | Overall Score|
| -- | -- | -- | -- |
| ASP.NET	| 	NA	| 100 | 100 |
| Ruby on Rails	| 95 | 	98	| 96 |
| AngularJS	| 100	| 93	| 96 |
| ASP.NET MVC | NA		| 93	| 93 |
| Django	| 89	| 92	| 90 |
| Laravel	| 91	| 81	| 86 |
| Meteor	| 95	| 76	| 85 |
| Spring	| 80	| 89	| 84 | 
| Express	| 92	| 77	| 84 |
| CodeIgniter	| 85	| 84	| 84 |

Notes: From hotframeworks.com 8/24/15 top 10 results
Github score: Based on the number of stars the git repository for a framework has on GitHub. (frameworks not on GitHub have a NA)
Stack Overflow score: Based on the number of questions on Stack Overflow that are tagged with the name of the framework.
Scores normalized 0-100

## Visualization - GitHub scores
ASP.NET and ASP.NET MVC scores set to 0 because not on GitHub.
{% set numbers = [0,95,100,0,89,91,95,80,92,85] %}
{% svg %}
<svg width="500" height="200">
{% set height = 200 %}
{% set stroke = 3 %}
{% for number in numbers %}
    <rect x="{{loop.index * 30}}" width="20" y="{{height - number-stroke}}" height="{{number}}" style="fill:rgb(0,0,255);stroke-width:{{stroke}};stroke:rgb(0,0,0)" />
{% endfor %}
</svg>
{% endsvg %}


## Recommendation

Based on GitHub popularity (stars) I would recommend using AngularJS, because it has the highest star score on GiHub. However, GitHub stars actually measures the number of times users of GitHub starred a repository, not actually how many times it was forked or used. Stars are a method for a GitHub user to bookmark a repository and show appreciation to the maintainer. But it is considered by GitHub to be a "measure of popularity".

While you asked for a recommendation based on popularity, I would not use that measure as the sole criterion for choosing a framework. Questions asked on the method page should also be considered when choosing a framework. 
