from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from unicodedata import category

from eapp.models import Category,Product
from eapp import app, db

admin = Admin(app=app, name='eSaleApp')

class ProductView(ModelView):
    page_size = 5
    can_export = True
    column_list = ['id','name','price','category_id']





admin.add_view(ModelView(Category,db.session))
admin.add_view(ProductView(Product,db.session))


