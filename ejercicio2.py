import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]})
available_products = _PRODUCT_DF[_PRODUCT_DF['quantity'] > 0]

def is_product_available(product_name, quantity):
    global available_products
    while True:
        product_name_lower = product_name.lower()  # convert names to lowercase
        product_index = available_products[available_products['product_name'].str.lower() == product_name_lower].index
        if len(product_index) == 0:
            print("El producto no está en el inventario o no tiene cantidad disponible.")
            print("Lista de productos disponibles:")
            print(available_products[['product_name', 'quantity']])
            choice = input("¿Desea elegir otro producto o cancelar? (s/n/c): ")
            if choice.lower() == 's':
                product_name = input("Ingrese el nombre del producto: ")
                quantity = int(input("Ingrese la cantidad deseada: "))
            elif choice.lower() == 'c':
                return False
        else:
            available_quantity = available_products.loc[product_index[0], 'quantity']
            if available_quantity >= quantity:
                return True
            else:
                print("La cantidad solicitada no está disponible.")
                print("Lista de productos disponibles:")
                print(available_products[['product_name', 'quantity']])
                choice = input("¿Desea elegir otra cantidad o cancelar? (s/n/c): ")
                if choice.lower() == 's':
                    quantity = int(input("Ingrese la cantidad deseada: "))
                elif choice.lower() == 'c':
                    return False

print (available_products)
product_name = input("Ingrese el nombre del producto: ")
quantity = int(input("Ingrese la cantidad deseada: "))
print(is_product_available(product_name, quantity))