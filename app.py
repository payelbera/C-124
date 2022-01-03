from flask import Flask, jsonify,request
app=Flask(__name__)
""" @app.route("/")
def hello_world():
    return "hello world" """


tasks=[
    {
        "id":1, "title":"buy groceries", "description":"milk,cheese,fruits","done":"False"
    },
     {
        "id":2, "title":"learn python", "description":"complete all the projects","done":"False"
    },
]
@app.route("/getdata")
def gettask():
    return jsonify({
        "data":tasks
    })

@app.route("/adddata", methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

        task={
            "id":tasks[-1]["id"]+1,
            "title":request.json["title"],
            "description":request.json.get("description",""),
            "done":False

        }
        tasks.append(task)
        return jsonify({
            "status":"success",
            "message":"task added successfully"
        })
if(__name__=="__main__"):
    app.run(debug=True)
