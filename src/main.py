"""route main"""
from flask import Flask

app = Flask('__main__')

@app.route('/', methods=['GET'])
def index() -> str:
    return 'OK'

if __name__ == '__main__':
    app.run()    