$(document).ready(function() {
	
	//Fade in, out & to
	$(".borderedpicture").bind("click", function (e) {
		 $(this).slideUp(2000);
		 $(this).slideDown(2000);
		
	});

	// //Slide in, out & to
	// $("#borderedpicture").click( function () {
	// 	$("#caja1").slideDown(2000);
	// 	$("#caja2").slideUp(2000);
	// 	$("#caja3").slideToggle(2000);
	// });

});
