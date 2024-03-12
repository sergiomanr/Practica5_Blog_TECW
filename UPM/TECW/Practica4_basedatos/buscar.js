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
            console.log(`Id: ${post.id}, Title ${post.title}`)
            
        });
    } 
    else  {
        let arg_limp = args[2].replace('[','').replace(']','');
        try {
            
            let post =  await Posts.findByPk(Number(arg_limp));
            let attachment = await Attachments.findByPk(post.attachmentId);
            console.log(post.id);
            console.log(post.title);
            console.log(post.body);
            console.log(post.updatedAt,'\n');
            console.log(attachment.mime,'\n');
            try {
                console.log(attachment.url,'\n');
            } catch (error) {
                console.log('')
            }


        } catch (error) {
            console.log(`No existe el post ${arg_limp}`)
            process.exit(2)
        }
    }
}
buscar(args)