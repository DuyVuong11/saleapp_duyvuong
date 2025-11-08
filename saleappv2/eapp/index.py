from flask import render_template, request, redirect
from eapp import app, dao, login
from flask_login import login_user
from eapp.models import User, UserRole
import hashlib


@app.route('/')
def index():
    categories = dao.load_category()
    products = dao.load_product(
        cate_id=request.args.get('category_id'),
        kw=request.args.get('kw'),
        page=request.args.get('page')
    )
    return render_template("index.html", categories=categories, products=products)


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")


        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user=user)


    return redirect('/admin')


@login.user_loader
def load_user(user_id):
    return dao.load_user_by_id(user_id)


if __name__ == '__main__':
    from eapp import admin
    app.run(debug=True)
