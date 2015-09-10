# Q: What programming languages have the most packages?

## Data

* Manual collection of most popular languages from online sources

Table-1: Online search for most popular programming languages (basis)

| Rank | LangPop [1] | IEEE [2] | Udeny [3] | Mashable [4] | CodeDev [5] |
| -- | -- | -- | -- | -- | -- |
| 1 | Javascript | Java | C | Java | Python |
| 2 | Java | C | C++ | Javascript | Java |
| 3 | C | C++ | Java | C# | C++ |
| 4 | Objective C | Python | C# | PHP | C# |
| 5 | Python | C# | Objective C| C++ | Ruby |
| 6 | Ruby | R | PHP | Python | Javascript |
| 7 | C++ | PHP | Javascript | C | C |
| 8 | PHP | Javascript | Python | SQL | PHP |
| 9 | Shell | Ruby | SQL | Ruby | Go |
| 10 | C# | MatLab | Ruby | Objective C | Perl |

Table-1 Sources:

[1] http://langpop.com

[2] http://spectrum.ieee.org/computing/software/the-2015-top-ten-programming-languages

[3] https://blog.udemy.com/best-programming-language/

[4] http://mashable.com/2015/01/18/programming-languages-2015/

[5] http://blog.codeeval.com/codeevalblog/2015#.Vd8_tbR-lUh=



Table-2: Ranking (weighting) of most popular programming languages in Table-1

| Popularity Rank | Language | Weighting |
| -- | -- | -- |
| 1 | Java | 2 + 1 + 3 + 1 + 2 = 9 |
| 2 | C | 3 + 2 + 1 + 7 + 7 = 20 |
| T3 | Javascript | 1 + 8 + 7 + 2 + 6 = 24 |
| T3 | Python | 5 + 4 + 8 + 6 + 1 = 24 |
| 5 | C# | 10 + 5 + 4 + 3 + 4 = 26 |
| 6 | PHP | 8 + 7 + 6 + 4 + 8 = 33 |
| 7 | Ruby | 6 + 9 + 10 + 9 + 5 = 39 |


Table-3: Most programming packages (omitting C and C#)

| Rank | Language | # Packages [6] |
| -- | -- | -- |
| 1 | Javascript | 178450 |
| 2 | Java | 115568 |
| 3 | Ruby | 106600 |
| 4 | PHP | 68436 |
| 5 | Python | 65314 |

[6] http://www.modulecounts.com, accessed 27-August-2015


## Top five

{% svg %}

<!-- barchart with five bars -->
<rect x="0" width="20" height="178" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="30" width="20" height="115" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="60" width="20" height="106" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="90" width="20" height="68" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="120" width="20" height="65" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endsvg %}

## Top one

{% svg %}

<!-- same barchart, but the top is highlighted, using css -->
<rect x="0" width="20" height="178" style="fill:rgb(255,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="30" width="20" height="115" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="60" width="20" height="106" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="90" width="20" height="68" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="120" width="20" height="65" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endsvg %}
