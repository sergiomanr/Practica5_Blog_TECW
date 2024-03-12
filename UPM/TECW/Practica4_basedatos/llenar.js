const fs = require('fs');
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
        return `./images/${receta.photo}`
    } else {
        return '/none.jpg'
    }
    
}

const llenar = async () => {
    try {
        await sequelize.sync({force: true});
        const Recetas = JSON.parse(await fs.promises.readFile('./recipes.json', 'utf-8'));
        for (let receta of Recetas) {
                const nuevoAttachments = await Attachments.create({
                    mime: receta.mime,
                    url: foto(receta)
                })

                const nuevoPost = await Posts.create({
                    title: receta.title,
                    body: rellenar_body(receta.ingredients, receta.steps),
                    attachmentId: nuevoAttachments.id
                });
        }
    } catch (error) {
        console.log(`Upsi ha habido un error ${error}  `)
    }
}
llenar();
