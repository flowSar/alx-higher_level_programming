
$(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        results = data['results'];
        for (const result of results) {
            $('#list_movies').append(`<li>${result['title']}</li>`)
        }
    })
});
