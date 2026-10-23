from config import PRODUCTS_FILE, TRANSACTIONS_FILE
from storage import read_data, write_data, get_next_id
from product_manager import list_products
from utils import (
    input_integer,
    input_non_empty,
    timestamp,
    money,
)


def record_stock_movement(movement_type):
    products = list_products()

    if not products:
        print("Add a product before recording stock movements.")
        return

    print(f"\n--- Record Stock {movement_type.title()} ---")

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"SKU: {product['sku']} | "
            f"Stock: {product['quantity']}"
        )

    product_id = input_integer("Enter product ID: ", minimum=1)

    product = next(
        (item for item in products if item["id"] == product_id),
        None,
    )

    if not product:
        print("Product not found.")
        return

    quantity = input_integer("Enter quantity: ", minimum=1)

    if movement_type == "sale" and quantity > product["quantity"]:
        print(
            "Sale rejected. Available stock is "
            f"{product['quantity']} units."
        )
        return

    note = input("Reference or note (optional): ").strip()

    if movement_type == "purchase":
        product["quantity"] += quantity
    else:
        product["quantity"] -= quantity

    product["updated_at"] = timestamp()

    transactions = read_data(TRANSACTIONS_FILE)

    transaction = {
        "id": get_next_id(transactions),
        "product_id": product["id"],
        "product_name": product["name"],
        "sku": product["sku"],
        "type": movement_type,
        "quantity": quantity,
        "unit_price": product["unit_price"],
        "total_value": round(quantity * product["unit_price"], 2),
        "note": note,
        "created_at": timestamp(),
    }

    # Persist the updated stock and its transaction history.
    write_data(PRODUCTS_FILE, products)

    try:
        transactions.append(transaction)
        write_data(TRANSACTIONS_FILE, transactions)
    except OSError:
        # Attempt to restore the previous quantity if the history write fails.
        if movement_type == "purchase":
            product["quantity"] -= quantity
        else:
            product["quantity"] += quantity

        product["updated_at"] = timestamp()
        write_data(PRODUCTS_FILE, products)
        raise

    print("\nStock movement recorded successfully.")
    print(f"Product     : {product['name']}")
    print(f"Movement    : {movement_type.title()}")
    print(f"Quantity    : {quantity}")
    print(f"Stock now   : {product['quantity']}")
    print(f"Unit value  : {money(product['unit_price'])}")
    print(f"Total value : {money(transaction['total_value'])}")

    if product["quantity"] <= product["min_stock"]:
        print("LOW STOCK ALERT: Reorder this product soon.")


def stock_purchase():
    record_stock_movement("purchase")


def stock_sale():
    record_stock_movement("sale")


def show_transactions():
    transactions = read_data(TRANSACTIONS_FILE)

    print("\n--- Stock Movement History ---")

    if not transactions:
        print("No stock movements recorded.")
        return

    for transaction in sorted(
        transactions,
        key=lambda item: item["id"],
    ):
        print("-" * 45)
        print(f"Transaction ID: {transaction['id']}")
        print(f"Product       : {transaction['product_name']}")
        print(f"SKU           : {transaction['sku']}")
        print(f"Type          : {transaction['type'].title()}")
        print(f"Quantity      : {transaction['quantity']}")
        print(f"Total value   : {money(transaction['total_value'])}")
        print(f"Note          : {transaction.get('note') or '-'}")
        print(f"Date          : {transaction['created_at']}")
