
$(function() {
    let redFound = $('header').hasClass('red')
    let greenFound = $('header').hasClass('green')

    if (redFound && greenFound) {
        $('header').removeClass('red')
    } 
    if (!redFound && !greenFound) {
        $('header').addClass('red')
    }
    $('#toggle_header').click(function () {
        redFound = $('header').hasClass('red')
        greenFound = $('header').hasClass('green')
        
        if (redFound) {
            $('header').removeClass('red')
            $('header').addClass('green')
        } else if (greenFound) {
            $('header').removeClass('green')
            $('header').addClass('red')
        }
    });
});
