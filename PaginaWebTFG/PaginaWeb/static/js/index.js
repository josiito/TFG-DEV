// Carga todo el js cuando ya se ha cargado el html
document.addEventListener('DOMContentLoaded', () => {

    // Botones para controlar el modo de enviar el texto a analizar
    const rBtnDocu  = document.getElementById("s-documento");
    const rBtnTexto = document.getElementById("s-texto");

    const opciones = document.form.forma;
    let checked = false;
    var elemIndex = -1;
    for(var i = 0; i < opciones.length && !checked; i++) {
        checked = opciones[i].checked;
        if(checked) elemIndex = i;
    }

    // Se le da valor al atributo del formulario cuando se selecciona la opcion del documento
    if (opciones[elemIndex].value === "documento") {
        document.form.setAttribute("enctype", "multipart/form-data");
        document.getElementById("input-doc-text").setAttribute("required", "required");
        
        // Se oculta el cuadro de texto (no es buena practica, porque se pinta el html)
        document.getElementById('textarea-text').setAttribute('hidden', 'hidden');
    }

    // Compruebo que el boton se ha obtenido correctamente
    if (rBtnDocu) {
        rBtnDocu.addEventListener('click', () => {

            const label = document.getElementById("label-doc-text");
            const input = document.getElementById("input-doc-text");

            const textarea = document.getElementById("textarea-text");

            if (label) {
                label.removeAttribute("hidden", "hidden");
                label.innerHTML = "Documento a analizar (pdf o txt):";
            } 

            if (input && textarea) {
                input.setAttribute("required", "required");
                document.form.setAttribute("enctype", "multipart/form-data");

                input.removeAttribute("hidden");

                // Se oculta el cuadro de texto (no es buena practica, porque se pinta el html)
                textarea.setAttribute('hidden', 'hidden');
                textarea.removeAttribute('required');
            }

        });
    }

    // Compruebo que el boton se ha obtenido correctamente
    if (rBtnTexto) {
        rBtnTexto.addEventListener('click', () => {

            // Borro el documento

            const label = document.getElementById("label-doc-text");
            const input = document.getElementById("input-doc-text");

            const textarea = document.getElementById("textarea-text");

            if (label) {
                label.setAttribute("hidden", "hidden");
            }

            if (input && textarea) {
                document.form.removeAttribute("enctype", "multipart/form-data");

                textarea.removeAttribute("hidden");
                textarea.setAttribute('required', 'required');

                // Se oculta el cuadro de texto (no es buena practica, porque se pinta el html)
                input.setAttribute('hidden', 'hidden');
                input.removeAttribute('required');
            }

        });
    }

});