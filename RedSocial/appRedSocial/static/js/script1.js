$.fn.qtip.styles.mystyle = { // Definir estilo que aplicaremos después
   width: 200,
   background: '#A2D959',
   color: 'black',
   textAlign: 'center',
   border: {
      width: 0.5,
      radius: 2,
      color: '#A2D959'
   },
   tip: 'bottomLeft',
   name: 'dark' 
}

$(document).ready(function() {
  
  $('#paisvasco').qtip(
  {
    content: 'Una comunidad autónoma es una especie de región, un estado suele tener varios.',
    style: 'mystyle'
  });
});