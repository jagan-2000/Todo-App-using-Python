from flask import Flask, render_template,url_for,request,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import random

app=Flask(__name__)



todos = [
   {
        'id' :1,
        'name' : 'Write SQL',
        'checked': False,
   },
   {
        'id' : 2,
        'name' : 'Write Python',
        'checked': False,
   },
    
]
@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def Home():
    now = datetime.now()
    strftime = now.strftime("%A")
    str_now = now.strftime("%d-%B-%Y")
    if (request.method=="POST"):
          todo_name = request.form["todo_name"]
          cur_id = random.randint(1,1000)
          todos.append({
               'id': cur_id,
               'name': todo_name,
               'checked': False
          })
    return render_template("index.html", items=todos,str_now=str_now,strftime=strftime)

@app.route("/checked/<int:todo_id>", methods=['POST'])
def checked_todo(todo_id):
     for todo in todos:
          if todo ['id'] == todo_id:
               todo['checked'] = not todo['checked']
               break
     return redirect(url_for('Home'))

@app.route("/delete/<int:todo_id>", methods=['POST'])
def delete_todo(todo_id):
     global todos
     for todo in todos:
          if todo['id']== todo_id:
               todos.remove(todo)
     return redirect(url_for('Home'))

@app.route("/done/<int:todo_id>", methods=['POST'])
def done_todo(todo_id):
     if request.form.get('done'):
          return render_template(url_for('Home'),done=True)
     else:
          return redirect(url_for('Home'))


@app.route("/test")
def test():
     if (request.method=="POST"):
          todo_name = request.form["todo_name"]
          cur_id = random.randint(1,1000)
          todos.append({
               'id': cur_id,
               'name': todo_name,
               'checked': False
          })
     return render_template("base.html")

@app.route("/")
def time():
    now = datetime.now()
    str_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("time.html", str_now=str_now)


if __name__ =="__main__":
    app.run(debug=True)