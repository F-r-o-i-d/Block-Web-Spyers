from flask import Flask
import requests
import AdBlock
app = Flask(__name__)

@app.route('/url=<path:path>')
def hello_world(path):
    path = path.replace('url=','')
    path = requests.get(path).text

    return AdBlock.Formater(path)

if __name__ == '__main__':
   app.run(debug=True)
