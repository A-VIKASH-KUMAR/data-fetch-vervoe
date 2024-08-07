from flask import Flask
from data_retrieval.data_fetch import data_fetch

# initialize flask app
app = Flask(__name__)
# register blueprint of data fetch endpoints
app.register_blueprint(data_fetch)


if __name__ == '__main__':
    app.run()