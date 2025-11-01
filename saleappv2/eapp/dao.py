
from eapp.models import Category, Product


def load_category():
    return Category.query.all()

def load_product(cate_id=None, kw=None, page=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query=query.filter(Product.id.__eq__(cate_id))

    return query.all()