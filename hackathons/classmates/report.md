{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# What percentage of the class are Computer Science students?

{% lodash %}
var total_count = 0
for (i = 0; i < _.size(data.comments); i++) {
    var text = data.comments[i].body
    var found_count = 0

    function splitString(stringToSplit, separator) {
        var arrayOfStrings = stringToSplit.split(separator)
        var department = arrayOfStrings[1]
        var count = 0

        if (_.last(department.split(':')) == " Computer Science") {
            count++
        }
        return count
    }

    found_count = splitString(text, '\r\n')
    total_count += found_count
}
return _.round( ( (total_count/_.size(data.comments)) * 100), 2)
{% endlodash %}

The percentage of CSCI-4830 students that are Computer Science majors is {{result}}%


# What are the favorite programming languages for the class participants?

{% lodash %}
var language_string = ""
for (i = 0; i < _.size(data.comments); i++) {
    var text = data.comments[i].body
    var languages

    function splitString(stringToSplit, separator) {
        var arrayOfStrings = stringToSplit.split(separator)
        var language_line = arrayOfStrings[2]
        var line = language_line.split(':')
        var favorite_language = line[1]
        var splitline = favorite_language.split(" ")

        if (favorite_language != "") {
            return (splitline[1])
        }
        else {
            return 'false'
        }
    }

    languages = splitString(text, '\r\n')
    if (languages == "JAVA") {languages = "Java"}
    language_string += (_.capitalize(languages) + ',')
}

var array = language_string.split(',')
var saved_array = language_string.split(',')
var new_array = array
var key = array[0].split()
var found_keys = key + ','

while (new_array.length > 1) {
    new_array = _.difference(array, key)
    array = new_array
    key = new_array[0].split()
    found_keys += (key + ',')
}

var sort_keys = found_keys.split(",")
var answer = ""

for (var i = 0; i < sort_keys.length; i++) {
    if (sort_keys[i] != "") {
    var count = 0
        for (var j = 0; j < saved_array.length; j++) {
            if(saved_array[j] == sort_keys[i]) { count++ }
        }
        answer += (sort_keys[i] + ':' + count + ' ')
    }
}

return answer
{% endlodash %}

The favorite CSCI-4830 programming languages are: {{result}}.


# How many students commented on the Introduction Issue before the first class?

{% lodash %}
count = 0
for (i = 0; i < _.size(data.comments); i++) {
    var class_start = "2015-08-24T22:00:00"
    var create_string = _.trimRight(data.comments[i].created_at, 'Z')
    var update_string = _.trimRight(data.comments[i].updated_at, 'Z')
    var CreateTime = new Date(create_string)
    var ClassTime = new Date(class_start)

    if( ( CreateTime.getTime() - ClassTime.getTime() ) > 0 ) { }
    else { count++ }
}
return count 
{% endlodash %}

The number of CSCI-4830 students that commented initially on the class list before class started is: {{result}}

# How many students have updated their initial Introduction comments?

{% lodash %}
count = 0
for (i = 0; i < _.size(data.comments); i++) {
    var create_string = _.trimRight(data.comments[i].created_at, 'Z')
    var update_string = _.trimRight(data.comments[i].updated_at, 'Z')

    var CreateTime = new Date(create_string)
    var UpdateTime = new Date(update_string)

    if( ( UpdateTime.getTime() - CreateTime.getTime() ) > 0 ) { count++ }
    else { }
}
return count 
{% endlodash %}

The number of CSCI-4830 students that updated/edited their initial forum comment is: {{result}}

