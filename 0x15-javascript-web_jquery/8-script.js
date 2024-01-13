$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  data.results.forEach(function (entry) {
    $('ul#list_movies').append('<li>' + entry.title + '</li>');
  });
});
