$(document).ready(function () {

    $(window).scroll(function () {

        if ($(this).scrollTop() > 50) {
            $('#header').addClass('sticky');
        } else {
            $('#header').removeClass('sticky');
        }

        if ($(this).scrollTop() > 200) {
            $('#back-to-top').addClass('show');
        } else {
            $('#back-to-top').removeClass('show');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, '300');
    });



    $('.menu-btn').click(function (e) {
        $('.menu-container').toggleClass('open');
    });

    $('.menu-close').click(function () {
        $('.menu-container').removeClass('open');
    });

    $(".sid-menu li.menu-item-has-children").append('<div class="sub-btn"><i class="fa-sharp fa-light fa-angle-right"></i></div>');

    $('.sub-btn').click(function () {
        $(this).prev().slideToggle();
        $(this).parent().siblings().find('.sub-menu').slideUp();
        $(this).parent().siblings().removeClass('open');
        $(this).parent().addClass('open');
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