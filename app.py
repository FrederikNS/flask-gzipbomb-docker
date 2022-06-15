from flask import Flask
from flask_gzipbomb import GzipBombResponse

app = Flask(__name__)

@app.route('/')
def bomb():
    return GzipBombResponse(size='10G')

if __name__ == "__main__":
    app.run()
