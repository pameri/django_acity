// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "#tabla_pedidos"; // id
var nombre_tabla2 = "#tabla_pedidos2"; // id
var nombre_boton_aprobar = ".aprobar"; // Clase
var nombre_boton_verificar = ".verificar"; // Clase
var nombre_boton_detalle = ".detalle"; // Clase
var nombre_formulario_modal = "#frmAprobar"; //id
var nombre_formulario_modal2 = "#frmVerificar"; //id
var nombre_ventana_modal = "#myModal"; // id
var nombre_ventana_modal2 = "#myModal2"; // id
var nombre_ventana_modaldet = "#myModaldet"; // id

// Fin de configuraciones

	//aprobar oc
	$(document).on('ready',function(){
        $('.aprobaroc').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idoc').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response)
                {
                    if(response.status=="True"){                        
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        //alert("ok aprobar!");
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }                        
                    }
                    else if (response.status=="A") {                    	          	
                        alert("La Orden Compra ya está Aprobado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="V") {                    	          	
                        alert("La Orden Compra ya está Verificado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status ="P") {                    	          	
                        alert("La Orden Compra ya está parcialmente atendida!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status ="R") {                    	          	
                        alert("La Orden Compra ya está atendida!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al aprobar o/c!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };
        $('#frmAprobarOC').ajaxForm(options);
    });
    
    //verificar oc
	$(document).on('ready',function(){
        $('.verificaroc').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idoc').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response)
                {
                    if(response.status=="True"){                        
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;                        
                        if(elementos==1){
                             location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }                        
                    }
                    else if (response.status=="False") {                    	          	
                        alert("Hubo un error al verificar o/c! por favor comunicar al área de Sistemas");
                        $(nombre_ventana_modal).modal('hide');					
  					}
  					
                    else if (response.status=="A") {                    	          	
                        alert("La Orden Compra ya está Aprobado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="V") {                    	          	
                        alert("La Orden Compra ya está Verificado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					
  					else if (response.status ="P") {                    	          	
                        alert("La Orden Compra ya está parcialmente atendida! X  " + response.pedido_id);  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status ="R") {                    	          	
                        alert("La Orden Compra ya está atendida!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al verificar o/c!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };
        $('#frmVerificarOC').ajaxForm(options);
    });
    
    
	$(document).on('ready',function(){
        $('.anularoc').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idoc').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }                        
                    }
                    else if (response.status=="N") {                    	          	
                        alert("La Orden Compra ya está Anulado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status ="P") {                    	          	
                        alert("La Orden Compra ya está parcialmente atendida!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status ="R") {                    	          	
                        alert("La Orden Compra ya está atendida!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al anular orden de Compra!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };
        $('#frmAnularOC').ajaxForm(options);
    });
        
  
    //aprobar pedidos bm
    $(document).on('ready',function(){
        $('.aprobar').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idPedido').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response)
                {                	
                	if(response.status=="True"){
                        
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }                        
                    }
                    else if (response.status=="1") {                    	          	
                        alert("El pedido no cumple con la reglas de negocio");                       
                        $(nombre_ventana_modal).modal('hide');
                        location.reload();                        
  					}
  					else if (response.status=="A") {                    	          	
                        alert("El pedido ya está aprobado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                              location.reload();
                        }
                        else{
                            $('#tr'+idProd).remove();                            
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else if (response.status=="N") {                    	          	
                        alert("El pedido ya está anulado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                              location.reload();
                        }
                        else{
                            $('#tr'+idProd).remove();                            
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="P") {                    	          	
                        alert("El pedido está parcialmente atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="Q") {                    	          	
                        alert("El pedido ya está en un Req. de Compra !");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="R") {                    	          	
                        alert("El pedido ya está atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al aprobar el pedido!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                    
                    
                }
            };
        $('#frmAprobar').ajaxForm(options);
    });
    
	$(document).on('ready',function(){
        $(nombre_boton_verificar).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idPedido2').val(Pid);
            $('#modal_name2').text(name);
        });
        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        
                        var idProd = response.pedido_id2;
                        var elementos= $(nombre_tabla2+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal2).modal('hide');
                        }                        
                    }
                    else if (response.status=="1") {                    	          	
                        alert("El pedido no cumple con la reglas de negocio");                       
                        $(nombre_ventana_modal).modal('hide');
                        location.reload();                        
  					}
                    else if (response.status=="V") {                    	          	
                        alert("El pedido ya está verificado!");  
                        $(nombre_ventana_modal2).modal('hide');
                        var idProd = response.pedido_id2;
                        var elementos= $(nombre_tabla2+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal2).modal('hide');
                        }  						
  					}
  					else if (response.status=="A") {                    	          	
                        alert("El pedido ya está aprobado!");  
                        $(nombre_ventana_modal2).modal('hide');
                        var idProd = response.pedido_id2;
                        var elementos= $(nombre_tabla2+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal2).modal('hide');
                        }  						
  					}
  					else if (response.status=="P") {                    	          	
                        alert("El pedido está parcialmente atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="Q") {                    	          	
                        alert("El pedido ya está en un Req. de Compra !");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="R") {                    	          	
                        alert("El pedido ya está atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al verificar pedido!");
                        $(nombre_ventana_modal2).modal('hide');
                    };
                }
            };
        $(nombre_formulario_modal2).ajaxForm(options);
    });
    
     $(document).on('ready',function(){
        $('.anular').on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idPedido').val(Pid);
            $('#modal_name').text(name);
        });
        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }                        
                    }
                    else if (response.status=="N") {                    	          	
                        alert("El pedido ya esta anulado!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="P") {                    	          	
                        alert("El pedido esta parcialmente atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="Q") {                    	          	
                        alert("El pedido ya esta en un Req. de Compra !");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
  					else if (response.status=="R") {                    	          	
                        alert("El pedido ya está atendido!");  
                        $(nombre_ventana_modal).modal('hide');
                        var idProd = response.pedido_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }  						
  					}
                    else{
                        alert("Hubo un error al anular el pedido!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };
        $('#frmAnular').ajaxForm(options);
    });
    
    