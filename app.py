from flask import Flask,render_template,request,redirect,url_for
import json,os
app = Flask(__name__)

with open("extractedData.json","r") as f:
    mydict=json.load(f)

results=[]

@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method =="POST":
        pattern=request.form["to_search"]
        #mylist=pattern.split()
        #while "OR" in mylist:
        #   mylist.remove("OR")
        #while "AND" in mylist:
        #   mylist.remove("AND")
        results.clear()
        for file_name in mydict.keys():
            words_dict=mydict[file_name]
            if pattern in words_dict.keys():
                results.append(file_name)
        print(results)

        return redirect("/searchresults")
    else:
        return render_template('home.html');

@app.route('/searchresults',methods=["POST","GET"])
def result():
    return render_template("page2.html",file_names=results,curr_path=os.getcwd())


if __name__=="__main__":
    app.run(debug=True)