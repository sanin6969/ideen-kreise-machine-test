import csv

def read_csv(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            products = []
            
            for row in reader:
                try:
                    product_id = row['product_id']
                    name = row['name']
                    price = float(row['price'])  
                    products.append({'product_id': product_id, 'name': name, 'price': price})
                except (ValueError, KeyError):
                    print(f"Skipping malformed row: {row}")

            return products
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def find_top_expensive_products(products, top_n=3):
    return sorted(products, key=lambda x: x['price'], reverse=True)[:top_n]

if __name__ == "__main__":
    filename = "products.csv"  
    products = read_csv(filename)

    if products:
        top_products = find_top_expensive_products(products)
        print("\nTop 3 Most Expensive Products:")
        for product in top_products:
            print(f"{product['name']} (ID: {product['product_id']}) - ${product['price']:.2f}")
    else:
        print("No valid product data found.")
