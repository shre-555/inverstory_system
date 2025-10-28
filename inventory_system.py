"""
Inventory Management System
---------------------------
A simple inventory tracker that supports adding, removing, saving,
and loading stock data. Includes input validation, logging, and
security best practices.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable for storing inventory
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add a new item or increase its quantity.

    Args:
        item (str): Name of the item.
        qty (int): Quantity to add.
        logs (list, optional): Log entries list.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid input types for add_item: item=%s, qty=%s",
            item, qty
        )
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s of %s", qty, item)


def remove_item(item, qty):
    """
    Decrease the quantity of an item, removing it if depleted.

    Args:
        item (str): Name of the item to remove.
        qty (int): Quantity to remove.
    """
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid remove input types: item=%s, qty=%s",
            item, qty
        )
        return

    if item in stock_data:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed item '%s' from inventory.", item)
        else:
            logging.info("Decreased '%s' by %s units.", item, qty)
    else:
        logging.warning("Attempted to remove non-existent item '%s'.", item)


def get_qty(item):
    """
    Get the quantity of an item in stock.

    Args:
        item (str): Name of the item.

    Returns:
        int: Quantity of the item or 0 if not found.
    """
    if not isinstance(item, str):
        logging.warning("Invalid item type for get_qty: %s", type(item))
        return 0
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): Path to the inventory JSON file.

    Returns:
        dict: Loaded inventory data or empty dict on failure.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Inventory data loaded from %s", file)
            return data
    except FileNotFoundError:
        logging.warning("Inventory file not found: %s", file)
        return {}
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in %s", file)
        return {}
    except (OSError, ValueError) as error:
        logging.exception("Error loading file %s: %s", file, error)
        return {}


def save_data(file="inventory.json"):
    """
    Save current inventory data to a JSON file.

    Args:
        file (str): Path to save the inventory JSON file.
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
            logging.info("Inventory data saved to %s", file)
    except (OSError, TypeError, ValueError) as error:
        logging.exception("Error saving inventory data: %s", error)


def print_data():
    """
    Print the current inventory items and their quantities.
    """
    logging.info("Printing inventory data.")
    print("\n=== Inventory Report ===")
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def check_low_items(threshold=5):
    """
    Identify items with quantity below the given threshold.

    Args:
        threshold (int): Minimum acceptable stock level.

    Returns:
        list: Items with quantities below the threshold.
    """
    if not isinstance(threshold, (int, float)):
        logging.warning("Invalid threshold type: %s", type(threshold))
        return []
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        logging.info("Items below threshold: %s", low_items)
    return low_items


def main():
    """
    Main execution entry point for the inventory system.
    """
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("grape", 0)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    loaded_data = load_data()
    if loaded_data:
        global stock_data
        stock_data = loaded_data
    print_data()

    logging.info("Program executed successfully.")


if __name__ == "__main__":
    main()
