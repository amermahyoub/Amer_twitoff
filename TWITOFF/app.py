from decouple import config
from flask import Flask
from .models import DB, User

#now we make a app factory

def create_app():
    app = Flask(__name__)

    #add our config
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #now have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_tempelate('base.html', title='Home', users=users)
    return app
