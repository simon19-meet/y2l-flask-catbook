from flask import *
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_1(id):
    cat = get_cat_by_id(id)
    return render_template("cat.html",cat=cat.name)

@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        name=request.form['catname']
        create_cat(name)
        return render_template("response.html",n=name)

@app.route('/cat',methods=['GET','POST'])
def upvote(id):
    if request.method == 'POST':
        vote(id)
        return render_template("home.html")
    
    

if __name__ == '__main__':
   app.run(debug = True)
