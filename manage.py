from flask.ext.script import Manager
from guild import build_app

app = build_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()