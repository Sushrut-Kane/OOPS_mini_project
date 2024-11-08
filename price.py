# from inventory import items
def calculate_total_price(items, selected_quantities):
    order_summary = {item: qty for item, qty in selected_quantities.items() if qty > 0}
    total_price = 0
    detailed_summary = []

    for item, qty in order_summary.items():
        item_price = items[item]["price"]
        item_total = item_price * qty
        total_price += item_total
        detailed_summary.append((item, qty, item_price, item_total))

    return total_price, detailed_summary