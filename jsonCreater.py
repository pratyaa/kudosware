import os
import re
import json
from nltk.corpus import stopwords


mappedData = dict()
stop_words = set(stopwords.words('english'))

for file_name in os.listdir(os.getcwd()):
    
    if not file_name.endswith(".txt"):
        continue

    key = file_name[:len(file_name)-4]+".pdf"
    val = dict()
    print(key)

    with open(os.path.join(os.getcwd(), file_name), encoding="utf-8") as fp:
        ln = fp.readline()
        while ln != "":
            ls = list(ln.split())
            ln = fp.readline()
            for word in ls:
                s = word[:]

                if not (s.isalpha()):
                    if s[1:].isalpha():
                        s = s[1:]
                    elif s[:len(s)-1].isalpha():
                        s = s[:len(s)-1]
                    else:
                        continue
                re.sub(r'\W+', '', s)

                s = s.lower()

                if s in stop_words:
                    continue
                
                if s not in val.keys():
                    val[s] = 0
                val[s] += 1
    mappedData[key] = val
    
with open('extractedData.json', 'w') as jfp:
    json.dump(mappedData, jfp)