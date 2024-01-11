 # Import the ProductDAO class from DAO module
from ProductDAO import ProductDAO 

def test_product_dao():
    # Create an instance of ProductDAO
    product_dao = ProductDAO()

    # Test create method
    new_product_id = product_dao.create({
        'Product': 'TestProduct',
        'Manufacturer': 'TestManufacturer',
        'Model': 'TestModel',
        'Price': 999
    })
    print(f'New Product ID: {new_product_id}')

    # Test getAll method
    all_products = product_dao.getAll()
    print('All Products:')
    print(all_products)

    # Test findByID method
    product_by_id = product_dao.findByID(new_product_id)
    print(f'Product by ID {new_product_id}:')
    print(product_by_id)

    # Test update method
    product_dao.update({
        'ID': new_product_id,
        'Product': 'UpdatedProduct',
        'Manufacturer': 'UpdatedManufacturer',
        'Model': 'UpdatedModel',
        'Price': 888
    })
    updated_product = product_dao.findByID(new_product_id)
    print('Updated Product:')
    print(updated_product)

    # Test delete method
    product_dao.delete(new_product_id)
    print(f'Product with ID {new_product_id} deleted.')

if __name__ == "__main__":
    test_product_dao()
