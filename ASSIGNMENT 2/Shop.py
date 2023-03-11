class Shop:
    def __init__(self, name, description, categories, items, url):
        self.name = name
        self.description = description
        self.categories = categories
        self.items = items
        self.url = url
        self.shopping_cart = []

    def view_category(self, category):
        if category in self.categories:
            category_items = [item for item in self.items if item['category'] == category]
            if len(category_items) > 0:
                print(f"{category} items:")
                for item in category_items:
                    print(f"{item['name']} - {item['price']}")
            else:
                print(f"No items found in {category}")
        else:
            print(f"{category} is not a valid category")

    def search_items(self, keyword):
        search_results = [item for item in self.items if keyword in item['name']]
        if len(search_results) > 0:
            print(f"Search results for '{keyword}':")
            for item in search_results:
                print(f"{item['name']} - {item['price']}")
        else:
            print(f"No items found for '{keyword}'")

    def view_item(self, item_name):
        item = next((item for item in self.items if item['name'] == item_name), None)
        if item:
            print(f"{item['name']} - {item['description']} - {item['price']}")
        else:
            print(f"{item_name} not found")

    def view_shopping_cart(self):
        if len(self.shopping_cart) > 0:
            total = sum(item['price'] for item in self.shopping_cart)
            print("Shopping cart:")
            for item in self.shopping_cart:
                print(f"{item['name']} - {item['price']}")
            print(f"Total: {total}")
        else:
            print("Shopping cart is empty")
