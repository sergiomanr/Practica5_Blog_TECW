const { Posts, Attachments, sequelize } = require('./crear');



const args = process.argv;
// console.log(args[2][0])


async function buscar(args) {
    await sequelize.sync()
    if (args.length > 3) {
        process.exit(1);
    } else if (args.length == 2) {
        let posts = await Posts.findAll({
            attributes: ['id','title']
        })
        console.log(posts)
    } 
    else  {
        let arg_limp = args[2].replace('[','').replace(']','');
        try {
            
            let post =  await Posts.findByPk(Number(arg_limp));
            let attachment = await Attachments.findByPk(post.attachmentId);
            console.log(post.id);
            console.log(post.title);
            console.log(post.body);
            console.log(post.updatedAt);
            console.log(post.attachmentId);
            try {
                console.log(attachment.url);
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