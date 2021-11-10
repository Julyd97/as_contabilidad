
const tbody = document.querySelectorAll('#position tr');

let DOMModal = document.getElementById('modal1');
let modalElement = new bootstrap.Modal(DOMModal, {
  keyboard: false
});

for (var i = 1; i < tbody.length; i++){
  tbody[i].addEventListener('click', function() {
    console.log(this.childNodes[1].innerHTML)
    modalElement.show(this);
  });
}

DOMModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  let serial = button.getAttribute('data-bs-serial')
  let descripcion = button.getAttribute('data-bs-descripcion')
  let cartera = button.getAttribute('data-bs-cartera')
  let tercero = button.getAttribute('data-bs-tercero')
  let proveedor = button.getAttribute('data-bs-proveedor')
  let costo = button.getAttribute('data-bs-costo')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  let modalSerial = DOMModal.querySelector('#serial-text')
  let modalDescripcion = DOMModal.querySelector('#descripcion-text')
  let modalCartera = DOMModal.querySelector('#check-cartera')
  let modalTercero = DOMModal.querySelector('#check-tercero')
  let modalProveedor = DOMModal.querySelector('#check-proveedor')
  let modalCosto = DOMModal.querySelector('#check-costo')

  if(cartera == 'True'){
    cartera= true
  }else{
    cartera=false
  }
  if(tercero == 'True'){
    tercero= true
  }else{
    tercero=false
  }
  if(proveedor == 'True'){
    proveedor= true
  }else{
    proveedor=false
  }
  if(costo == 'True'){
    costo= true
  }else{
    costo=false
  }
  //var modalBodyInput = DOMModal.querySelector('.modal-body input')
  modalSerial.value = serial
  modalDescripcion.value = descripcion
  modalCartera.checked = cartera
  modalTercero.checked = tercero
  modalProveedor.checked = proveedor
  modalCosto.checked = costo
  console.log(cartera)
  //modalBodyInput.value = recipient
})
// Click boton de modificar
let buttonmodify = document.getElementById('buttonmodify')
buttonmodify.addEventListener('click', function(){
    let descripcion = document.getElementById('descripcion-text') 
    let cartera = document.getElementById('check-cartera')
    let tercero = document.getElementById('check-tercero')
    let proveedor = document.getElementById('check-proveedor')
    let costo = document.getElementById('check-costo')
    descripcion.disabled = false
    cartera.disabled = false
    tercero.disabled = false
    proveedor.disabled = false
    costo.disabled = false
})
let myModalEl = document.getElementById('modal1')
myModalEl.addEventListener('hidden.bs.modal', function () {
    let descripcion = document.getElementById('descripcion-text') 
    let cartera = document.getElementById('check-cartera')
    let tercero = document.getElementById('check-tercero')
    let proveedor = document.getElementById('check-proveedor')
    let costo = document.getElementById('check-costo')
    descripcion.disabled = true
    cartera.disabled = true
    tercero.disabled = true
    proveedor.disabled = true
    costo.disabled = true
})
let buttonclose = document.getElementById('buttonclose')
buttonclose.addEventListener('click', function(){
    let descripcion = document.getElementById('descripcion-text') 
    let cartera = document.getElementById('check-cartera')
    let tercero = document.getElementById('check-tercero')
    let proveedor = document.getElementById('check-proveedor')
    let costo = document.getElementById('check-costo')
    descripcion.disabled = true
    cartera.disabled = true
    tercero.disabled = true
    proveedor.disabled = true
    costo.disabled = true

})
let buttonbuscar = document.getElementById('buttonbuscar')
buttonbuscar.addEventListener('click', function(){
  let buscar = document.getElementById('textbuscar')
  if(buscar.style.display !== 'none'){
    buscar.style.display = 'none'
  }else{
    buscar.style.display = "inline"
  }
  
})

// api url
const api_url =
	"/api/v1.0/proveedores/";

function sendapi(url,data){
  
  fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(response => response.json())
  .then(data => {
    alert("Proveedor creado");
    
  })
  

}
// Defining async function
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url);
	
	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	// if (response) {
	// 	hideloader();
	// }
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
// function hideloader() {
// 	document.getElementById('loading').style.display = 'none';
// }
// Function to define innerHTML for HTML table
function send(data){
  sendapi(api_url, data);
}
let buttonEnviar = document.getElementById('enviarproveedor')
buttonEnviar.addEventListener('click',function(){
  let primerNombre1 = document.getElementById('primerNombre').value
  let segundoNombre1 = document.getElementById('segundoNombre').value
  let primerApellido1 = document.getElementById('primerApellido').value
  let segundoApellido1 = document.getElementById('segundoApellido').value
  let tipoDocumento1 = document.getElementById('tipoDocumento').value
  let numDocumento1 = document.getElementById('numDocumento').value
  let correo1 = document.getElementById('correo').value
  let pais1 = document.getElementById('pais').value
  let departamento1 = document.getElementById('departamento').value
  let municipio1 = document.getElementById('municipio').value
  let direccion1 = document.getElementById('direccion').value
  let codigoPostal1 = document.getElementById('codigoPostal').value
  let telefono1 = document.getElementById('telefono').value

  let data = {primerNombre: primerNombre1, segundoNombre: segundoNombre1, primerApellido: primerApellido1, 
              segundoApellido: segundoApellido1, tipoDocumento: tipoDocumento1, numDocumento: numDocumento1,
              correo: correo1, pais:pais1, departamento: departamento1, municipio:municipio1, direccion:direccion1, codigoPostal:codigoPostal1, telefono:telefono1 }
  
  send(data);
  
})
function show(data) {
	let tab =
		`<tr>
		<th>Pais</th>
		<th>Codigo Postal</th>
		<th>Primer Nombre</th>
		<th>Segundo Nombre</th>
		<th>Primer Apellido</th>
    <th>Segundo Apellido</th>
    <th>Departamento</th>
    <th>Telefono</th>
    <th>Correo</th>
    <th>Municipio</th>
    <th>Tipo de Documento</th>
    <th>Numero de Documento</th>
    <th>Dirección</th>
    </tr>`;
	
	// Loop to access all rows
	for (let r of data) {
		tab += `<tr>
	<td>${r.pais} </td>
	<td>${r.codigoPostal}</td>
	<td>${r.primerNombre}</td>
	<td>${r.segundoNombre}</td>
  <td>${r.primerApellido}</td>
  <td>${r.segundoApellido}</td>
  <td>${r.departamento}</td>
  <td>${r.telefono}</td>
  <td>${r.correo}</td>
  <td>${r.municipio}</td>
  <td>${r.tipoDocumento}</td>
  <td>${r.numDocumento}</td>
  <td>${r.direccion}</td>		
</tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("proveedores").innerHTML = tab;
}


