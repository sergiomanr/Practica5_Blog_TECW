const Sequelize = require('sequelize')

const sequelize = new Sequelize('blog', 'root', '', {
    dialect: 'sqlite',
    storage: './blog.sqlite',
    logging: false
  });


sequelize.sync();

const Posts = sequelize.define('Posts',{
    id : {
        primaryKey: true,
        autoIncrement: true,
        type: Sequelize.INTEGER
    },
    createdAt: {
        type: Sequelize.DATE
    },
    updatedAt: {
        type: Sequelize.DATE
    },
    title: {
        type: Sequelize.STRING,
        allowNull: false
    },
    body: {
        type: Sequelize.TEXT,
        allowNull: false
    },
    attachmentId: {
        type: Sequelize.INTEGER,
    }   
    },{
    tableName: 'Posts'        
    }
)

const Attachments = sequelize.define('Attachments',{
    id : {
        primaryKey: true,
        autoIncrement: true,
        type: Sequelize.INTEGER
    },
    createdAt: {
        type: Sequelize.DATE
    },
    updatedAt: {
        type: Sequelize.DATE
    },
    mime: {
        type: Sequelize.STRING,
        allowNull: true
    },
    url: {
        type: Sequelize.STRING,
        allowNull: true
    }
    },
    {
        tableName: 'Attachments'
    }
)

Posts.hasOne(Attachments, {
    foreignKey: 'attachmentId',
    onDelete: 'CASCADE',
    onUpdate: 'CASCADE'
})
Attachments.belongsTo(Posts)

module.exports = {
    Posts,
    Attachments,
    sequelize, 
  };