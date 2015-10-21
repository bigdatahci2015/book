

## Q. When did the user 'grahamannett' leave a comment?
{% import "/home/sushant/Desktop/HCIBIGDATA2015/book/learning/week1/data.html" as sushant  %}
{% set data = sushant.comments %}


{% lodash %}

var result= _.find(data, {url: "https://api.github.com/repos/bigdatahci2015/forum/issues/comments/133358653"})
return result
{% endlodash %}

The result is {{ result.created_at}}.
