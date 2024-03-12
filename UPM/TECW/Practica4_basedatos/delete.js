const { Posts, Attachments, sequelize } = require('./crear');

const args = process.argv;

async function borrar(args) {
    await sequelize.sync();
    if (args.length > 3) {
        process.exit(1);
    } else {
        let arg_limp = args[2].replace('[','').replace(']','');
        let posts = await Posts.findByPk(arg_limp);
        if (posts) {
            await posts.destroy();
            console.log('Se ha borrado correctamente el post con id: %d',arg_limp)
        } else if (!posts) {
            console.log('No existe el post %d',arg_limp);
            process.exit(2);
        }
    }
};

borrar(args);