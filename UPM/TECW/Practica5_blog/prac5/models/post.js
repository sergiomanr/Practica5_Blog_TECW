// const {sequelize } = require('./index');

// const Posts = sequelize.define('Posts',{
//     id : {
//         primaryKey: true,
//         autoIncrement: true,
//         type: Sequelize.INTEGER
//     },
//     createdAt: {
//         type: Sequelize.DATE
//     },
//     updatedAt: {
//         type: Sequelize.DATE
//     },
//     title: {
//         type: Sequelize.STRING,
//         allowNull: false
//     },
//     body: {
//         type: Sequelize.TEXT,
//         allowNull: false
//     },
//     attachmentId: {
//         type: Sequelize.INTEGER,
//     }   
//     },{
//     tableName: 'Posts'        
//     }
// )

// module.exports = {
//     Posts
// }

const {Model, Sequelize} = require('sequelize');
// Definition of the Quiz model:
module.exports = (sequelize) => {
 class Posts extends Model {
 }
    Posts.init({
    id: {
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
    }, {
        sequelize
    }
 );
 return Posts;
};