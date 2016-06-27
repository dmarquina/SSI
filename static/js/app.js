$(document).ready(function() {
        $('select').material_select();
        //llenar los progress bar

        $('.componentprogress').each(function() {
    		porcentaje = document.getElementById("status"+this.id).innerHTML
        	var elem = document.getElementById("componentbar"+this.id); 
            console.log(porcentaje);
            elem.style.width = porcentaje.replace(",",".");
        	var porcentajeEntero = parseInt(porcentaje.replace("%", ""));
        	if(porcentajeEntero<50)
        		elem.style.backgroundColor = "#F44336";
        	else if(porcentajeEntero>=50 && porcentajeEntero<70)
        		elem.style.backgroundColor = "#FFEB3B";
		});
});
