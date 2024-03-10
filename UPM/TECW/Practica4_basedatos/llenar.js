const fs = require('fs');
const { Posts, Attachments, sequelize } = require('./crear');
// const sequelize = require('sequelize');

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

const llenar = async () => {
    // fs.readFile('./recipes.json', 'utf-8',(err, data) => {
    try {
        await sequelize.sync({force: false})
        const Recetas = JSON.parse(await fs.promises.readFile('./recipes.json', 'utf-8'));
        // await sequelize.Transaction(async (transaction) => {
        for (let receta of Recetas) {
                const nuevoAttachments = await Attachments.create({
                    mime: receta.mime,
                    url: foto(receta)
                })
                // await nuevoAttachments.save();

                const nuevoPost = await Posts.create({
                    title: receta.title,
                    body: rellenar_body(receta.ingredients, receta.steps),
                    attachmentId: nuevoAttachments.id
                });

                // const nuevoAttachments = await Attachments.create({
                //     mime: receta.mime,
                //     url: foto(receta)
                //   }, { transaction });

                // const nuevoPost = await Posts.create({
                //     title: receta.title,
                //     body: rellenar_body(receta.ingredients, receta.steps),
                //     attachmentId: nuevoAttachments.id
                //   }, { transaction });
                
                console.log(nuevoPost.attachmentId, nuevoAttachments.url)
                
                // await nuevoPost.save();
        }
    // });
    } catch (error) {
        console.log(`Upsi ha habido un error ${error}  `)
    }
    // })

}
llenar();
