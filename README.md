# Inventory Stock Alert System

A beginner-friendly Python console application for managing product inventory, tracking stock purchases and sales, and identifying products that need to be reordered.

## Features

- Add and search products
- Edit product details
- Maintain unique product SKUs
- Record stock purchases
- Record stock sales
- Prevent sales beyond available stock
- Set minimum stock alert levels
- Identify low-stock and out-of-stock products
- View stock movement history
- Calculate estimated inventory retail value
- Generate inventory and movement summaries
- Store records locally using JSON files

## Technologies Used

- Python
- JSON
- Python standard library

## Project Structure

```text
InventoryStockAlertSystem/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── product_manager.py
├── stock_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── products.json
    └── transactions.json
```

## Requirements

- Python 3.10 or newer recommended
- Visual Studio Code or another Python editor

No third-party packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/InventoryStockAlertSystem.git
```

Open the project folder in your terminal.

Run the application:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## How to Use

1. Select **Add Product** to register a product.
2. Enter its SKU, name, category, selling price, opening quantity, and minimum stock level.
3. Select **Record Stock Purchase** when new stock arrives.
4. Select **Record Stock Sale** when products are sold.
5. Open **Low Stock Report** to identify products that need replenishment.
6. Use **Inventory Summary** to view current stock statistics.
7. Open **Stock Movement History** to review recorded transactions.

## Example

Suppose a shop registers a keyboard with:

- SKU: KB101
- Selling price: ₹800
- Opening quantity: 20
- Minimum stock level: 5

After recording a sale of 16 keyboards:

- Available stock: 4
- Minimum stock level: 5
- Status: Low stock

The system displays a low-stock warning.

## Data Storage

The application stores data in:

- `data/products.json`
- `data/transactions.json`

The files are initialized automatically if they do not exist.

Back up the `data` folder regularly. Avoid editing the JSON files while the application is running.

## Testing Checklist

- Add a product with a unique SKU.
- Try adding another product with the same SKU.
- Edit the product details.
- Record a stock purchase and verify the quantity increases.
- Record a sale and verify the quantity decreases.
- Attempt to sell more units than are available.
- Set a minimum stock level and test the low-stock report.
- Check inventory value and movement summaries.
- Restart the program and verify that records persist.

## Limitations

This project is designed for learning and personal practice. It uses local JSON storage and is intended for a single user.

It does not include login authentication, barcode scanning, supplier management, automatic notifications, simultaneous-user support, or production-grade transaction handling.

The inventory value is an estimate based on each product's selling price, not its purchase cost or accounting valuation.

## Future Improvements

- Add a graphical interface using Tkinter.
- Add supplier management.
- Add purchase-cost tracking.
- Export inventory reports to CSV.
- Add barcode scanning.
- Add automatic email stock alerts.
- Use SQLite or MySQL for storage.
- Add user login and permissions.

## License

This project is intended for educational and personal use.
