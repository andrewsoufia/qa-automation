# SPEC:
# - add(name, price, qty=1): qty must be 1 or more, otherwise ValueError.
#   Adding the same name again increases its qty.
# - remove(name): removes the item completely.
# - count(): total number of units (backpack x1 + light x2 = 3).
# - total(): sum of price * qty, rounded to 2 decimals.
# - apply_discount(percent): percent from 0 to 100 (both included), otherwise
#   ValueError. Returns the discounted total, rounded to 2 decimals.
# - save_receipt(path): writes "TOTAL: <total>" into the file at path.

class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, qty=1):
        if qty < 1:
            raise ValueError("qty must be 1 or more")
        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"price": price, "qty": qty}

    def remove(self, name):
        del self.items[name]

    def count(self):
        return sum(item["qty"] for item in self.items.values())

    def total(self):
        return round(sum(i["price"] * i["qty"] for i in self.items.values()), 2)

    def apply_discount(self, percent):
        if not 0 < percent <= 100:
            raise ValueError("percent must be 0 to 100")
        return round(self.total() * (1 - percent / 100), 2)

    def save_receipt(self, path):
        with open(path, "w") as f:
            f.write(f"TOTAL: {self.total()}")