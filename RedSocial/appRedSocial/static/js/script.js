$(document).ready( function() {
    $('#buscador').submit( function(e) {
        e.preventDefault();
        console.log('b')
       $.ajax({
       	url: $(this).attr('action'),
       	type: $(this).attr('method'),
       	data: $(this).serialize(),

       	success: function(json){
          if (Object.keys(json).length>0){
            var html = '<div class="fh5co-blog animate-box"><div class="blog-text" id="resultado"><h2 class="a">Los resultados de la busqueda son:<ul>'
            for( var i = 0;i <Object.keys(json).length; i++){
              html += '<li><a href="http://127.0.0.1:8000/perfil/'+json[i].id+'">'+json[i].id+':  '+json[i].nombre+' '+json[i].apellidoUno+'</a></li></ul>'
            }
            html+=' </ul></h2> </div> </div>'
            $('#resultado').html(html);
            console.log(json)
          }
          else{
             html='<span> No se ha encontrado ningún usuario.</span>'
            $('#resultado').html(html);
          }
       		
       	}
       	
       })
    });
});