from config import PRODUCTS_FILE
from storage import read_data, write_data, get_next_id
from utils import (
    input_non_empty,
    input_integer,
    input_money,
    money,
    timestamp,
)


def list_products():
    return read_data(PRODUCTS_FILE)


def find_product(product_id):
    for product in list_products():
        if product["id"] == product_id:
            return product

    return None


def find_product_by_sku(sku):
    for product in list_products():
        if product["sku"].lower() == sku.lower():
            return product

    return None


def add_product():
    products = list_products()

    print("\n--- Add Product ---")

    sku = input_non_empty("Product SKU/code: ").upper()

    if find_product_by_sku(sku):
        print("This SKU already exists.")
        return

    name = input_non_empty("Product name: ")
    category = input_non_empty("Category: ")
    unit_price = input_money("Selling price per unit: ")
    quantity = input_integer("Opening stock quantity: ")
    min_stock = input_integer("Minimum stock alert level: ")

    product = {
        "id": get_next_id(products),
        "sku": sku,
        "name": name,
        "category": category,
        "unit_price": unit_price,
        "quantity": quantity,
        "min_stock": min_stock,
        "created_at": timestamp(),
        "updated_at": timestamp(),
    }

    products.append(product)
    write_data(PRODUCTS_FILE, products)

    print(f"\nProduct added successfully. ID: {product['id']}")

    if quantity <= min_stock:
        print("Warning: This product is at or below its minimum stock level.")


def display_product(product):
    print("-" * 48)
    print(f"Product ID : {product['id']}")
    print(f"SKU        : {product['sku']}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Unit price : {money(product['unit_price'])}")
    print(f"In stock   : {product['quantity']}")
    print(f"Minimum    : {product['min_stock']}")
    print(
        "Stock value: "
        f"{money(product['quantity'] * product['unit_price'])}"
    )

    if product["quantity"] <= product["min_stock"]:
        print("Alert      : LOW STOCK")


def show_products():
    products = list_products()

    print("\n--- Product Inventory ---")

    if not products:
        print("No products registered.")
        return

    for product in sorted(products, key=lambda item: item["id"]):
        display_product(product)


def search_product():
    query = input_non_empty(
        "Enter product name, SKU, category, or ID: "
    ).lower()

    matches = []

    for product in list_products():
        if (
            query in product["name"].lower()
            or query in product["sku"].lower()
            or query in product["category"].lower()
            or query == str(product["id"])
        ):
            matches.append(product)

    if not matches:
        print("No matching products found.")
        return

    for product in matches:
        display_product(product)


def edit_product():
    products = list_products()

    print("\n--- Edit Product Details ---")
    product_id = input_integer("Enter product ID: ", minimum=1)

    product = next(
        (item for item in products if item["id"] == product_id),
        None,
    )

    if not product:
        print("Product not found.")
        return

    print("Press Enter to keep the current value.")

    new_name = input(f"Name [{product['name']}]: ").strip()
    new_category = input(
        f"Category [{product['category']}]: "
    ).strip()
    new_sku = input(f"SKU [{product['sku']}]: ").strip().upper()

    if new_sku:
        duplicate = next(
            (
                item for item in products
                if item["id"] != product_id
                and item["sku"].lower() == new_sku.lower()
            ),
            None,
        )

        if duplicate:
            print("Another product already uses this SKU.")
            return

    new_price_text = input(
        f"Selling price [{product['unit_price']}]: "
    ).strip()

    if new_price_text:
        try:
            new_price = float(new_price_text)

            if not (0 < new_price < float("inf")):
                print("Enter a valid positive price.")
                return

            from decimal import Decimal, ROUND_HALF_UP

            new_price = float(
                Decimal(str(new_price)).quantize(
                    Decimal("0.01"),
                    rounding=ROUND_HALF_UP,
                )
            )

            if new_price <= 0:
                print("Selling price must be greater than zero.")
                return

            product["unit_price"] = new_price

        except (ValueError, ArithmeticError):
            print("Invalid selling price.")
            return

    if new_name:
        product["name"] = new_name

    if new_category:
        product["category"] = new_category

    if new_sku:
        product["sku"] = new_sku

    product["updated_at"] = timestamp()

    write_data(PRODUCTS_FILE, products)
    print("Product details updated successfully.")
