from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.BaseModel import db

app = create_app('dev_config')
db.init_app(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()

