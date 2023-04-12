
from flask import Flask 
app = Flask(__name__)
from flask import url_for

from flask import request
@app.route('/return/text')
def text():
    return 'Oops', 404
if __name__ == "__main__":
    app()
                        
