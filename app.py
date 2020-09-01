from flask import Flask,render_template,request,redirect,url_for
import json,os
app = Flask(__name__)

with open("./Data/extractedData.json","r") as f:
    mydict=json.load(f)

results=[]        # final list that will contain names of requires files with keywords

def result_creation(mylist):
    numbr_of_words=len(mylist)

    if numbr_of_words==1:
        for file_name in mydict.keys():
            words_dict=mydict[file_name]
            if mylist[0] in words_dict.keys():
                    results.append(file_name)
           
          
    else:
        if(mylist[1]=="OR"):
             for file_name in mydict.keys():
                words_dict=mydict[file_name]
                if mylist[0] in words_dict.keys() or mylist[2] in words_dict.keys():
                    results.append(file_name)


        else:
                 for file_name in mydict.keys():
                    words_dict=mydict[file_name]
                    if mylist[0] in words_dict.keys() or mylist[2] in words_dict.keys():
                            results.append(file_name)
        


@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method =="POST":
        pattern=request.form["to_search"]
        mylist=pattern.split()

        results.clear()

        result_creation(mylist)

        return redirect("/searchresults")
    else:
        return render_template('home.html');

@app.route('/searchresults',methods=["POST","GET"])
def result():
    if request.method=="GET":
         return render_template("page2.html",file_names=results)
    else:
        pattern=request.form["to_search"]
        mylist=pattern.split()

        results.clear()

        result_creation(mylist)

        return redirect("/searchresults")
          


if __name__=="__main__":
    app.run(debug=True)