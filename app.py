
#===========================
# flask REST API code
#===========================
from flask import Flask
from flask import request
from flask import json
from flask import Response
import operator, re
from konlpy.tag import Kkma
from textblob import TextBlob

app = Flask(__name__)
app.config.from_object(__name__)

id = {"hello":"world"}

def keyword_extractor(title, highlight):
    konl = Kkma()
    eng_title = TextBlob(re.sub("[^A-Za-z]", ",", title.strip())).noun_phrases
    eng_highlight = TextBlob(re.sub("[^A-Za-z]", " ", highlight.strip())).noun_phrases
    title_nouns = konl.nouns(title)
    highlight_nouns = konl.nouns(highlight)

    #line = re.sub("[^A-Za-z]", "", title.strip())

    keyword_list = {i: 2 for i in title_nouns}
    for i in highlight_nouns:
        try:
            keyword_list[i] +=1
        except:
            keyword_list[i] = 1

    for i in eng_title:
        keyword_list[i] = 2

    for i in eng_highlight:
        try:
            keyword_list[i] +=1
        except:
            keyword_list[i] = 1

    keyword_list = sorted(keyword_list.items(), key=operator.itemgetter(1), reverse=True)[:10]
    '''
    keywords={}
    for i, k in enumerate(keyword_list):
        keywords[str("k"+str(i))] = k[0]
    '''
    return keyword_list

@app.route('/info/',methods=['POST', 'GET'])
def get():
    if request.method == 'POST':
        req = request.get_json()
        data = req[data]
        '''
        arrayList = 
        {
            title : ""
            url : ""
            memo : ["", "", ...]
            highlight : ["", "", ...]
        }
        '''
        result = {}
        result["keywords"] = keyword_extractor(data["title"], "")
        result["data"] = data
        
        res = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    if request.method == 'GET':
        return json.dumps(id)
    return "fail"

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5002,debug=True)
    #keyword_extractor("생성적 적대 신경망(GANs)에 대한 초보자용 가이드 (GANs)", "GANs을 이해하려면 생성(generative) 알고리즘이 작동하는 방식을 알아야 한다.")

