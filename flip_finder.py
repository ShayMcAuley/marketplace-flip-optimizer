def get_search_keyword():
    while True:
        keyword = input("Enter a search keyword: ").strip()
        if keyword:
            return keyword
        else:
            print("Keyword cannot be empty. Please try again.")

def get_category_filter():
    while True:
        category = input("Enter category (or press Enter to skip): ").strip()
        # Allow empty (no filter), otherwise store value
        return category if category else None

def get_marketplace_filter():
    marketplaces = ["ebay", "facebook", "gumtree"]
    print("Available marketplaces:", ", ".join(marketplaces))
    while True:
        marketplace = input("Enter marketplace (or press Enter to skip): ").strip().lower()
        if not marketplace or marketplace in marketplaces:
            return marketplace if marketplace else None
        else:
            print("Invalid marketplace. Choose from:", ", ".join(marketplaces))

def get_price_range():
    while True:
        min_price = input("Enter minimum price (or press Enter to skip): ").strip()
        max_price = input("Enter maximum price (or press Enter to skip): ").strip()
        try:
            min_val = float(min_price) if min_price else None
            max_val = float(max_price) if max_price else None
            if (min_val is not None and min_val < 0) or (max_val is not None and max_val < 0):
                print("Prices must be non-negative.")
                continue
            if min_val is not None and max_val is not None and min_val > max_val:
                print("Minimum price cannot be greater than maximum price.")
                continue
            return min_val, max_val
        except ValueError:
            print("Invalid input. Please enter numeric values or leave blank.")

if __name__ == "__main__":
    print("=== Flip Finder Input Collection ===")
    keyword = get_search_keyword()
    category = get_category_filter()
    marketplace = get_marketplace_filter()
    price_min, price_max = get_price_range()

    print("\nCollected Search Parameters:")
    print(f"Keyword: {keyword}")
    print(f"Category: {category or 'Any'}")
    print(f"Marketplace: {marketplace or 'Any'}")
    print(f"Price Range: {price_min or 0} - {price_max or 'No Max'}")
