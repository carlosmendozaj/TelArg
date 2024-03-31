document.getElementById("enviar").addEventListener("click", function() {
    var respuesta = document.getElementById("respuesta").value;
    console.log("Enviando respuesta: ", respuesta);

    fetch('http://localhost:5000/guardar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({respuesta: respuesta}),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Ver la respuesta del servidor
        document.getElementById("resultado").textContent = "Gracias por tu respuesta: " + respuesta;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("resultado").textContent = "Hubo un error al enviar tu respuesta.";
    });
});