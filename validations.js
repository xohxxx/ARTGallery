function validarEmail() {
	// Obtener el valor del correo electrónico
	var email = document.getElementById("email").value;
	
	// Expresión regular para validar el formato del correo electrónico
	var expresion = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
	
	// Validar el correo electrónico
	if (expresion.test(email)) {
	  alert("El correo electrónico es válido");
	} else {
	  alert("El correo electrónico no es válido");
	}
  }