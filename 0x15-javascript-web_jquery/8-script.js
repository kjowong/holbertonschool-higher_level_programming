$(document).ready(function () {
  $.get('https://swapi.co/api/films?format=json', function (data) {
    for (let i = 0; i < data['results'].length; i++) {
      let title = data['results'][i]['title'];
      $('ul#list_movies').append('<li>' + title + '</li>');
    }
  });
});
