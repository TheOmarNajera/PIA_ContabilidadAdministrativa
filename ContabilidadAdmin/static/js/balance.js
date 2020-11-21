    function activo(){
        try {
            var efectivo = parseFloat(document.getElementById("efec").value) || 0,
            clientes = parseFloat(document.getElementById("clts").value) || 0,
            deuddiv = parseFloat(document.getElementById("deuddiv").value) || 0;
            funcyemp = parseFloat(document.getElementById("funcyemp").value) || 0;
            invdemat = parseFloat(document.getElementById("invdemat").value) || 0;
            invprodter = parseFloat(document.getElementById("invprodter").value) || 0;

            document.getElementById("total_ac").value = efectivo + clientes + deuddiv + funcyemp + invdemat + invprodter;
        } catch (e) {}

        try {
            var terreno = parseFloat(document.getElementById("terr").value) || 0,
            planta_yeq = parseFloat(document.getElementById("plantayeq").value) || 0,
            depreciacion_acu = parseFloat(document.getElementById("depacu").value) || 0;

            document.getElementById("total_anc").value = terreno + planta_yeq - depreciacion_acu;
        } catch (e) {}

        try {
            document.getElementById("total_activos").value = efectivo + clientes + deuddiv + funcyemp + invdemat + invprodter + terreno + planta_yeq - depreciacion_acu;
        } catch (e) {}
    }


        function pasivoCapital(){
            try {
                var proveedores = parseFloat(document.getElementById("prov").value) || 0,
                docxpagar = parseFloat(document.getElementById("dxp").value) || 0,
                isrxp = parseFloat(document.getElementById("ixp").value) || 0;

                document.getElementById("total_pascp").value = proveedores + docxpagar + isrxp;
            } catch (e) {}
        

            try {
                var prestamosbancarios = parseFloat(document.getElementById("pb").value) || 0;

                document.getElementById("totalpaslp").value = prestamosbancarios;
            } catch (e)  {}


            try {
                document.getElementById("totalpasivos").value = proveedores + docxpagar + isrxp + prestamosbancarios;
            } catch (e)  {} 

            try {
                var capitalContribuido = parseFloat(document.getElementById("cc").value) || 0,
                capitalGanado = parseFloat(document.getElementById("cg").value) || 0;

                document.getElementById("cct").value = capitalContribuido + capitalGanado;
            } catch (e) {}

            try {
                document.getElementById("spc").value = proveedores + docxpagar + isrxp + prestamosbancarios + capitalContribuido + capitalGanado;
            } catch (e) {}

        }
        
