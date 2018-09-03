from flask import Flask, render_template, Blueprint, request, flash
from model import *

index = Blueprint('index',__name__)


@index.route('/home')
def home():
	datas = Student.query.all()
	return render_template('./admin/starter.html',datas=datas)

@index.route('/create')
def create():
	db.create_all()
	return("done")
@index.route('/delete')
def delete():
	db.drop_all()
	return("deleted")