$(document).ready(function () {
  $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json%20The%20wind%20speed%20must%20be%20display%20in%20the%20HTML%20tag%20DIV#sf_wind_speed', function (data) {
    let speed = $(data).find('channel').find('yweather\\:wind').attr('speed');
    $('div#sf_wind_speed').text(speed);
  });
});
