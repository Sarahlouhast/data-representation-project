# Import necessary modules from Flask and ProductDAO class from DAO file
from flask import Flask, jsonify, request, abort, render_template
from ProductDAO import ProductDAO

# Create a Flask web application instance
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Create an instance of ProductDAO and use its methods as needed
product_dao = ProductDAO()

# Route: '/', returns a welcome message for the Product API page
@app.route('/')
def index():
   return  "Welcome to the Product API Page"

# Route: '/products' (HTTP GET method), retrieves and returns all products from the database in JSON format
@app.route('/products', methods=['GET'])
def get_all_products():
    products = product_dao.getAll()
    return jsonify(products)

# Route: '/products/<int:product_id>' (HTTP GET method), retrieves and returns a specific product based on its ID in json format
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = product_dao.findByID(product_id)
    # If the product with the specified ID is not found, return a 404 error
    if not product:
        abort(404)
    return jsonify(product)

# Route: '/products' (HTTP POST method), creates a new product based on the json data received in the request
@app.route('/products', methods=['POST'])
def create_product():
    # Check if the required fields are present in the json request data
    if not request.json or 'Product' not in request.json or 'Manufacturer' not in request.json or 'Model' not in request.json or 'Price' not in request.json:
        # If not present, return a 400 Bad Request error
        abort(400)
    # Extract product data from the json request data, note ID is omitted as this is auto incremented by mysql
    product_data = {
        'Product': request.json['Product'],
        'Manufacturer': request.json['Manufacturer'],
        'Model': request.json['Model'],
        'Price': request.json['Price']
    }
    # Call the create method of the instance to add the new product to the database
    new_product_id = product_dao.create(product_data)
    # Retrieve the created product from the database
    created_product = product_dao.findByID(new_product_id)
    # Return the created product in json format along with a 201 Created status code
    return jsonify(created_product), 201

# Route: '/products/<int:product_id>' (HTTP PUT method), updates an existing product based on the json data received in the request
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Retrieve the existing product by its ID
    product = product_dao.findByID(product_id)
    # If the product with the specified ID is not found, return a 404 error
    if not product:
        abort(404)
    # Update the product data if corresponding fields are present in the json request data
    if 'Product' in request.json:
        product['Product'] = request.json['Product']
    if 'Manufacturer' in request.json:
        product['Manufacturer'] = request.json['Manufacturer']
    if 'Model' in request.json:
        product['Model'] = request.json['Model']
    if 'Price' in request.json:
        product['Price'] = request.json['Price']
    # Call the update method of the instance to save the changes to the database
    product_dao.update(product)
    # Return the updated product in json format
    return jsonify(product)
    
# Route: '/products/<int:product_id>' (HTTP DELETE method), deletes an existing product based on its ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Retrieve the existing product by its ID
    product = product_dao.findByID(product_id)
    # If the product with the specified ID is not found, return a 404 error
    if not product:
        abort(404)
    # Call the delete method of the instance to remove the product from the database
    product_dao.delete(product_id)
    # Return a json response indicating that the deletion is completed
    return jsonify({'Deletion completed.': True})

# Block: Run the Flask application if this script is the main entry point
if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
