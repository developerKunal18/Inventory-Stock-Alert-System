from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

PRODUCTS_FILE = DATA_DIR / "products.json"
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"

CURRENCY = "₹"
