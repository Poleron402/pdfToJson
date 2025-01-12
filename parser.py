import pdfplumber
import re
import json

def test_to_json(pdf_path):
    pdf_text = []
    questions = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text = text.replace('\u25aa', '-')
                lines = text.split('\n')
                for i in lines:
                    pdf_text.append(i)
    i = 0
    while i < len(pdf_text):
        obj = {}
        if re.search(r'^(\d+)\.', pdf_text[i]):
            obj['question'] = pdf_text[i]
            i+=1
            obj['answers'] = []
            while pdf_text[i].startswith('- '):
                obj['answers'].append(pdf_text[i].replace('- ', ''))
                i+=1
            questions.append(obj)
        else:
            i+=1
    return questions
print(test_to_json('C:\\coding\\scripts\\100q.pdf')) # replace with where your pdf is stored
where_to_store = 'C:\\coding\\civics\\src\\questions.json' # replace with where you want the json to be stored/used
with open(where_to_store, 'w') as js:
    json.dump(test_to_json('C:\\coding\\scripts\\100q.pdf'), js)
