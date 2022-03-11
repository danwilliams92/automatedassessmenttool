from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c9ddf3c61037ad426abd6262587fd8757ba49e6f01772beb'

from mainApp import routes