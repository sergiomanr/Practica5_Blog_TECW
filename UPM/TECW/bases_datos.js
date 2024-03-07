let Sequelize = require('sequelize')

const connetion = new Sequelize('demo','idm','contraseña',
{
    host:  'localhost',
    dialect: 'mysql',
    port: 3306,
    logging: false
})

async function conectarse(){
    await connetion.authenticate()
    console.log('Connection succesfull')
    const artista = Sequelize('Artista', {
    
            id: {
                primaryKey: true,
                unique: true,
                autoincrement: true,
                type: Sequelize.INTEGER
            },
            nombre: {
                type: Sequelize.STRING,
                allowNull: false
            },
            nacionalidad: {
                type: Sequelize.STRING,
                allowNull: false    
            },
        },
        {
            tableName: 'Artista',
            timestamps: false
        }

    )
}