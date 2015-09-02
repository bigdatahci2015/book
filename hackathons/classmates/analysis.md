# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}
var total_count = 0
for (i = 0; i < _.size(data.comments); i++) {
    var text = data.comments[i].body
    var search_string=  _.last(text.split('Food: '))
    var found_count = 0

    function splitString(stringToSplit, separator) {
        var arrayOfStrings = stringToSplit.split(separator)
        var j
        var count = 0

        for (j = 0; j < arrayOfStrings.length; j++) {
            if (arrayOfStrings[j] == "Sushi") { count++ }
        }
        return count
    }

    found_count = splitString(search_string, ' ')
    total_count += found_count
}
return total_count
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
var answer
for (i = 0; i < _.size(data.comments); i++) {
    var text = data.comments[i].body
    // console.log(text)

    var found_name

    function splitString(stringToSplit, separator) {
        var arrayOfStrings = stringToSplit.split(separator)
        var j
        var count = 0

        // console.log('The original string is: "' + stringToSplit + '"')
        // console.log('The separator is: "' + separator + '"')
        // console.log('The array has ' + arrayOfStrings.length + ' elements: ' + arrayOfStrings.join(' / '))

        var name = arrayOfStrings[0]
	// console.log(name)
        // console.log(_.last(name.split('Name:')))
        var language = arrayOfStrings[2]
	// console.log(language)
        // console.log(_.last(language.split(':')))

        if (_.last(language.split(':')) == " Python") {
            count++ 
            console.log("******* FOUND PYTHON *******")
	    return (_.last(name.split('Name:')))
        }
        else {
	    return 'false'
        }
    }

    found_name = splitString(text, '\r\n')

    if (found_name != 'false') {
        console.log('-----> ' + found_name)
        answer += found_name
    }
    console.log("====================================")
}
return "[answer]"
{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
return "[answer]"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
return "[answer]"
{% endlodash %}

Their names are {{result}}.
