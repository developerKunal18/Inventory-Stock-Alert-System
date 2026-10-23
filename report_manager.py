from config import PRODUCTS_FILE, TRANSACTIONS_FILE
from storage import read_data
from utils import money


def low_stock_report():
    products = read_data(PRODUCTS_FILE)

    low_stock = [
        product for product in products
        if product["quantity"] <= product["min_stock"]
    ]

    print("\n--- Low Stock Report ---")

    if not low_stock:
        print("All products are above their minimum stock levels.")
        return

    for product in low_stock:
        shortage = max(0, product["min_stock"] - product["quantity"])

        print("-" * 40)
        print(f"Product  : {product['name']}")
        print(f"SKU      : {product['sku']}")
        print(f"Available: {product['quantity']}")
        print(f"Minimum  : {product['min_stock']}")
        print(f"Below minimum by: {shortage} units")

        if product["quantity"] == 0:
            print("Status   : OUT OF STOCK")
        else:
            print("Status   : LOW STOCK")


def inventory_report():
    products = read_data(PRODUCTS_FILE)

    print("\n--- Inventory Summary ---")

    if not products:
        print("No products registered.")
        return

    total_products = len(products)
    total_units = sum(product["quantity"] for product in products)
    low_stock_count = sum(
        1 for product in products
        if product["quantity"] <= product["min_stock"]
    )
    out_of_stock_count = sum(
        1 for product in products
        if product["quantity"] == 0
    )
    estimated_value = sum(
        product["quantity"] * product["unit_price"]
        for product in products
    )

    print(f"Unique products       : {total_products}")
    print(f"Total units in stock  : {total_units}")
    print(f"Low-stock products    : {low_stock_count}")
    print(f"Out-of-stock products : {out_of_stock_count}")
    print(f"Estimated stock value : {money(estimated_value)}")

    print("\nStock by category:")

    category_totals = {}

    for product in products:
        category = product["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + product["quantity"]
        )

    for category, quantity in sorted(category_totals.items()):
        print(f"{category}: {quantity} unit(s)")


def movement_report():
    transactions = read_data(TRANSACTIONS_FILE)

    purchases = [
        transaction for transaction in transactions
        if transaction["type"] == "purchase"
    ]
    sales = [
        transaction for transaction in transactions
        if transaction["type"] == "sale"
    ]

    purchase_units = sum(item["quantity"] for item in purchases)
    sale_units = sum(item["quantity"] for item in sales)

    purchase_value = sum(item["total_value"] for item in purchases)
    sale_value = sum(item["total_value"] for item in sales)

    print("\n--- Stock Movement Summary ---")
    print(f"Purchase transactions : {len(purchases)}")
    print(f"Units purchased       : {purchase_units}")
    print(f"Purchase value        : {money(purchase_value)}")
    print(f"Sale transactions     : {len(sales)}")
    print(f"Units sold            : {sale_units}")
    print(f"Sale value            : {money(sale_value)}")

    print(
        "\nNote: Values use the product's current selling price "
        "recorded at the time of each transaction."
    )
