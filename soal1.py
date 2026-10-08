import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_products():
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()

        data = response.json()
        print("GET Response :")
        print(data[:2])
    except requests.exceptions.RequestException as e:
        print("ERROR :", e)

def get_product(product_id):
    try:
        response = requests.get(f"{BASE_URL}/{product_id}", timeout=5)
        response.raise_for_status()

        print("GET Detail :")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("ERROR :", e)

def add_product():
    product = {
        "nama" : "Laptop",
        "harga" : 10000000,
        "stok" : 5
    },
    {
        "nama" : "Mouse",
        "harga" : 100000,
        "stok" : 10
    }

    try :
        response = requests.post(
            BASE_URL, json=product, timeout=5
        )
        response.raise_for_status()
        
        print("POST Response :")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("ERROR :", e)

def update_product(product_id):
    product = {
            "nama" : "Laptop",
            "harga" : 20000000,
            "stok" : 10
    }
    try:
        response = requests.put(f"{BASE_URL}/{product_id}", timeout=5)
        response.raise_for_status()
                 
        print("PUT Response :")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("ERROR :", e)

def delete_product(product_id):
    try:
        response = requests.delete(f"{BASE_URL}/{product_id}", timeout=5)
        response.raise_for_status()
                 
        print("Delete Response :")
        print("produk berhasil dihapus")
    except requests.exceptions.RequestException as e:
        print("ERROR :", e)

get_products()
get_product(1)
add_product()
update_product(1)
delete_product(2)