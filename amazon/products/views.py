from flask import Blueprint

blueprint = Blueprint('products', __name__)

@blueprint.route('/', methods=['GET'])
def products():
    return 'products'