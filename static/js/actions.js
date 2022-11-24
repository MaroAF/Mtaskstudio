
$(document).ready(function () {
  AOS.init();
  $(window).scroll(function () {
    $(".eapps-link").css("display", "none")
    if ($(window).scrollTop() > 130) {
      $(".main-menu").addClass("fix-pos");
    } else {
      $(".main-menu").removeClass("fix-pos");
    }
  });

  if ($('#exampleModalToggle').data('bs.modal').isShow == true) {
    console.log("Modal is open");
  }


});


$(".carousel-item:first").addClass("active")
$(".Bar-slide:first").addClass("active")

$('.b-game-card').hover(function () {
  $(this).find('.text-card').css({ "transform": "translateY(0%)" });
}, function () {
  $(this).find('.text-card').css({ "transform": "translateY(100%)" });
});


$("#song-1").click(function () {
  if ($("#item-1").is(':checked')) {
    $("#song-1 a").css("pointer-events", "none")
  }
  else {
    $("#song-1 a").css("pointer-events", "auto")
    $("#song-2 a").css("pointer-events", "none")
    $("#song-3 a").css("pointer-events", "none")
  }
});
$("#song-2").click(function () {
  if ($("#item-2").is(':checked')) {
    $("#song-2 a").css("pointer-events", "none")
  }
  else {
    $("#song-2 a").css("pointer-events", "auto")
    $("#song-1 a").css("pointer-events", "none")
    $("#song-3 a").css("pointer-events", "none")
  }
});
$("#song-3").click(function () {
  if ($("#item-3").is(':checked')) {
    $("#song-3 a").css("pointer-events", "none")
  }
  else {
    $("#song-3 a").css("pointer-events", "auto")
    $("#song-1 a").css("pointer-events", "none")
    $("#song-2 a").css("pointer-events", "none")
  }
});

// document.addEventListener('keydown', (event) => {
//   if (event.key == "ArrowRight") {
//     $(".next-btn-modal").trigger('click');
//   }
//   if (event.key == "ArrowLeft") {
//     $(".prev-btn-modal").trigger('click');
//   }

// }, false);