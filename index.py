from flask  import Flask,request,jsonify
from libs.Connection import Connection 
app =Flask(__name__)

#--------------home
@app.route("/",methods=["GET"])
def index():
    return "algo"
#--------------home

#------------ list
@app.route("/people",methods=["GET"])
def list():
    con = Connection()
    result = con.query("select * from people p")
    print(result)
    json1 =[]    
    for x in result:
        print(x)
        json1.append({
            "name":x[1],
            "email":x[2]
        })
    # return "result"
    return jsonify(json1)
#------------ list


#------------ by name
@app.route("/busqueda/<name>", methods=["GET"])
def busqueda(name):
    con = Connection()
    result = con.query("select * from people p where p.name ='"+name+"'")
    print(result)
    json1 =[]    
    for x in result:
        print(x)
        json1.append({
            "name":x[1],
            "email":x[2]
        })
    # return "result"
    return jsonify(json1)
#------------ by name

if  __name__ == '__main__':
    app.run(port=8000)