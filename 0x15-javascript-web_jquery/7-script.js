$(document).ready(function () {
  $.get('https://swapi.co/api/people/5/?format=json', function (data) {
    $('div#character').append(data['name']);
  });
});
