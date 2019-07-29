import os
import psycopg2

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://swowgedxgmeugi:0d1eda082de1fae25d151bcf290377d6c919c1b39f65f14a96f0982a194a0db3@ec2-174-129-41-127.compute-1.amazonaws.com:5432/d5t458ucvgs05j'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
db = SQLAlchemy(app)

class Data_Base(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	info = db.Column('data', db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page_2')
def page_2():
	return render_template("random_page_2.html")

@app.route('/view_database')
def view_db():
	record = Data_Base.query.filter_by(info='Hello World!').first()
	data = record.data
	return render_template('view_database.html', data=data) # this works!

	# record = Data_Base.query.all()
	# record = record.query(id, info)
	# data = record.get.all()
	# return render_template('view_database.html', data=data)

	# record = Data_Base.query.all()
	# data = record
	# return render_template('view_database.html', data=data)






if __name__ == '__main__': app.run(debug=True)