const fs = require('fs');
const Sequelize = require('sequelize');
const { Posts, Attachments, sequelize } = require('./crear');

function rellenar_body(ingr, steps) {
    let body = '\n# Ingredientes'
    for (i of ingr) {
        body += `\n* ${i}`
    }
    body += '\n\n# Pasos'
    for (s of steps) {
        body += `\n* ${s}`
    }
    
    return body;
}
function foto(receta) {
    
    if (receta.photo){
        return receta.photo
    } else {
        return '/none.jpg'
    }
    
}

fs.readFile('./recipes.json', 'utf-8', (err, data) => {
  try {
    const Recetas = JSON.parse(data);

    for (const receta of Recetas) {
    const nuevoAttachments = new Attachments({
        mime: receta.mime,
        url: foto(receta)
    })
    const nuevoPost = new Posts({
        title: receta.title,
        body: rellenar_body(receta.ingredients, receta.steps),
        attachmentId: nuevoAttachments.id

    });
    // console.log(`Los ingredientes y paso de ${receta.title} son ${rellenar_body(receta.ingredients, receta.steps) } \n`)
    // nuevoPost.save().then(() => {
    //   console.log(`Receta ${receta.title} ha sido añadida`);
    // });
  }
  } catch (error) {
    console.log(`Upsi ha habido un error ${error}  `)
  }
});
