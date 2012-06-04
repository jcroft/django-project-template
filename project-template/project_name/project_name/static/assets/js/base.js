$(document).ready(function() {

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