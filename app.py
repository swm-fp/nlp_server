#===========================
# flask REST API code
#===========================
from flask import Flask
from flask import request
from flask import json
from utils import *

app = Flask(__name__)
app.config.from_object(__name__)

id = {"hello":"world"}

@app.route('/info/',methods=['POST'])
def get():
    if request.method == 'POST':
        data = request.get_json()
        # title, url, highlight, memo, other tags
        keywordlist = get_keywordlist(data["title"], data["url"], data["highlight"], data["memo"], data["other_tags"])
        return json.dumps(id)
    return "fail"

if __name__=='__main__':
	print('connection succeeded')
	app.run(host='127.0.0.1',port=5002,debug=True)
