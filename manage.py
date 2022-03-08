# from app import create_app,db
from flask_script import Manager, Server
from app import create_app,db
from app.models import User, Pitch,Upvote,Downvote,Comment
from  flask_migrate import Migrate,MigrateCommand


app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)


manager.add_command('db',MigrateCommand)
manager.add_command('run',Server(use_debugger=True))

@manager.command
def test():
    """This function will run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
     return dict(app = app,db = db,User=User,Pitch=Pitch,Upvote=Upvote,Downvote=Downvote,Comment=Comment)
    
if __name__ == '__main__':
    manager.run()