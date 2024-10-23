document.addEventListener('DOMContentLoaded', function() {
    var toggles = document.querySelectorAll('.accordion-toggle');
    toggles.forEach(function(toggle) {
        toggle.addEventListener('click', function() {
            var submenu = this.nextElementSibling;
            var arrow = this.querySelector('.arrow');
            if (submenu.style.display === 'block') {
                submenu.style.display = 'none';
                arrow.classList.remove('rotate');
            } else {
                submenu.style.display = 'block';
                arrow.classList.add('rotate');
            }
        });
    });
});

function mostrarFormulario() {
    var formulario = document.getElementById('formularioRegistro');
    if (formulario.classList.contains('formulario-oculto')) {
        formulario.classList.remove('formulario-oculto');
        formulario.classList.add('formulario-visible');
    } else {
        formulario.classList.remove('formulario-visible');
        formulario.classList.add('formulario-oculto');
    }
}
