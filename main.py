from lib.db import create_db
from app.app import app
from app.index import index



if __name__ == '__main__':
    create_db()
    app.run(debug=True)