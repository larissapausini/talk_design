$(document).ready(function() {
function getRandomSize(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}
  for (var i = 0; i < 5; i++) {
    var width = getRandomSize(260, 555);
    var height =  getRandomSize(200, 500);
    $('#photos').append('<img src="http://www.lorempixel.com/'+width+'/'+height+'/city" alt="London">');
  }
});
