from flask import *
from flask import render_template
from database import *
from models import *

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>',methods=['GET','POST'])
def cat_1(id):
    cat = get_cat_by_id(id)
    vote(id)
    return render_template("cat.html",cat=cat.name,v=cat.votes)




@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        name=request.form['catname']
        create_cat(name)
        return render_template("response.html",n=name)



    
    

if __name__ == '__main__':
   app.run(debug = True)
