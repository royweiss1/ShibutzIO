$(document).ready(function() {
  var width = $(window).width();
  var height = $(window).height();

  function getRandomDirection() {
    return Math.random() < 0.5 ? -1 : 1;
  }

  function createMoving85() {
    var $moving85 = $('<div class="moving-85">85</div>');
    $moving85.css({
      top: Math.random() * height + 'px',
      left: Math.random() * width + 'px',
      transform: 'translate(' + getRandomDirection() + 'px, ' + getRandomDirection() + 'px)'
    });
    $('body').append($moving85);

    setInterval(function() {
      var currentTop = parseInt($moving85.css('top'), 10);
      var currentLeft = parseInt($moving85.css('left'), 10);
      var directionX = parseInt($moving85.css('transform').split(',')[4], 10);
      var directionY = parseInt($moving85.css('transform').split(',')[5], 10);

      if (currentTop <= 0 || currentTop >= height - 24) {
        directionY *= -1;
      }
      if (currentLeft <= 0 || currentLeft >= width - 14) {
        directionX *= -1;
      }

      $moving85.css({
        top: currentTop + directionY + 'px',
        left: currentLeft + directionX + 'px',
        transform: 'translate(' + directionX + 'px, ' + directionY + 'px)'
      });
    }, 10);
  }

  // Create multiple instances of moving "85"
  for (var i = 0; i < 85; i++) {
    createMoving85();
  }
});
