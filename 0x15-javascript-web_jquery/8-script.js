$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  for (let x = 0; x < data.results.length; x++) {
    $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
  }
});
