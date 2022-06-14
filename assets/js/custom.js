/*-----------------------------------------------------------
 * Template Name    : DESIGN - Fully Responsive Personal Template
 * Author           : TOONALITE Group
 * Version          : 1.0.0
 * Created          : SEPTEMBER 2021
 * File Description : Main JQuery file of the template
 *------------------------------------------------------------*/


//repeated variables
var $window = $(window);
var $root = $('html,body');

$(document).ready(function() {
    CloseMenu();
    activemenu();
    themeOption();
    smoothScroll();
    portfolioPopup();
    portfolioIsotop();
    videoPopup();
    // map();

});


$window.on("load", (function() {
    preloader();
    HeaderSticky();
    portfolioIsotop();
}));

$window.on('scroll', function() {
    countUp();
    skills();
    returnUp();
    HeaderSticky();
    // map();
    
});

/*-----------------------------------------------------------------------------
                                   FUNCTIONS
-----------------------------------------------------------------------------*/
/*-------------------------
    PRELOADER
-------------------------*/
function preloader() {
    "use strict";
    $(".preloader").delay(2000).fadeOut('slow');
    $(".loader").delay(2000).fadeOut('slow');
}
/*-------------------------
     Header Sticky
-------------------------*/
function HeaderSticky() {
    if ($window.scrollTop() > 10) {
        $('.nav-pills').addClass('header-sticky');
    } else {
        $('.nav-pills').removeClass('header-sticky');
    }
}
/*-------------------------
    CLOSE MENU
-------------------------*/
function CloseMenu() {
    $('.close-menu').click( function(){
        if($(this).closest('#navbarSupportedContent').hasClass('show')){
            $(this).closest('#navbarSupportedContent').removeClass('show');
        }
        else{
            $(this).closest('#navbarSupportedContent').addClass('show');
        }
       
    });
}

/*-------------------------
        Theme Option
-------------------------*/
function themeOption() {

    "use strict";

    $("ul.pattern .color1").on('click', function() {
        return $("#option-color").attr("href", "assets/css/color/purple.css"), !1
    });
    $("ul.pattern .color2").on('click', function() {
        return $("#option-color").attr("href", "assets/css/color/blue.css"), !1
    });
    $("ul.pattern .color3").on('click', function() {
        return $("#option-color").attr("href", "assets/css/color/orange.css"), !1
    });
    $("ul.pattern .color4").on('click', function() {
        return $("#option-color").attr("href", "assets/css/color/green.css"), !1
    });
    $("#color-switcher .pallet-button").on('click', function() {
        return $("#color-switcher .color-pallet").toggleClass('show'), !1
    })

}
/*-------------------------
  Testimonial CAROUSEL JS
-------------------------*/
(function () {
    "use strict";
  
    var carousels = function () {
      $(".owl-carousel1").owlCarousel({
        loop: true,
        autoplay: false,
        center: true,
        margin: 0,
        responsiveClass: true,
        nav: false,
        responsive: {
          0: {
            items: 1,
            nav: false
          },
          680: {
            items: 2,
            nav: false,
            loop: false
          },
          1000: {
            items: 3,
            nav: true
          }
        }
      });
    };
  
    (function () {
      carousels();
    })(jQuery);
  })();

/*-------------------------
         active
-------------------------*/
function activemenu() {
    "use strict";
    $('a.nav-link').click( function() {
        $('a.nav-link').removeClass('active');
        $(this).addClass('active');
    });
}


/*-------------------------
       SMOOTH SCROLL
-------------------------*/
function smoothScroll() {
    "use strict";
    $(window).on('scroll', function() {
        $('section[id]').each(function(index, elem) {
             $(elem).on('appear',function() {
                const elemId = $(elem).attr('id');
                $(" a.nav-link.active").removeClass('active');
                $(" a[href='#" + elemId + "']").addClass('active');
            });
        });
    });
    $('a.nav-link[href^="#"]').click(function() {
        var href = $.attr(this, 'href');
    
        $root.animate({
            scrollTop: $(href).offset().top - 55
        }, 1000)
        return false;
    });
}

/*-------------------------
         Count Up
-------------------------*/
function countUp() {
    "use strict";
    var scroll = $window.scrollTop();
    var countId = $('#count-up');
    if (countId.length) {
        var winH = $window.height(),
            countOffset = countId.offset().top;
        if (scroll + winH > countOffset) {
            $('.timer').countTo();
            $('.count-number').removeClass('timer');
        }
    }
}

/*-------------------------
       PopUP Video
-------------------------*/
function videoPopup() {
    "use strict";
    if ($('.video').length > 0) {
        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }
}



/*-------------------------
      Portfolio Popup
-------------------------*/
function portfolioPopup() {
    "use strict";
    if ($('.portfolio-items').length > 0) {
        $('.portfolio-items').each(function() {
            $(this).magnificPopup({
                delegate: '.js-zoom-gallery',
                type: 'image',
                gallery: {
                    enabled:true
                }
            });
        });
    }
}

/*-------------------------
        Portfolio JS
-------------------------*/
function portfolioIsotop() {
    "use strict";
    if ($('.portfolio').length > 0) {
    
        var $pfilter = $('#portfolio-filter');
        var $pgrid = $('.portfolio-items');
        $pgrid.isotope({
            itemSelector: '.portfolio-item',
            layoutMode: 'masonry',
            isOriginLeft: false,
        });
        $pfilter.find('a').on("click",function() {
            var filterValue = $(this).attr('data-filter');
            $pfilter.find('a').removeClass('active');
            $(this).addClass('active');
            $pgrid.isotope({
                filter: filterValue,
            });
            updateFilterCounts();
            return false;
        });
        function updateFilterCounts() {
            var itemElems = $pgrid.isotope('getFilteredItemElements');
            if ($('.portfolio-item').hasClass('visible_item')) {
                $('.portfolio-item').removeClass('visible_item');
            }
            var index = 0;
            $(itemElems).each(function() {
                if (index >= initial_items) {
                    $(this).addClass('visible_item');
                }
                index++;
            });
            $pgrid.isotope('layout');
        }
    }
}
/*-------------------------
            skills
-------------------------*/
function skills() {
  "use strict";
  var scroll = $window.scrollTop();
  var skillsDiv = $('.skill-box');
  if (skillsDiv.length > 0) {
      var winH = $window.height(),
          skillsT = skillsDiv.offset().top;
      if (scroll + winH > skillsT) {
          $('.skillbar').each(function() {
              $(this).find('.skillbar-bar').animate({
                  width: $(this).attr('data-percent')
              }, 6000);
          });
          $('.timer-skill').countTo();
        $('.skill-bar-percent').removeClass('timer-skill');
      }
  }
}
/*-------------------------
         ReturnUp
-------------------------*/
function returnUp() {
    var $returnToTop = $('.return-to-top');
    if ($window.scrollTop() > 150) {
        $returnToTop.addClass('show');
    } else {
        $returnToTop.removeClass('show');
    }
    $returnToTop.click(function() {
        $root.stop().animate({
            scrollTop: 0
        }, 1500);
    });
}
/*-------------------------
         Map
-------------------------*/
// function map() {
//   "use strict";
//   var myMap = $('#my-map');

//   if (myMap.length) {
//       var lat = myMap.data("location-lat");
//       var lng = myMap.data("location-lng");
//       var options = {
//           center: new google.maps.LatLng(lat, lng),
//           zoom: 7,
//           mapTypeControl: true,
//           gestureHandling: 'cooperative',
//           panControl: false,
//           zoomControl: true,
//           zoomControlOptions: {
//               style: google.maps.ZoomControlStyle.DEFAULT,
//               position: google.maps.ControlPosition.TOP_LEFT
//           },
//           scaleControl: false,
//           styles: [{
//                   "elementType": "geometry",
//                   "stylers": [{
//                       "color": "#ebe3cd"
//                   }]
//               },
//               {
//                   "elementType": "labels.text.fill",
//                   "stylers": [{
//                       "color": "#523735"
//                   }]
//               },
//               {
//                   "elementType": "labels.text.stroke",
//                   "stylers": [{
//                       "color": "#f5f1e6"
//                   }]
//               },
//               {
//                 "featureType": "landscape",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "hue": "#6600ff"
//                     },
//                     {
//                         "saturation": -11
//                     }
//                 ]
//             },
//             {
//                 "featureType": "poi",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "saturation": -78
//                     },
//                     {
//                         "hue": "#6600ff"
//                     },
//                     {
//                         "lightness": -47
//                     },
//                     {
//                         "visibility": "off"
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "hue": "#5e00ff"
//                     },
//                     {
//                         "saturation": -79
//                     }
//                 ]
//             },
//             {
//                 "featureType": "road.local",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "lightness": 30
//                     },
//                     {
//                         "weight": 1.3
//                     }
//                 ]
//             },
//             {
//                 "featureType": "transit",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "visibility": "simplified"
//                     },
//                     {
//                         "hue": "#5e00ff"
//                     },
//                     {
//                         "saturation": -16
//                     }
//                 ]
//             },
//             {
//                 "featureType": "transit.line",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "saturation": -72
//                     }
//                 ]
//             },
//             {
//                 "featureType": "water",
//                 "elementType": "all",
//                 "stylers": [
//                     {
//                         "saturation": -65
//                     },
//                     {
//                         "hue": "#1900ff"
//                     },
//                     {
//                         "lightness": 8
//                     }
//                 ]
//             }
//         ]
//       };
//       var map = new google.maps.Map(document.getElementById('my-map'), options);
//       var marker1 = new google.maps.Marker({
//           position: map.getCenter(),
//           title: $('title').text(),
//           icon: myMap.data("location-icon"),
//           animation: google.maps.Animation.BOUNCE
//       });
//       marker1.setMap(map);
//   }
// }

/*-------------------------
    AJAX CONTACT FORM
-------------------------*/
function validateEmail(email) {

    "use strict";

    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function sendEmail() {

    "use strict";

    var name = $('#name').val();
    var email = $('#email').val();
    var subject = $('#subject').val();
    var comments = $('#comments').val();

    if (!name) {
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Name is required');
    } else if (!email) {
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Email is required');
    } else if (!validateEmail(email)) {
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Email is not valid');
    } else if (!subject) {
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Subject is required');
    } else if (!comments) {
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Comments is required');
    } else {
        $.ajax({
            type: 'POST',
            data: $("#contactForm").serialize(),
            url: "sendEmail.php",
            beforeSend: function() {
                $('#submit-btn').html('<span class="spinner-border spinner-border-sm"></span> Loading..');
            },
            success: function(data) {
                $('#submit-btn').html('Submit');
                var myObj = JSON.parse(data);
                if (myObj['status'] == 'Congratulation') {
                    $('#message').toast('show').addClass('bg-success').removeClass('bg-danger bg-warning');
                    $('.toast-body').html('<strong>' + myObj['status'] + ' : </strong> ' + myObj['message']);
                } else if (myObj['status'] == 'Error') {
                    $('#message').toast('show').addClass('bg-danger').removeClass('bg-success bg-warning');
                    $('.toast-body').html('<strong>' + myObj['status'] + ' : </strong> ' + myObj['message']);
                } else if (myObj['status'] == 'Warning') {
                    $('#message').toast('show').addClass('bg-warning').removeClass('bg-success bg-danger');
                    $('.toast-body').html('<strong>' + myObj['status'] + ' : </strong> ' + myObj['message']);
                }
            },
            error: function(xhr) {
                $('#submit-btn').html('Submit');
                $('#message').toast('show').addClass('bg-danger').removeClass('bg-success bg-warning');
                $('.toast-body').html('<strong> Error : </strong> Something went wrong, Please try again.');
            },
        });
    }
}







