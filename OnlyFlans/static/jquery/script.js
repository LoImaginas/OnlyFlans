$(document).ready(function(){
    $('.card').hover(function(){
        var price = $(this).find('.card-img-top').data('price');
        var tooltip = $('<div class="card-tooltip"></div>').text(price);
        $(this).append(tooltip);
    }, function(){
        $('.card-tooltip').remove();
    });
});

/* texto  leer mas y leer menos*/



