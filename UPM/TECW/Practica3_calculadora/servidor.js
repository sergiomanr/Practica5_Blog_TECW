const express = require("express");
const app = express();

app.listen(3001,() => {
    console.log('Servidor activo')
});

app.use(express.static('calculadora'));
app.use(express.urlencoded({extended: true}));


app.post('/cuadrado',cuadrado);
app.post('/raiz',raiz);
app.post('/factorial',factorial);



function factorial(req, res, next) {
    num = req.body.numero;
    let sol = 1;
    if (num === 1 || num === 0) {
        sol = 1
    }

    for (let i = 2; i <= num ; i++) {
        sol *= i
    }
    res.send(sol.toString());
}

function raiz(req, res, next) {
    var sol = Math.round(Math.sqrt(req.body.numero) * 1000) / 1000;
    res.send(sol.toString());
}

function cuadrado(req, res, next) {
        var sol = Math.pow(req.body.numero,2);
        res.send(sol.toString());
}
    


function validar(valor) {
    if (!isNaN(valor)) {
        return true;
    } else {
        escribirPantalla('Error');
    }
}