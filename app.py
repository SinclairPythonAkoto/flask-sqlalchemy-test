from flask import Flask, render_template, url_for
from flask sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://swowgedxgmeugi:0d1eda082de1fae25d151bcf290377d6c919c1b39f65f14a96f0982a194a0db3@ec2-174-129-41-127.compute-1.amazonaws.com:5432/d5t458ucvgs05j'
db = SQLAlchemy(app)

class Data_Base(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_database')
def view_db():
	data = Data_Base.query.all()
	return render_template('view_database.html', data=data)





if __name__ == '__main__': app.run(debug=True)