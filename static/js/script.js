const tablacuentas = `<tr>
<th>Codigo</th>
<th>Descripción</th>
<th>Cartera</th>
<th>Tercero</th>
<th>Proveedor</th>
<th>C.Costo</th>
<th class="d-none">parent_id</th>
<th class="d-none">nivel</th>
<th class="d-none">id</th>  
</tr>`;
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
<th>Tipo Documento</th>
</tr>`;

const tablaselectproveedores =  `<tr>
<th>Nombre</th>
<th>N° Doc</th>
<th>Correo</th>
</tr>`;

const tablaselectcuentas =  `<tr>
<th>Codigo</th>
<th>Descripcion</th>
</tr>`;
function stringtonumber(numero){
  let cambio = parseFloat(numero.replace(/[^0-9\.]+/g,''),10)
  if(numero == ''){
    cambio = 0
  }
  return cambio
}
function showalert(message, alerttype, icon) {
  let alerta = document.getElementById('alert_placeholder')
  alerta.innerHTML = `<div id="alertdiv" class="alert alert-dismissible fade show  ${alerttype}" role="alert"> <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" ><use xlink:href="${icon}"/></svg>
  <div style='display: inline'><span>${message}</span><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`

  setTimeout(function () { // this will automatically close the alert and remove this if the users doesnt close it in 5 secs


    document.getElementById("alertdiv").remove();

  }, 5000);
}

const tbody = document.querySelectorAll('#position tr');

let DOMModal = document.getElementById('modal1');
let modalElement = new bootstrap.Modal(DOMModal, {
  keyboard: false
});

for (var i = 1; i < tbody.length; i++) {
  tbody[i].addEventListener('click', function () {
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

  if (cartera == 'True') {
    cartera = true
  } else {
    cartera = false
  }
  if (tercero == 'True') {
    tercero = true
  } else {
    tercero = false
  }
  if (proveedor == 'True') {
    proveedor = true
  } else {
    proveedor = false
  }
  if (costo == 'True') {
    costo = true
  } else {
    costo = false
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
function habilitarmodalcuentas() {
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
buttonclose.addEventListener('click', function () {
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
const api_url_proveedores =
  "/api/v1.0/proveedores/";
const api_url_documentos =
  "/api/v1.0/documentoscontables/";
const api_url_cuentas =
  "/api/v1.0/carteras/";
async function sendapi(url, data, tabla, iddestino) {
  let a = await fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      response.json().then((result) => {
        
        if (response.ok) {
          loadtable(url, tabla, iddestino)
          loadtable(url, tabla, iddestino)
        }
        // alert(result.message)
        showalert(result.message, result.alerta,result.icon)
        
      })
      return response
      
    })
    .catch(error => console.log(error))
  return a.ok
}
// Defining async function
async function getapi(url) {

  let response = await fetch(url);

  return response

}
// Calling that async function

//getapi(api_url_proveedores);


loadtable(api_url_proveedores, tablaproveedores, "proveedores");
loadtable(api_url_documentos, tabladocumentos, "tabladocumentoscontables");
loadtable(api_url_cuentas, tablacuentas, "cuentas");

// Function to hide the loader
// function hideloader() {
// 	document.getElementById('loading').style.display = 'none';
// }
// Function to define innerHTML for HTML table

// Send to modify in the api
function modifyinapi(urlmodificar, tabla, data, id, urlactualizar) {

  fetch(urlmodificar, {
    method: 'PUT', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(response => {
    response.json().then((result) => {
      if (response.ok) {
        loadtable(urlactualizar, tabla, id)
      }
      showalert(result.message, result.alerta,result.icon)
    })
  })
}

function deleteapi(urldelete, tabla, id, urlactualizar) {
  fetch(urldelete, {
    method: 'DELETE', // or 'PUT'
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(response => {
    response.json().then((result) =>{
      if (response.ok) {
        loadtable(urlactualizar, tabla, id)
      }
      showalert(result.message, result.alerta,result.icon)
    })
  })
}
// Muestra la informacion de la api en la tabla previamente creada
function show(data, tabladestino, id) {
  let tab = tabladestino;
  if (id == "cuentas") {
    for (let r of data) {
      if (r.cartera == true) { r.cartera = '+'; } else { r.cartera = ''; }
      if (r.tercero == true) { r.tercero = '+'; } else { r.tercero = ''; }
      if (r.proveedor == true) { r.proveedor = '+'; } else { r.proveedor = ''; }
      if (r.centroCosto == true) { r.centroCosto = '+'; } else { r.centroCosto = ''; }
      tab += `<tr>
      <td>${r.serial}</td>
      <td>${r.descripcion}</td>
      <td>${r.cartera}</td>
      <td>${r.tercero}</td>
      <td>${r.proveedor}</td>
      <td>${r.centroCosto}</td>
      <td class="d-none">${r.parent_id}</td>
      <td class="d-none">${r.nivel}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
  if (id == "proveedores") {
    for (let r of data) {
      if(r.codigoPostal==null){r.codigoPostal=''}
      if(r.telefono==null){ r.telefono =''}
      tab += `<tr>
      <td data-pn="${r.primerNombre}" data-sn="${r.segundoNombre}" data-pa="${r.primerApellido}" data-sa="${r.segundoApellido}">${r.primerNombre} ${r.segundoNombre} ${r.primerApellido} ${r.segundoApellido} </td>
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
  if(id=="tableselectproveedores"){
    for (let r of data) {
      tab += `<tr>
      <td data-pn="${r.primerNombre}" data-sn="${r.segundoNombre}" data-pa="${r.primerApellido}" data-sa="${r.segundoApellido}">${r.primerNombre} ${r.segundoNombre} ${r.primerApellido} ${r.segundoApellido} </td>
      <td>${r.numDocumento}</td>
      <td>${r.correo}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
  if (id == "tableselectcuentas") {
    for (let r of data) {
      tab += `<tr>
      <td>${r.serial}</td>
      <td>${r.descripcion}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
  if (id == "tabladocumentoscontables") {
    for (let r of data) {
      tab += `<tr>
      <td>${r.fecha}</td>
      <td>${r.prefijo}</td>
      <td>${r.consecutivo}</td>
      <td>${r.descripcion}</td>
      <td>${r.tipodocumento}</td>
      <td class="d-none">${r.id}</td>
    </tr>`;
    }
  }
  // Setting innerHTML as tab variable
  document.getElementById(id).innerHTML = tab;
}

async function loadtable(url, tabladestino, id) {
  response = await getapi(url);
  if (response.ok != true) {
    alert('El objeto que esta buscando no se encuentra, revise la busqueda')
  }
  var data = await response.json();
  show(data, tabladestino, id);
  if (id == "cuentas") {
    cargarmodalcuentas()
  }
  if (id == "proveedores") {
    cargarmodalproveedores()
  }
  if(id == "tableselectproveedores"){
    selecttablaproveedores('inputtercero')
  }
  if(id == 'tableselectcuentas'){
    selecttablacuentas('inputcuenta')
  }
  if (id == "tabladocumentoscontables") {
    cargarmodaldocumentos()
  }
}
// Cargar la información de la tabla de cuentas al modal de modificación de cuentas
function cargarmodalcuentas() {
  const tbodysmodificarcuenta = document.querySelectorAll('#cuentas tr');

  let DOMModalmodificarcuenta = document.getElementById('modalmodificarcuenta');
  let modalElementsmodificarcuenta = new bootstrap.Modal(DOMModalmodificarcuenta, {
    keyboard: false
  });

  for (var i = 1; i < tbodysmodificarcuenta.length; i++) {
    tbodysmodificarcuenta[i].addEventListener('click', function (event) {
      modalElementsmodificarcuenta.show(this);
      console.log(event)
    });
    
  }
  DOMModalmodificarcuenta.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes

    let serial = button.childNodes[1].innerHTML
    let descripcion = button.childNodes[3].innerHTML
    let cartera = button.childNodes[5].innerHTML
    let tercero = button.childNodes[7].innerHTML
    let proveedor = button.childNodes[9].innerHTML
    let centrocosto = button.childNodes[11].innerHTML
    let parent_id = button.childNodes[13].innerHTML
    let nivel = button.childNodes[15].innerHTML
    let id = button.childNodes[17].innerHTML

    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    let modalSerial = DOMModalmodificarcuenta.querySelector('#serialmodificarcuenta')
    let modalDescripcion = DOMModalmodificarcuenta.querySelector('#descripcionmodificarcuenta')
    let modalCartera = DOMModalmodificarcuenta.querySelector('#carteramodificarcuenta')
    let modalTercero = DOMModalmodificarcuenta.querySelector('#terceromodificarcuenta')
    let modalProveedor = DOMModalmodificarcuenta.querySelector('#proveedormodificarcuenta')
    let modalCentroCosto = DOMModalmodificarcuenta.querySelector('#centrocostomodificarcuenta')
    let modalId = DOMModalmodificarcuenta.querySelector("#idcuentamodificar")

    //var modalBodyInput = DOMModal.querySelector('.modal-body input')
    modalSerial.value = serial
    modalDescripcion.value = descripcion
    modalCartera.checked = cartera
    modalTercero.checked = tercero
    modalProveedor.checked = proveedor
    modalCentroCosto.checked = centrocosto
    modalId.value = id

    let elements = document.querySelectorAll('#modalmodificarcuenta input');
    for (let e of elements) {
      e.disabled = true
    }
    //modalBodyInput.value = recipient
  })
}

//Cargar la informacion de los proveedores(api) que esta en la tabla al modal emergente
function cargarmodalproveedores() {
  const tbodys = document.querySelectorAll('#proveedores tr');

  let DOMModals = document.getElementById('modalmodificarproveedor');
  console.log(tbodys);
  let modalElements = new bootstrap.Modal(DOMModals, {
    keyboard: false
  });

  for (var i = 1; i < tbodys.length; i++) {
    tbodys[i].addEventListener('click', function () {
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
    let modalId = DOMModals.querySelector("#idproveedormodificar")

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

function cargarmodaldocumentos() {
  const tbodyss = document.querySelectorAll('#tabladocumentoscontables tr');

  let DOMModals = document.getElementById('modalmodificardocumentocontable');
  console.log(tbodyss);
  let modalElements = new bootstrap.Modal(DOMModals, {
    keyboard: false
  });

  for (var i = 1; i < tbodyss.length; i++) {
    tbodyss[i].addEventListener('click', function () {
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
    let tipodocumento = button.childNodes[9].innerHTML
    let id = button.childNodes[11].innerHTML

    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    let modalPrefijo = DOMModals.querySelector('#prefijodocumentom')
    let modalConsecutivo = DOMModals.querySelector('#consecutivodocumentom')
    let modalDescripcion = DOMModals.querySelector('#descripciondocumentom')
    let modalFecha = DOMModals.querySelector('#fechadocumentom')
    let modalTipoDocumento = DOMModals.querySelector('#tipodocumentom')
    let modalid = DOMModals.querySelector('#iddocumentomodificar')

    //var modalBodyInput = DOMModal.querySelector('.modal-body input')
    modalPrefijo.value = prefijo
    modalConsecutivo.value = consecutivo
    modalDescripcion.value = descripcion
    modalFecha.value = fecha
    modalTipoDocumento.value = tipodocumento
    modalid.value = id
    //modalBodyInput.value = recipient

  })
}// Activar el campo tipo dependiendo de la cuenta
let serialcuenta = document.getElementById('serialnuevacuenta')
serialcuenta.addEventListener('change', function(){
  let tipocuenta = document.getElementById('tipocuenta')
  let label = document.getElementById('labeltipocuenta')
  if(serialcuenta.value.length == 1){
    tipocuenta.style.display = 'block'
    label.style.display = 'block'
  }else{
    tipocuenta.style.display = 'none'
    label.style.display = 'none'
  }
})
// Enviar la info de la cuenta a la api para crearla
let buttonenviarcuenta = document.getElementById('enviarcuentaform')
buttonenviarcuenta.addEventListener('submit', async function (event) {
  let serial1 = document.getElementById('serialnuevacuenta').value
  let descripcion1 = document.getElementById('descripcionnuevacuenta').value
  let cartera1 = document.getElementById('carteranuevacuenta').checked
  let tercero1 = document.getElementById('terceronuevacuenta').checked
  let proveedor1 = document.getElementById('proveedornuevacuenta').checked
  let centrocosto1 = document.getElementById('centrocostonuevacuenta').checked
  let naturaleza1 = 0;
  if(document.getElementById('radiodebito').checked) {
    naturaleza1 = 0;
  }else if(document.getElementById('radiocredito').checked) {
    naturaleza1 = 1;
  }
  let tipocuenta1 = document.getElementById('tipocuenta').value

  let data = {
    serial: serial1, descripcion: descripcion1, cartera: cartera1, tercero: tercero1,
    proveedor: proveedor1, centroCosto: centrocosto1, naturaleza: naturaleza1, tipo: tipocuenta1 
  }
  event.preventDefault();
  let ok = await sendapi(api_url_cuentas, data, tablacuentas, 'cuentas')
  console.log(ok)
  if(ok == true){
  let all = document.querySelectorAll('#modalnewcuenta input');
  all.forEach(function (allelements) {
    allelements.value = ""
    allelements.checked = false
  })
  }
  
})
// Buscar cuenta
let buttonbuscarcuenta = document.getElementById('buttonbuscarcuenta')
buttonbuscarcuenta.addEventListener('click', function () {
  buscar('textbuscarcuenta','selectparametrobuscarcuenta', '/api/v1.0/carteras/', tablacuentas, "cuentas");
})

document.querySelector('#textbuscarcuenta').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    buscar('textbuscarcuenta','selectparametrobuscarcuenta', '/api/v1.0/carteras/', tablacuentas, "cuentas");
  }
});
// Boton Modificar en el modal para habilitar los campos de edicion
let buttonmodificarcuenta = document.getElementById('modificarcuenta')
buttonmodificarcuenta.addEventListener('click', function () {
  let allinputs = document.querySelectorAll('#modalmodificarcuenta input');
  allinputs.forEach(function (allelements) {
    allelements.disabled = false
  })
  allinputs[0].disabled = true
})

// Boton de guardar para guardar los datos realizados en la modificacion
let buttonguardarcuenta = document.getElementById('modificarcuentaform')
buttonguardarcuenta.addEventListener('submit', function (event) {
  let descripcion1 = document.getElementById('descripcionmodificarcuenta').value
  let cartera1 = document.getElementById('carteramodificarcuenta').checked
  let tercero1 = document.getElementById('terceromodificarcuenta').checked
  let proveedor1 = document.getElementById('proveedormodificarcuenta').checked
  let centrocosto1 = document.getElementById('centrocostomodificarcuenta').checked
  let id1 = document.getElementById('idcuentamodificar').value
  let data = {
    descripcion: descripcion1, cartera: cartera1, tercero: tercero1,
    proveedor: proveedor1, centroCosto: centrocosto1
  }
  let url = '/api/v1.0/cartera/'.concat(id1)

  modifyinapi(url, tablacuentas, data, "cuentas", api_url_cuentas)
  let modal = document.getElementById('modalmodificarcuenta')
  let modalinstance = bootstrap.Modal.getInstance(modal)
  
  modalinstance.hide()
  event.preventDefault()
  
})
//Boton de eliminar cuenta en el mismo modal de cuentas
let buttondeletecuenta = document.querySelector('#modalmodificarcuenta .btn-delete')
buttondeletecuenta.addEventListener('click',function(){
  deletemodal('#modalmodificarcuenta','cuentas')
})
//Modal de confirmar eliminacion
let buttonBorrar = document.querySelector('#modaldelete .btn-confirm')
buttonBorrar.addEventListener('click', function () {
  let from = buttonBorrar.getAttribute('from')
  if(from=='cuentas'){
    deleteobject('idcuentamodificar', '/api/v1.0/cartera/',tablacuentas, from,api_url_cuentas)
  }else if(from=='proveedores'){
    deleteobject('idproveedormodificar', '/api/v1.0/proveedor/',tablaproveedores, from,api_url_proveedores)
  }
  else if(from ='tabladocumentoscontables'){
    deleteobject('iddocumentomodificar', '/api/v1.0/documentocontable/',tabladocumentos, from,api_url_documentos)
  }
});


// Enviar la info del proveedor para crearlo
let buttonEnviar = document.getElementById('enviarproveedorform')
buttonEnviar.addEventListener('submit', async function (event) {
  let primerNombre1 = document.getElementById('primerNombre').value
  let primerApellido1 = document.getElementById('primerApellido').value
  let numDocumento1 = document.getElementById('numDocumento').value

    let segundoNombre1 = document.getElementById('segundoNombre').value
    let segundoApellido1 = document.getElementById('segundoApellido').value
    let tipoDocumento1 = document.getElementById('tipoDocumento').value
    let correo1 = document.getElementById('correo').value
    let pais1 = document.getElementById('pais').value
    let departamento1 = document.getElementById('departamento').value
    let municipio1 = document.getElementById('municipio').value
    let direccion1 = document.getElementById('direccion').value
    let codigoPostal1 = document.getElementById('codigoPostal').value
    let telefono1 = document.getElementById('telefono').value
    if (codigoPostal1 == '') { codigoPostal1 = null }
    if (telefono1 == '') { telefono1 = null }
    let data = {
      primerNombre: primerNombre1, segundoNombre: segundoNombre1, primerApellido: primerApellido1,
      segundoApellido: segundoApellido1, tipoDocumento: tipoDocumento1, numDocumento: numDocumento1,
      correo: correo1, pais: pais1, departamento: departamento1, municipio: municipio1, direccion: direccion1, codigoPostal: codigoPostal1, telefono: telefono1
    }
    event.preventDefault()
    let ok = await sendapi(api_url_proveedores, data, tablaproveedores, "proveedores");

    if(ok == true){
      let all = document.querySelectorAll('#modalnewproveedor input');
      all.forEach(function (allelements) {
        allelements.value = ""
        allelements.checked = false
      })
    }
})
// Boton para modificar proveedores en el modal de proveedor
let buttonModificarProveedor = document.getElementById('modificarProveedor')
buttonModificarProveedor.addEventListener('click', function () {
  let allinputs = document.querySelectorAll('#modalmodificarproveedor input');
  allinputs.forEach(function (allelements) {
    allelements.disabled = false
  })
  allinputs[4].disabled = true
})
// Guardar la info de proveedor en el modal de modificar
let buttonGuardarProveedor = document.getElementById('guardarProveedor')
buttonGuardarProveedor.addEventListener('click', function () {
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
  let id1 = document.getElementById('idproveedormodificar').value
  console.log(codigoPostal1=='')
  if (codigoPostal1 == '') { codigoPostal1 = null }
  if (telefono1 == '') { telefono1 = null }
  let data = {
    primerNombre: primerNombre1, segundoNombre: segundoNombre1, primerApellido: primerApellido1,
    segundoApellido: segundoApellido1, tipoDocumento: tipoDocumento1, numDocumento: numDocumento1,
    correo: correo1, pais: pais1, departamento: departamento1, municipio: municipio1, direccion: direccion1, codigoPostal: codigoPostal1, telefono: telefono1
  }
  let url = '/api/v1.0/proveedor/'.concat(id1)
  modifyinapi(url, tablaproveedores, data, "proveedores", api_url_proveedores);
});
//Boton de eliminar proveedor en el mismo modal de proveedor
let buttondeleteproveedor = document.querySelector('#modalmodificarproveedor .btn-delete')
buttondeleteproveedor.addEventListener('click',function(){
  deletemodal('#modalmodificarproveedor','proveedores')
})

function deletemodal(idmodal, idtable){
  let buttonback = document.getElementById('buttonback')
  let buttondelete = document.querySelector('#modaldelete .btn-confirm')
  buttonback.setAttribute("data-bs-target",idmodal)
  buttondelete.setAttribute('from',idtable)
}
function deleteobject(iddelete, urldelete, tabla, idtabla, urlactualizar){
  let id1 = document.getElementById(iddelete).value
  let url = urldelete.concat(id1)
  deleteapi(url, tabla, idtabla, urlactualizar);
}
// Bloquea los campos del modal de proveedores cuando se cierra
let modalmodificarproveedor = document.getElementById('modalmodificarproveedor')
modalmodificarproveedor.addEventListener('hidden.bs.modal', function () {
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
buttonbuscar.addEventListener('click', function () {
  buscar('textbuscar', 'selectparametrobuscarproveedor', '/api/v1.0/proveedores/', tablaproveedores,"proveedores");
})

document.querySelector('#textbuscar').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    buscar('textbuscar','selectparametrobuscarproveedor', '/api/v1.0/proveedores/', tablaproveedores,"proveedores");
  }
});

function buscar(idtextobuscar,idselectparametrobuscar, url, tabla, idtabla) {
  let buscar = document.getElementById(idtextobuscar)
  let selectparametrobuscar = document.getElementById(idselectparametrobuscar)
  if (buscar.innerHTML != null) {
    if(selectparametrobuscar.value=='nombre'){
      dato = '?nombre='+buscar.value
    }
    else if(selectparametrobuscar.value=='numero'){
      dato ='?numero='+buscar.value
    }
    else if(selectparametrobuscar.value == 'codigo'){
      dato = '?codigo='+ buscar.value
      if(idselectparametrobuscar=='selectparametrobuscarcuentaform'){
        dato+='&childs=1'
      }
    }
    else if(selectparametrobuscar.value == 'descripcion'){
      dato = '?descripcion='+ buscar.value
      if(idselectparametrobuscar=='selectparametrobuscarcuentaform'){
        dato+='&childs=1'
      }
    }
    console.log(dato)
    loadtable(url + dato, tabla, idtabla)
  } else {

  }
}

// Buscar proveedor en form boton + tecla
let buttonbuscarproveedorform = document.getElementById('buscarproveedorform')
buttonbuscarproveedorform.addEventListener('click', function () {
  buscar('textbuscarproveedorform', 'selectparametrobuscarproveedorform','/api/v1.0/proveedores/', tablaselectproveedores,"tableselectproveedores");
})

let textbuscarproveedorform = document.getElementById('textbuscarproveedorform')
textbuscarproveedorform.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    buscar('textbuscarproveedorform', 'selectparametrobuscarproveedorform', '/api/v1.0/proveedores/', tablaselectproveedores,"tableselectproveedores");
  }
});
// Buscar cuenta en form boton + tecla
let buttonbuscarselectcuenta = document.getElementById('buttonbuscarcuentaform')
buttonbuscarselectcuenta.addEventListener('click', function () {
  buscar('textbuscarcuentaform', 'selectparametrobuscarcuentaform', '/api/v1.0/carteras/', tablaselectcuentas,"tableselectcuentas");
})

document.querySelector('#textbuscarcuentaform').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    buscar('textbuscarcuentaform', 'selectparametrobuscarcuentaform', '/api/v1.0/carteras/', tablaselectcuentas,"tableselectcuentas");
  }
});


// Modal Crear Documento Contable
let buttonEnviarNuevoDocumento = document.getElementById('enviarnuevodocumento')
buttonEnviarNuevoDocumento.addEventListener('click', function () {
  let prefijo1 = document.getElementById('prefijonuevodocumento').value
  let consecutivo1 = document.getElementById('consecutivonuevodocumento').value
  let descripcion1 = document.getElementById('descripcionnuevodocumento').value
  fecha1 = '0001-01-01'
  let tipodocumento1 = document.getElementById('tiponuevodocumento').value
  let plantilla1 = document.getElementById('plantillanuevodocumento').value
  console.log(plantilla1)
  let data = { fecha: fecha1, consecutivo: consecutivo1, descripcion: descripcion1, prefijo: prefijo1, tipodocumento: tipodocumento1, plantilla: plantilla1 }

  sendapi('/api/v1.0/documentoscontables/', data, tabladocumentos, "tabladocumentoscontables");
})
//Modificar Documento contable
let buttonmodificardocumento = document.getElementById('modificardocumentom')
buttonmodificardocumento.addEventListener('click',function(){
  let allinputs = document.querySelectorAll('#modalmodificardocumentocontable input, #modalmodificardocumentocontable select')
  allinputs.forEach(function(allelements){
    allelements.disabled= false
  })
})
// Modal guardar Documento contable

let buttonguardardocumento = document.getElementById('modificardocumentosform')
buttonguardardocumento.addEventListener('submit', function (event) {
  let prefijo1 = document.getElementById('prefijodocumentom').value
  console.log(prefijo1)
  let consecutivo1 = document.getElementById('consecutivodocumentom').value
  let descripcion1 = document.getElementById('descripciondocumentom').value
  let fecha1 = document.getElementById('fechadocumentom').value
  let id1 = document.getElementById('iddocumentomodificar').value
  let tipodocumento1 = document.getElementById('tipodocumentom').value

  let data = { fecha: fecha1, consecutivo: consecutivo1, descripcion: descripcion1, prefijo: prefijo1, tipodocumento:tipodocumento1 }
  let url = '/api/v1.0/documentocontable/'.concat(id1)
  modifyinapi(url,tabladocumentos,data,'tabladocumentoscontables',api_url_documentos)
  event.preventDefault()
})
// Boton eliminar documento en el mismo modal
let buttondeletedocumento = document.querySelector('#modalmodificardocumentocontable')
buttondeletedocumento.addEventListener('click', function(){
  deletemodal('#modalmodificardocumentocontable','tabladocumentoscontables')
})
// Bloquear campos del modal de documentos cunado se cierra
let modalmodificardocumentocontable = document.getElementById('modalmodificardocumentocontable')
modalmodificardocumentocontable.addEventListener('hidden.bs.modal', function(){
  let all = document.querySelectorAll('#modalmodificardocumentocontable input, #modalmodificardocumentocontable select')
  all.forEach(function(allelements){
    allelements.disabled=true
  })
})
let buttonnuevoregistro = document.getElementById('buttonregistrodocumento')
buttonnuevoregistro.addEventListener('click', async function(){
  let selecttipodocumento = document.getElementById('selecttipodocumento')
  selecttipodocumento.innerHTML=''
  var optempty = document.createElement('option')
  selecttipodocumento.appendChild(optempty)
  response = await getapi(api_url_documentos)
  documentosarray = await response.json()
  console.log(documentosarray)
  for(var i = 0; i < documentosarray.length;i++){
    var opt = document.createElement('option')
    opt.value = documentosarray[i]['id']
    date = document.createAttribute('date')
    consecutivo = document.createAttribute('consecutivo')
    consecutivo.value = documentosarray[i]['consecutivo']
    date.value = documentosarray[i]['fecha']
    opt.setAttributeNode(date)
    opt.setAttributeNode(consecutivo)
    opt.innerHTML = `${documentosarray[i]['descripcion']}      ${documentosarray[i]['prefijo']}`
    selecttipodocumento.appendChild(opt)
  }
})
let selecttipodocumento = document.getElementById('selecttipodocumento')
selecttipodocumento.addEventListener('click', function(){
  let inputfecha =  document.getElementById('tipofecha')
  let inputconsecutivo =document.getElementById('tipoconsecutivo')
  inputconsecutivo.value = Number(selecttipodocumento.selectedOptions[0].getAttribute('consecutivo'))+1
  inputfecha.value = selecttipodocumento.selectedOptions[0].getAttribute('date')
})
// Seleccionar proveedor en el modal de registro
let selectproveedor = document.getElementById('buttonproveedores')
selectproveedor.addEventListener('click', async function(){
  botonseleccionarproveedoresinput(this.getAttribute('target'))
})
let inputtercero = document.getElementById('inputtercero')
inputtercero.addEventListener('click', async function(){
  botonseleccionarproveedoresinput(this.getAttribute('target'))
})
let inputcuenta = document.getElementById('inputcuenta')
inputcuenta.addEventListener('click', async function(){
  botonseleccionarcuentasinput(this.id)
  console.log(this.id)
})
// Carga la tabla de proveedores del modal selectproveedores 
async function botonseleccionarproveedoresinput(id){
  let response = await getapi(api_url_proveedores);
  let data = await response.json()
  show(data, tablaselectproveedores, "tableselectproveedores")
  selecttablaproveedores(id)
}
async function botonseleccionarcuentasinput(id){
  let response = await getapi(api_url_cuentas + "?childs=1")
  let data = await response.json()
  show(data, tablaselectcuentas, "tableselectcuentas")
  selecttablacuentas(id)
} 
// Hace que la tabla de proveedores del modal select proveedores sea clickeable
function selecttablaproveedores(id){
const tbodyselectproveedores = document.querySelectorAll('#tableselectproveedores tr')
for(var i = 1; i < tbodyselectproveedores.length; i++){
  tbodyselectproveedores[i].addEventListener('dblclick', function(){
      let proveedorseleccionado = document.getElementById(id)
      let inputtercero = document.getElementById('inputtercero')
      let DOMModalnuevoregistro = document.getElementById('modalnuevoregistrodocumentos')
      let DOMModalModal2 = document.getElementById('myModal2')
      let modalbackdrop2 = document.getElementsByClassName('modal-backdrop')
      let modalElementsModal2 = new bootstrap.Modal(DOMModalModal2,{
        keyboard: false
      })
      let modalElementsnuevoregistro = new bootstrap.Modal(DOMModalnuevoregistro, {
        keyboard: false
      })
      
      modalElementsModal2._hideModal()
      modalbackdrop2[0].remove()
      modalElementsnuevoregistro.show()
      nombreproveedor = this.children[0].innerHTML
      idproveedor = this.children[3].innerHTML
      id = document.createAttribute('id_proveedor')
      id.value = idproveedor
      proveedorseleccionado.setAttributeNode(id)
      proveedorseleccionado.value= nombreproveedor
      if(id == 'proveedorseleccionado'){
        inputtercero.value = nombreproveedor
      }
    })
  }
}
function selecttablacuentas(id){
  const tbodyselectcuentas = document.querySelectorAll('#tableselectcuentas tr')
  for(var i = 1; i < tbodyselectcuentas.length; i++){
    tbodyselectcuentas[i].addEventListener('dblclick', function(){
        let cuentaseleccionada = document.getElementById(id)
        let DOMModalnuevoregistro = document.getElementById('modalnuevoregistrodocumentos')
        let DOMModalModal2 = document.getElementById('modalselectcuenta')
        let modalbackdrop2 = document.getElementsByClassName('modal-backdrop')
        let modalElementsModal2 = new bootstrap.Modal(DOMModalModal2,{
          keyboard: false
        })
        let modalElementsnuevoregistro = new bootstrap.Modal(DOMModalnuevoregistro, {
          keyboard: false
        })
        
        modalElementsModal2._hideModal()
        modalbackdrop2[0].remove()
        modalElementsnuevoregistro.show()
        codigocuenta = this.children[0].innerHTML
        idcuenta = this.children[2].innerHTML
        id = document.createAttribute('id_cuenta')
        id.value = idcuenta
        cuentaseleccionada.setAttributeNode(id)
        cuentaseleccionada.value= codigocuenta 
      })
    }
  }
// Pone la observacion general de modal registro en la tabla 
let inputobservaciones = document.getElementById('observacionesregistro')
inputobservaciones.addEventListener('change',function(){
  let inputdescripcion = document.getElementById('inputdescripcion')
  inputdescripcion.value=inputobservaciones.value
})
// Le da el formato de peso a los numeros
function formatopeso(numero){
  let formatocolombia = new Intl.NumberFormat('en-US',{
    style: 'currency',
    currency: 'USD',
  });
  
  let number = parseFloat(numero.replace(/[^0-9\.]+/g,''),10)
  let a = formatocolombia.format(number)
  if (a=='$NaN'){
    a='0'
  }
  return a
}
let inputvalorbase = document.getElementById('inputvalorbase')
inputvalorbase.addEventListener('change',function(){
  
  this.value = formatopeso(this.value)
  
})
let inputvalortotal = document.getElementById('inputvalortotal')
inputvalortotal.addEventListener('change',function(){
  this.value = formatopeso(this.value)
})
let porcentajevalor = document.getElementById('porcentajevalor')
porcentajevalor.addEventListener('change',function(){
  let numero = document.getElementById('inputvalorbase').value
  numero = stringtonumber(numero)
  porcentaje = parseFloat(this.value)/100
  let valortotal = document.getElementById('inputvalortotal')
  let valorfinal = Math.round(numero*porcentaje)
  valortotal.value = formatopeso(valorfinal.toString())
})
// llenar la tabla de filas
let formregistro = document.getElementById('buttonsend')
function llenartablaregistro(e){
  e.preventDefault();
  let tbodydocuments = document.querySelector('#tableregistrodocumentos tbody')
  let cuenta = document.getElementById('inputcuenta').value
  let idcuenta = document.getElementById('inputcuenta').getAttribute('id_cuenta')
  let descripcion = document.getElementById('inputdescripcion').value
  let proveedor = document.getElementById('inputtercero').value
  let id_proveedor = document.getElementById('inputtercero').getAttribute('id_proveedor')
  let debitocredito = document.getElementById('debitocredito').value
  let valorbase = document.getElementById('inputvalorbase').value
  let porcentaje = document.getElementById('porcentajevalor').value
  let valortotal = document.getElementById('inputvalortotal').value
  let tr = document.createElement("tr")
  tr.innerHTML= `
  <th id_cuenta='${idcuenta}'>${cuenta}</th>
  <th>${descripcion}</th>
  <th id_proveedor = '${id_proveedor}'>${proveedor}</th>
  <th>${debitocredito}</th>
  <th>${valorbase}</th>
  <th>${porcentaje}</th>
  <th>${valortotal}</th>
  <th></th>
  <th></th>
  <th><button class ="btn-delete btn-danger btn" onclick="deleterow(this)">-</button></th>`;
  tbodydocuments.appendChild(tr);
}
// Traer valores debitos o creditos y sumarlos
function sumarvalores(){
  let debitos = document.getElementById('sumadebitosregistro')
  let creditos = document.getElementById('sumacreditosregistro')
  let tipo = document.getElementById('debitocredito')
  let valor = document.getElementById('inputvalortotal')
  tipo = tipo.value
  if(tipo == 'debito'){
    
    let numerodebito = stringtonumber(valor.value) + stringtonumber(debitos.value)
    debitos.value = formatopeso(numerodebito.toString())
  }
  else{
    let numerocredito = stringtonumber(valor.value) + stringtonumber(creditos.value)
    creditos.value = formatopeso(numerocredito.toString())
  }

}
formregistro.addEventListener('click', llenartablaregistro);
formregistro.addEventListener('click',sumarvalores)
// document.getElementById('debitocredito').options[document.getElementById('debitocredito').selectedIndex].text
function deleterow(event){
  // event.target will be the input element.
  let debitos = document.getElementById('sumadebitosregistro')
  let creditos = document.getElementById('sumacreditosregistro')
  let td = event.parentNode; 
  let tr = td.parentNode; // the row to be removed
  let tipo = tr.childNodes[7].innerHTML
  let valor = tr.childNodes[13].innerHTML
  if(tipo == 'debito'){
    
    let numerodebito = stringtonumber(debitos.value) - stringtonumber(valor) 
    debitos.value = formatopeso(numerodebito.toString())
  }
  else{
    let numerocredito = stringtonumber(creditos.value) - stringtonumber(valor.value) 
    creditos.value = formatopeso(numerocredito.toString())
  }
  tr.parentNode.removeChild(tr);
}
async function createasientos(){
  let tablaregistro = document.getElementById('tableregistrodocumentos');
  let tbody = tablaregistro.children[1].children;
  let asientos = Array.from(tbody);
  let contador = 0;
  let data = []
  for (let index = 1; index < asientos.length; index++) {
    datos = asientos[index].children;
    // let asien = new Asiento(datos[0].getAttribute('id_cuenta'), datos[1].innerHTML, datos[2].getAttribute('id_proveedor'), datos[3].innerHTML, datos[4].innerHTML, datos[5].innerHTML, datos[6].innerHTML, datos[7].innerHTML, datos[8].innerHTML)
    let asien = new Asiento('27', 'gdhasgdh', '37', '0', '5454', '454', '454', '454', '5615')
    data.push(asien)
  }
  console.log(data)
  console.log(data[0])
  let a = await fetch('/api/v1.0/asientos/', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers: {
      'Content-Type': 'application/json'
    }
  })
}
async function createregistros(){
  
  let tipodocumento = document.getElementById('selecttipodocumento')
  let consecutivo = document.getElementById('tipoconsecutivo')
  let fecha = document.getElementById('tipofecha')
  let proveedor = document.getElementById('proveedorseleccionado')
  let observaciones = document.getElementById('observacionesregistro')
  let regis = new Registro(tipodocumento.value, consecutivo.value, fecha.value, proveedor.getAttribute('id_proveedor'), observaciones.value)
  let data = regis
  let id_registro;
  let a = await fetch('/api/v1.0/registros/', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((response) => {
    response.json().then((result) => {
      // alert(result.message)
      showalert(result.message, result.alerta,result.icon)
      console.log(result.id)
      id_registro=result.id
      return result.id
    })
    
    
  })
  console.log(id_registro)
}
class Registro{
  constructor(documentocontable, consecutivo, fecha, proveedor, observaciones){
    this.id_documentocontable = documentocontable;
    this.consecutivo = consecutivo;
    this.fecha = fecha;
    this.id_proveedor = proveedor;
    this.observaciones = observaciones;
  }
}
class Asiento {
  constructor(cuenta, descripcion, tercero, debitocredito, valorbase, porcentaje, valortotal, formadepago, ccosto) {
    this.id_registro = '3';
    this.id_cuenta = cuenta;
    this.descripcion = descripcion;
    this.id_proveedor = tercero;
    this.debitocredito = debitocredito;
    this.valorbase = valorbase;
    this.porcentaje = porcentaje;
    this.valortotal = valortotal;
    this.id_formapago = formadepago;
    this.id_centrocosto = ccosto;
  }
}