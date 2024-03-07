// const net = require('net');


// net.createServer(socket => {
    
//     socket.on('data',data => {
//         // console.log('He recibido algo')
//         socket.write('Hola')
//     })
// }).listen(3000);
// const express = require('express');

// const app = express()

// app.use((req,resp,next) => {

//     resp.send('Hola mundo');

// })

// app.listen(3000);
const express = require('express');

let coches = [
    {
        id: 1,
        marca : 'seat',
        modelo : 'ibiza'
    },
    {
        id : 2,
        marca : 'ferrari',
        modelo : 'amarillo'
    }

]
const app = express();
app.use(express.json());



app.get('/',indicePag);
app.get('/coches',getCoches);
app.post('/coches',createCoches);

function indicePag(req, res, next) {
    let pagina = `
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Coches</title>
        </head>
        <body>
            <p>Mas coches</p>
            <a href="/coches">fotos de cohches</a>
            <form action="/coches" method="POST">
        <label for="">Marca</label>
        <input type="text" name="marca" id="">
        <label for="">Modelo</label>
        <input type="text" name="modelo">
        <input type="submit">
    </form>

        </body>
        </html>
    `
    res.send(pagina)
}

app.listen(80);

function getCoches(req,res,next) {
    let pagina = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Coches</title>
        </head>
        <body>
            <h1>Coches de carretas</h1>
            <ul>
            ${
                (() => {
                    let loopresult = '';
                    for (let coche of coches) {
                        loopresult += `<li> El coche es un <a href='/coches/${coche.id}> ${coche.marca} </a> </li>`;
                    }
                    return loopresult;
                }) ()
            }
             </ul>
        </body>
        </html>
    `
    res.send(pagina)
}
