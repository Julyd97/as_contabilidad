
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
