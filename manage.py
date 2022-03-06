# from app import create_app,db
from flask_script import Manager, Server
from app import create_app
from app.models import User, Pitch,Upvote,Downvote,Comment
from  flask_migrate import Migrate

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app)
manager.add_command('db')

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