$(document).ready(function() {
    $('div.step').hide();

    $('div.step').each(function(i) {
	$(this).delay(i * 100).show(0, function() {
	    $(this).prev().hide();
	});
    });
});

