$(document).ready(function(){

  //|
  //| convert external links
  //|
  $("a[href*='http://']:not([href*='"+location.hostname+"'])").attr("target","_blank");


  //|
  //| mobile slide nav
  //|

  $(".breadcrumb a.mobile").bind("touchstart, click", function(event){
    if ( $("body").hasClass("shift") )
    {
      $("body").removeClass("shift");
    }
    else
    {
      $("body").addClass("shift");
    }
    event.preventDefault();
  });

  $(document).bind("touchstart, click", function(){
    $("body").removeClass("shift");
  });

  $("nav.wrapper, .breadcrumb a.mobile").bind("touchstart, click", function(event){
    event.stopPropagation();
  });

});