from storage import initialize_storage

from product_manager import (
    add_product,
    show_products,
    search_product,
    edit_product,
)

from stock_manager import (
    stock_purchase,
    stock_sale,
    show_transactions,
)

from report_manager import (
    low_stock_report,
    inventory_report,
    movement_report,
)

from utils import pause


def display_menu():
    print("\n" + "=" * 48)
    print("       INVENTORY STOCK ALERT SYSTEM")
    print("=" * 48)
    print("1.  Add Product")
    print("2.  View All Products")
    print("3.  Search Product")
    print("4.  Edit Product Details")
    print("5.  Record Stock Purchase")
    print("6.  Record Stock Sale")
    print("7.  View Stock Movement History")
    print("8.  Low Stock Report")
    print("9.  Inventory Summary")
    print("10. Stock Movement Summary")
    print("0.  Exit")
    print("=" * 48)


def main():
    initialize_storage()

    actions = {
        "1": add_product,
        "2": show_products,
        "3": search_product,
        "4": edit_product,
        "5": stock_purchase,
        "6": stock_sale,
        "7": show_transactions,
        "8": low_stock_report,
        "9": inventory_report,
        "10": movement_report,
    }

    print("Welcome to the Inventory Stock Alert System!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using the Inventory Stock Alert System.")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice. Please select a valid menu option.")
            pause()
            continue

        try:
            action()
        except (ValueError, OSError, KeyError) as error:
            print(f"\nUnable to complete the operation: {error}")
            print("Check the data files and try again.")

        pause()


if __name__ == "__main__":
    main()
