$(document).ready(function() 
{
	// $(".imagen-post").cycle('shuffle');
	$(".imagen-post").cycle({ 
		fx: 'scrollRight', 
		speed: 850, 
		timeout: 1750,
		random: 1
	});
});