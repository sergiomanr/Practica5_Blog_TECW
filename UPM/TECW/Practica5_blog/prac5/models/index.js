const Sequelize = require('sequelize')
const url = process.env.DATABASE_URL ||
"sqlite:blog.sqlite";
const sequelize = new Sequelize(url);
const Posts = require('./post')(sequelize);
const Attachments = require('./attachments')(sequelize);
module.exports = sequelize;

Posts.hasOne(Attachments, {
    foreignKey: 'attachmentId',
    onDelete: 'CASCADE',
    onUpdate: 'CASCADE'
})
Attachments.belongsTo(Posts)

