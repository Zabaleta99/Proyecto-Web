window.onload = function () 
{
	$("#verComments").click( function () 
	{
		$(this).attr('disabled', true);
		$("#ocultarComments").attr('disabled', false);
		$(".comentarios").css("display", "block");
	});

	$("#ocultarComments").click( function () 
	{
		$("#verComments").attr('disabled', false);
		$("#ocultarComments").attr('disabled', true);
		$(".comentarios").css("display", "none");
	});
}