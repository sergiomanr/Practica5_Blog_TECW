const Sequelize = require('sequelize')

const sequelize = new Sequelize('blog', 'root', '', {
    dialect: 'sqlite',
    storage: './blog.sqlite',
    logging: false
  });


sequelize.sync({ force: true });

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


// (async () => {
//     try {
//       // Force dropping existing tables (if any)
//       await sequelize.sync({ force: true });
  
//       console.log('Database and tables dropped and recreated successfully.');
  
//       // Define the Posts and Attachments models
//       const Posts = sequelize.define('Posts', {
//         id: {
//           type: Sequelize.INTEGER,
//           primaryKey: true,
//           autoIncrement: true
//         },
//         createdAt: {
//           type: Sequelize.DATE
//         },
//         updatedAt: {
//           type: Sequelize.DATE
//         },
//         title: {
//           type: Sequelize.STRING,
//           allowNull: false
//         },
//         body: {
//           type: Sequelize.TEXT,
//           allowNull: false
//         },
//         attachmentId: {
//           type: Sequelize.INTEGER,
//           references: {
//             model: 'Attachments',
//             key: 'id'
//           }
//         }
//       }, {
//         tableName: 'Posts'
//       });
  
//       const Attachments = sequelize.define('Attachments', {
//         id: {
//           type: Sequelize.INTEGER,
//           primaryKey: true,
//           autoIncrement: true
//         },
//         createdAt: {
//           type: Sequelize.DATE
//         },
//         updatedAt: {
//           type: Sequelize.DATE
//         },
//         mime: {
//           type: Sequelize.STRING,
//           allowNull: true
//         },
//         url: {
//           type: Sequelize.STRING,
//           allowNull: true
//         }
//       }, {
//         tableName: 'Attachments'
//       });
  
//       // Define the one-to-one relationship with cascade delete onDelete
//       Posts.hasOne(Attachments, {
//         foreignKey: 'attachmentId',
//         onDelete: 'CASCADE' // Delete associated attachment on post deletion
//       });
  
//       console.log('Models and relationships defined successfully.');
//     } catch (error) {
//       console.error('Error dropping tables or defining models:', error);
//     }
//   })();


module.exports = {
    Posts,
    Attachments,
    sequelize, 
  };
