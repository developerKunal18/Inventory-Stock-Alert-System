from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from config import CURRENCY


def money(amount):
    value = Decimal(str(amount)).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )
    return f"{CURRENCY}{value:,.2f}"


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def input_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt).strip())

            if value < minimum:
                print(f"Enter a whole number of at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Enter a valid whole number.")


def input_money(prompt, allow_zero=False):
    while True:
        try:
            value = Decimal(input(prompt).strip())

            if not value.is_finite():
                print("Enter a valid finite amount.")
                continue

            if value < 0 or (value == 0 and not allow_zero):
                print("Enter an amount greater than zero.")
                continue

            return float(
                value.quantize(
                    Decimal("0.01"),
                    rounding=ROUND_HALF_UP,
                )
            )

        except (InvalidOperation, ValueError):
            print("Enter a valid amount, such as 125 or 125.50.")


def timestamp():
    return datetime.now().isoformat(timespec="seconds")


def pause():
    input("\nPress Enter to continue...")
