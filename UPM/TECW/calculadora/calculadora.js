const leerPantalla = () => document.getElementById('pantalla').value;
const escribirPantalla = v => document.getElementById('pantalla').value = v;


var num1 = 0;
var operador = '';
var llave = false;
let boton_C = document.getElementById('clear');
let boton_AC = document.getElementById('acumulated_clear');



// function fact() {
//         let sol = 1;
//         if (num === 1 || num === 0) {
//             sol = 1
//         }

//         for (let i = 2; i <= num ; i++) {
//             sol *= i
//         }
// }

// function sq() {
//     if (validar(leerPantalla())) {
//         sol = Math.pow(Number(leerPantalla()),2)
//         escribirPantalla(sol);
//     }
//     console.log('entra %d',sol)
    
// }

// function sqr() {
//     if (validar(leerPantalla())) {
//     escribirPantalla( Math.round(Math.sqrt(leerPantalla()) * 1000) / 1000)
// }}

function fact() {
    var num = leerPantalla();
    if (validar(leerPantalla())) {

        fetch('/factorial', {
                        method: "POST",
                        headers: {"Content-Type": "application/x-www-form-urlencoded"},
                        body: `numero=${num}`})         
        .then(res => res.text()).then(sol => escribirPantalla(sol) && actualizar_h2());
                    }}



 function sq() {
    var num = leerPantalla();
    if (validar(num)) {
        fetch('/cuadrado', {
                            method: "POST",
                            headers: {"Content-Type": "application/x-www-form-urlencoded"},
                            body: `numero=${num}`})                    
        .then(res => res.text()).then(sol => escribirPantalla(sol) && actualizar_h2() );
    }   
}
function sqr(){
    var num = leerPantalla()
    if (validar(num)) {
        console.log('Entramos en raiz de calc.js con %d',num);
        fetch('/raiz', {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `numero=${num}`})
        .then(res => res.text()).then(sol => escribirPantalla(sol) && actualizar_h2())
    }

}

function add() {
    num1 = leerPantalla()
    operador = 'suma'
    escribirPantalla("")
    llave = true
}
function sub() {
    num1 = leerPantalla()
    operador = 'resta'
    escribirPantalla("")
    llave = true
}
function mul() {
    num1 = leerPantalla()
    operador = 'mult'
    escribirPantalla("")
    llave = true
}
function div() {
    num1 = leerPantalla()
    operador = 'division'
    escribirPantalla("")
    llave = true
}

function actualizar_h2() {
    let txt_h2 = document.getElementById('info')
    let res = leerPantalla()
    if (res < 100) {
        txt_h2.textContent = 'Info: El resultado es menor que 100';
    } else if ( res >= 100 && res < 200 ) {
        txt_h2.textContent = 'Info: El resultado está entre 100 y 200';
    } else if ( res >= 200 ) {
        txt_h2.textContent = 'Info: El resultado es superior a 200';
    }
     
}

function eq() {
    while (llave) {
        llave = false
        if (operador === 'suma') {
            sol = parseFloat(num1) + parseFloat(leerPantalla());
            escribirPantalla(Math.round(sol * 1000) / 1000);

        } else if (operador === 'resta') {
            sol = num1 - leerPantalla();
            escribirPantalla(Math.round(sol * 1000) / 1000);

        } else if (operador === 'mult') {
            sol = num1*leerPantalla();
            escribirPantalla(Math.round(sol * 1000) / 1000);

        } else if (operador === 'division') {
            sol = num1/leerPantalla()
            escribirPantalla(Math.round(sol * 1000) / 1000)
            }
        else if (operador === ''){
            escribirPantalla(0)
        }
        actualizar_h2()
        console.log('Operador es %s',operador)
    }
}

function validar(valor) {
    if (!isNaN(valor)) {
        return true
    } else {
        escribirPantalla('Error')
    }
}
function clearScreen() {
    escribirPantalla(0)
}
function clearAll() {
    escribirPantalla(0)
    operador = ''
    llave = false
    console.log('Operador es %s',operador)
}
// boton_C.addEventListener('click', function() {
//     return clearScreen()
// })