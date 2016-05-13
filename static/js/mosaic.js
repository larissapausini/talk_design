$(document).ready(function() {
function getRandomSize(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}
  for (var i = 0; i < 10; i++) {
    var width = getRandomSize(230, 230);
    var height =  getRandomSize(200, 400);
    $('#photos').append('<img src="http://www.lorempixel.com/'+width+'/'+height+'/city" alt="London">');
  }
});
