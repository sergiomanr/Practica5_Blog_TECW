const { Posts, Attachments, sequelize } = require('./crear');
const args = process.argv;

async function buscar(args) {
    await sequelize.sync()
    if (args.length > 3) {
        process.exit(1);
    } else if (args.length == 2) {
        let posts = await Posts.findAll({
            attributes: ['id','title']
        });
        posts.forEach(post => {
            console.log(`Id: ${post.id}, Title: ${post.title}`)
            
        });
    } 
    else  {
        let arg_limp = args[2].replace('[','').replace(']','');
        try {
            
            let post =  await Posts.findByPk(Number(arg_limp));
            let attachment = await Attachments.findByPk(post.attachmentId);
            console.log('ID:',post.id);
            console.log('Title:',post.title);
            console.log('Cuerpo:',post.body);
            console.log('Fecha modificación:',post.updatedAt,'\n');
            console.log('Mime:',attachment.mime,'\n');
            if (attachment.url) {
                console.log('Url:',attachment.url,'\n');
            } else {
                console.log('')
            }


        } catch (error) {
            console.log(`No existe el post ${arg_limp}`)
            process.exit(2)
        }
    }
}
buscar(args)