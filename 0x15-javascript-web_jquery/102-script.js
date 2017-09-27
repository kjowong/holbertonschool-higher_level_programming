$(document).ready(function () {
  $('input#btn_search').on('click', function () {
    let cityName = $('input#city_search').val();
    let url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + cityName + '%22)&format=json';
    $.get(url, function (data) {
      let speed = data['query']['results']['channel']['wind']['speed'];
      $('div#wind_speed').text(speed);
    });
  });
});
