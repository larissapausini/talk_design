$(document).ready(function() {
function getRandomSize(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}
  for (var i = 0; i < 10; i++) {
    var width = getRandomSize(231, 231);
    var height =  getRandomSize(150, 340);
    $('#photos').append('<img src="http://www.lorempixel.com/'+width+'/'+height+'/city" alt="London">');
  }
});
