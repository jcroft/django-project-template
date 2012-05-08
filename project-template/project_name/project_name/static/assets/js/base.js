$(document).ready(function() {

  // Convert media elements to JS players.
  $('video,audio').mediaelementplayer({
    audioWidth: 260,
    flashName: '/static/assets/js/plugins/flashmediaelement.swf'
  });

  // Hide messages after twenty seconds.
  setTimeout(function() {
    $("#messages").slideUp('slow');
  }, 20000);

  if (window.navigator.standalone) {
    $('a').live('click', function(e){
      e.preventDefault();
      window.location = $(this).attr("href");
    });
  }

});