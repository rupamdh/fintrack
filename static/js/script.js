jQuery(document).ready(function () {

    jQuery(window).scroll(function () {

        if (jQuery(this).scrollTop() > 50) {
            jQuery('#header').addClass('sticky');
        } else {
            jQuery('#header').removeClass('sticky');
        }

        if (jQuery(this).scrollTop() > 200) {
            jQuery('#back-to-top').addClass('show');
        } else {
            jQuery('#back-to-top').removeClass('show');
        }
    });

    jQuery('.back-to-top').click(function () {
        jQuery('html, body').animate({ scrollTop: 0 }, '300');
    });



    jQuery('.menu-btn').click(function (e) {
        jQuery('.menu-container').toggleClass('open');
    });

    jQuery('.menu-close').click(function () {
        jQuery('.menu-container').removeClass('open');
    });

    jQuery(".sid-menu li.menu-item-has-children").append('<div class="sub-btn"><i class="fa-sharp fa-light fa-angle-right"></i></div>');

    jQuery('.sub-btn').click(function () {
        jQuery(this).prev().slideToggle();
        jQuery(this).parent().siblings().find('.sub-menu').slideUp();
        jQuery(this).parent().siblings().removeClass('open');
        jQuery(this).parent().addClass('open');
    });

    // const swiper = new Swiper('.locations', {
    //     loop: true,
    //     navigation: {
    //         nextEl: '.swiper-button-next',
    //         prevEl: '.swiper-button-prev',
    //     },
    //     breakpoints: {
    //         // when window width is >= 320px
    //         320: {
    //             slidesPerView: 1,
    //             spaceBetween: 20
    //         },
    //         // when window width is >= 480px
    //         480: {
    //             slidesPerView: 3,
    //             spaceBetween: 30
    //         },
    //         // when window width is >= 640px
    //         640: {
    //             slidesPerView: 3,
    //             spaceBetween: 30
    //         }
    //     }

    // });

    // const swiper2 = new Swiper('.services', {
    //     loop: true,
    //     navigation: {
    //         nextEl: '.swiper-next',
    //         prevEl: '.swiper-prev',
    //     },
    //     breakpoints: {
    //         // when window width is >= 320px
    //         320: {
    //             slidesPerView: 1,
    //             spaceBetween: 20
    //         },
    //         // when window width is >= 480px
    //         480: {
    //             slidesPerView: 3,
    //             spaceBetween: 30
    //         },
    //         // when window width is >= 640px
    //         640: {
    //             slidesPerView: 3,
    //             spaceBetween: 30
    //         }
    //     }

    // });

    // const swiper3 = new Swiper('.service-data', {
    //     loop: true,
    //     slidesPerView: 1,
    //     navigation: {
    //         nextEl: '.swiper-button-next',
    //         prevEl: '.swiper-button-prev',
    //     },
    // });

    // const swiper4 = new Swiper('.service-imgs', {
    //     loop: true,
    //     slidesPerView: 1,
    //     allowTouchMove: false,
    //     effect: 'fade'
    // });

    // swiper3.on('slideChange', function () {
    //     swiper4.slideTo(swiper3.realIndex);
        
    // });



});