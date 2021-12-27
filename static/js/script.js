const tablaproveedores = `<tr>
<th>Nombre</th>
<th>Tipo de Documento</th>
<th>Numero de Documento</th>
<th>Correo</th>
<th>Pais</th>
<th>Departamento</th>
<th>Municipio</th>
<th>Dirección</th>
<th>Codigo Postal</th>    
<th>Telefono</th>
<th class="d-none">id</th>  
</tr>`;
const tabladocumentos = `<tr>
<th>Fecha</th>
<th>Prefijo</th>
<th>Consecutivo</th>
<th>Descripcion</th> 
</tr>`;
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
  console.log(descripcion)
  //modalBodyInput.value = recipient
})
// Click boton de modificar cuenta
let buttonmodify = document.getElementById('buttonmodify')
buttonmodify.addEventListener('click', habilitarmodalcuentas)
function habilitarmodalcuentas(){
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
}
let buttonguardar = document.getElementById('submitGuardar')
buttonguardar.addEventListener('click', habilitarmodalcuentas)

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

// api url
const api_url =
	"/api/v1.0/proveedores/";

function sendapi(url,data,alerta, tabla, destino){
  
  fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(response => response.json())
  .then(data => {
    alert(alerta);
    loadtable(url,tabla,destino)
    loadtable(url,tabla,destino)
  })
  

}
// Defining async function
async function getapi(url) {
	
	const response = await fetch(url);
	
  return response

}
// Calling that async function

//getapi(api_url);


loadtable(api_url,tablaproveedores,"proveedores");
loadtable('/api/v1.0/documentoscontables/',tabladocumentos,"tabladocumentoscontables");

// Function to hide the loader
// function hideloader() {
// 	document.getElementById('loading').style.display = 'none';
// }
// Function to define innerHTML for HTML table



// Choose fields from proveedores table



// Send to modify in the api
function modifyinapi(url,data,alerta){
  
  fetch(url, {
    method: 'PUT', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(response => response.json())
  .then(data => {
    alert(alerta);
    loadtable(api_url,tablaproveedores,"proveedores")
  })
}

function deleteapi(url){
  fetch(url, {
    method: 'DELETE', // or 'PUT'
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(response => response.json())
  .then(data => {
    alert("Proveedor eliminado");
    loadtable(api_url,tablaproveedores,"proveedores")
  })
}
// Muestra la informacion de la api en la tabla previamente creada
function show(data, tabladestino,id) {
	let tab = tabladestino;
  if(id == "proveedores"){
      for (let r of data) {
        tab += `<tr>
      <td data-pn=${r.primerNombre} data-sn=${r.segundoNombre} data-pa=${r.primerApellido} data-sa=${r.segundoApellido}>${r.primerNombre} ${r.segundoNombre} ${r.primerApellido} ${r.segundoApellido} </td>
      <td>${r.tipoDocumento}</td>
      <td>${r.numDocumento}</td>
      <td>${r.correo}</td>
      <td>${r.pais} </td>
      <td>${r.departamento}</td>
      <td>${r.municipio}</td>
      <td>${r.direccion}</td>	
      <td>${r.codigoPostal}</td>
      <td>${r.telefono}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
  if(id == "tabladocumentoscontables"){
      for (let r of data) {
        tab += `<tr>
      <td>${r.fecha}</td>
      <td>${r.prefijo}</td>
      <td>${r.consecutivo}</td>
      <td>${r.descripcion}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
	// Setting innerHTML as tab variable
	document.getElementById(id).innerHTML = tab;
}

//Cargar la informacion de los proveedores(api) que esta en la tabla al modal emergente 
async function loadtable(url, tabladestino, id){
  response = await getapi(url);
  if (response.ok == true){ 
    var data = await response.json();
    show(data, tabladestino,id);
  } else{
    alert('El proveedor que esta buscando no se encuentra, revise la busqueda')
  }
  if(id=="proveedores"){
    cargarmodalproveedores()
  }
  if(id=="tabladocumentoscontables"){
    cargarmodaldocumentos()
  }
  
}

function cargarmodalproveedores(){
  const tbodys = document.querySelectorAll('#proveedores tr');

  let DOMModals = document.getElementById('modalModifyProveedor');
  console.log(tbodys);
  let modalElements = new bootstrap.Modal(DOMModals, {
    keyboard: false
  });

  for (var i = 1; i < tbodys.length; i++){
    tbodys[i].addEventListener('click', function() {
      modalElements.show(this);
    });
  }
  DOMModals.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    
    let primerNombre = button.childNodes[1].getAttribute('data-pn')
    let segundoNombre = button.childNodes[1].getAttribute('data-sn')
    let primerApellido = button.childNodes[1].getAttribute('data-pa')
    let segundoApellido = button.childNodes[1].getAttribute('data-sa')
    let tipoDocumento = button.childNodes[3].innerHTML
    let numDocumento = button.childNodes[5].innerHTML
    let correo = button.childNodes[7].innerHTML
    let pais = button.childNodes[9].innerHTML
    let departamento = button.childNodes[11].innerHTML
    let municipio = button.childNodes[13].innerHTML
    let direccion = button.childNodes[15].innerHTML
    let codigoPostal = button.childNodes[17].innerHTML
    let telefono = button.childNodes[19].innerHTML
    let id = button.childNodes[21].innerHTML
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    let modalPrimerNombre = DOMModals.querySelector('#primerNombrem')
    let modalSegundoNombre = DOMModals.querySelector('#segundoNombrem')
    let modalPrimerApellido = DOMModals.querySelector('#primerApellidom')
    let modalSegundoApellido = DOMModals.querySelector('#segundoApellidom')
    let modalTipoDocumento = DOMModals.querySelector('#tipoDocumentom')
    let modalNumeroDocumento = DOMModals.querySelector('#numDocumentom')
    let modalCorreo = DOMModals.querySelector('#correom')
    let modalPais = DOMModals.querySelector('#paism')
    let modalDepartamento = DOMModals.querySelector('#departamentom')
    let modalMunicipio = DOMModals.querySelector('#municipiom')
    let modalDireccion = DOMModals.querySelector('#direccionm')
    let modalCodigoPostal = DOMModals.querySelector('#codigoPostalm')
    let modalTelefono = DOMModals.querySelector('#telefonom')
    let modalId = DOMModals.querySelector("#idm")

    //var modalBodyInput = DOMModal.querySelector('.modal-body input')
    modalPrimerNombre.value = primerNombre
    modalSegundoNombre.value = segundoNombre
    modalPrimerApellido.value = primerApellido
    modalSegundoApellido.value = segundoApellido
    modalTipoDocumento.value = tipoDocumento
    modalNumeroDocumento.value = numDocumento
    modalCorreo.value = correo
    modalPais.value = pais
    modalDepartamento.value = departamento
    modalMunicipio.value = municipio
    modalDireccion.value = direccion
    modalCodigoPostal.value = codigoPostal
    modalTelefono.value = telefono
    modalId.value = id
    //modalBodyInput.value = recipient
  })
}

function cargarmodaldocumentos(){
  const tbodyss = document.querySelectorAll('#tabladocumentoscontables tr');

  let DOMModals = document.getElementById('modalmodifydocumentocontable');
  console.log(tbodyss);
  let modalElements = new bootstrap.Modal(DOMModals, {
    keyboard: false
  });

  for (var i = 1; i < tbodyss.length; i++){
    tbodyss[i].addEventListener('click', function() {
      modalElements.show(this);
    });
  }
  DOMModals.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    let fecha = button.childNodes[1].innerHTML
    let prefijo = button.childNodes[3].innerHTML
    let consecutivo = button.childNodes[5].innerHTML
    let descripcion = button.childNodes[7].innerHTML
    let id = button.childNodes[9].innerHTML
    
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    let modalPrefijo= DOMModals.querySelector('#prefijodocumentom')
    let modalConsecutivo = DOMModals.querySelector('#consecutivodocumentom')
    let modalDescripcion = DOMModals.querySelector('#descripciondocumentom')
    let modalFecha = DOMModals.querySelector('#fechadocumentom')
    let modalid = DOMModals.querySelector('#iddocumentom')

    //var modalBodyInput = DOMModal.querySelector('.modal-body input')
    modalPrefijo.value = prefijo
    modalConsecutivo.value = consecutivo
    modalDescripcion.value = descripcion
    modalFecha.value = fecha
    modalid.value = id
    //modalBodyInput.value = recipient
    
  })
}
// Enviar la info del proveedor para crearlo
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
  
  sendapi(api_url,data,"Proveedor creado", tablaproveedores, "proveedores");
})
// Boton para modificar proveedores en el modal de proveedor
let buttonModificarProveedor = document.getElementById('modificarProveedor')
buttonModificarProveedor.addEventListener('click', function(){
  let primerNombre = document.getElementById('primerNombrem') 
  let segundoNombre = document.getElementById('segundoNombrem')
  let primerApellido = document.getElementById('primerApellidom')
  let segundoApellido = document.getElementById('segundoApellidom')
  let tipoDocumento = document.getElementById('tipoDocumentom')
  let numDocumento = document.getElementById('numDocumentom')
  let correo = document.getElementById('correom')
  let pais = document.getElementById('paism')
  let departamento = document.getElementById('departamentom')
  let municipio = document.getElementById('municipiom')
  let direccion = document.getElementById('direccionm')
  let codigoPostal = document.getElementById('codigoPostalm')
  let telefono = document.getElementById('telefonom')
  primerNombre.disabled = false
  segundoNombre.disabled = false
  primerApellido.disabled = false
  segundoApellido.disabled = false
  tipoDocumento.disabled = false
  numDocumento.disabled = false
  correo.disabled = false
  pais.disabled = false
  departamento.disabled = false
  municipio.disabled = false
  direccion.disabled = false
  codigoPostal.disabled = false
  telefono.disabled = false
})
// Guardar la info de proveedor en el modal de modificar
let buttonGuardarProveedor = document.getElementById('guardarProveedor')
buttonGuardarProveedor.addEventListener('click',function(){
  let primerNombre1 = document.getElementById('primerNombrem').value
  let segundoNombre1 = document.getElementById('segundoNombrem').value
  let primerApellido1 = document.getElementById('primerApellidom').value
  let segundoApellido1 = document.getElementById('segundoApellidom').value
  let tipoDocumento1 = document.getElementById('tipoDocumentom').value
  let numDocumento1 = document.getElementById('numDocumentom').value
  let correo1 = document.getElementById('correom').value
  let pais1 = document.getElementById('paism').value
  let departamento1 = document.getElementById('departamentom').value
  let municipio1 = document.getElementById('municipiom').value
  let direccion1 = document.getElementById('direccionm').value
  let codigoPostal1 = document.getElementById('codigoPostalm').value
  let telefono1 = document.getElementById('telefonom').value
  let id1 = document.getElementById('idm').value

  let data = {primerNombre: primerNombre1, segundoNombre: segundoNombre1, primerApellido: primerApellido1, 
              segundoApellido: segundoApellido1, tipoDocumento: tipoDocumento1, numDocumento: numDocumento1,
              correo: correo1, pais:pais1, departamento: departamento1, municipio:municipio1, direccion:direccion1, codigoPostal:codigoPostal1, telefono:telefono1 }
    let url = '/api/v1.0/proveedor/'.concat(id1)
    modifyinapi(url,data,"Proveedor modificado");
});

// Borrar proveedor en el modal de modificar
let buttonBorrarProveedor = document.getElementById('borrarProveedor')
buttonBorrarProveedor.addEventListener('click',function(){
  let id1 = document.getElementById('idm').value
  let url = '/api/v1.0/proveedor/'.concat(id1)
  deleteapi(url);
});

// Bloquea los campos del modal de proveedores cuando se cierra
let ModalModifyProveedor = document.getElementById('modalModifyProveedor')
ModalModifyProveedor.addEventListener('hidden.bs.modal', function () {
    let primerNombre = document.getElementById('primerNombrem') 
    let segundoNombre = document.getElementById('segundoNombrem')
    let primerApellido = document.getElementById('primerApellidom')
    let segundoApellido = document.getElementById('segundoApellidom')
    let tipoDocumento = document.getElementById('tipoDocumentom')
    let numDocumento = document.getElementById('numDocumentom')
    let correo = document.getElementById('correom')
    let pais = document.getElementById('paism')
    let departamento = document.getElementById('departamentom')
    let municipio = document.getElementById('municipiom')
    let direccion = document.getElementById('direccionm')
    let codigoPostal = document.getElementById('codigoPostalm')
    let telefono = document.getElementById('telefonom')
    primerNombre.disabled = true
    segundoNombre.disabled = true
    primerApellido.disabled = true
    segundoApellido.disabled = true
    tipoDocumento.disabled = true
    numDocumento.disabled = true
    correo.disabled = true
    pais.disabled = true
    departamento.disabled = true
    municipio.disabled = true
    direccion.disabled = true
    codigoPostal.disabled = true
    telefono.disabled = true
})

// Buscar proveedor boton + tecla
let buttonbuscar = document.getElementById('buttonbuscar')
buttonbuscar.addEventListener('click', function(){
  buscarproveedor();
})

document.querySelector('#textbuscar').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    buscarproveedor();
  }
}); 

function buscarproveedor (){
  let buscar = document.getElementById('textbuscar')
  if(buscar.innerHTML != null){
    let url = '/api/v1.0/proveedores/'
    loadtable(url + buscar.value,tablaproveedores,"proveedores")
  }else{
    
  }
}
// Modal Crear Documento Contable
let buttonEnviarNuevoDocumento = document.getElementById('enviarnuevodocumento')
buttonEnviarNuevoDocumento.addEventListener('click',function(){
  let prefijo1 = document.getElementById('prefijonuevodocumento').value
  console.log(prefijo1)
  let consecutivo1 = document.getElementById('consecutivonuevodocumento').value
  let descripcion1 = document.getElementById('descripcionnuevodocumento').value
  let fecha1 = document.getElementById('fechanuevodocumento').value

  let data = {fecha: fecha1, consecutivo: consecutivo1, descripcion: descripcion1,  prefijo: prefijo1  }
  
  sendapi('/api/v1.0/documentoscontables/',data,"Docuemnto creado",tabladocumentos,"tabladocumentoscontables");
})

// Modal modificar Documento contable

let buttonmodificardocumento = document.getElementById('modificardocumentom')
buttonmodificardocumento.addEventListener('click', function(){
  let elements = document.querySelectorAll('#modalmodifydocumentocontable div.modal-body div.row.container div input');
  for(let e of elements){
    e.disabled= false
  }
})

let modalmodifydocumento = document.getElementById('modalmodifydocumentocontable')
modalmodifydocumento.addEventListener('hidden.bs.modal', function () {
  let elements = document.querySelectorAll('#modalmodifydocumentocontable div.modal-body div.row.container div input');
  for(let e of elements){
    e.disabled= true
  }
})

let buttonguardardocumento = document.getElementById('guardardocumentom')
buttonguardardocumento.addEventListener('click',function(){
  let prefijo1 = document.getElementById('prefijonuevodocumento').value
  console.log(prefijo1)
  let consecutivo1 = document.getElementById('consecutivonuevodocumento').value
  let descripcion1 = document.getElementById('descripcionnuevodocumento').value
  let fecha1 = document.getElementById('fechanuevodocumento').value

  let data = {fecha: fecha1, consecutivo: consecutivo1, descripcion: descripcion1,  prefijo: prefijo1  }
  let url= '/api/v1.0/documentoscontables/'.concat(id1)
  modifyinapi()
})