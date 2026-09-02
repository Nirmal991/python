class ProductNotFoundError(Exception):
    def __init__(self, productId):
        self.productId = productId
        print(f'{self.productId} is not present in catalog')

        ...

class OutOfStockError(Exception):
    def __init__(self, quantity = 0):
        self.quantity = quantity
        print(f"The customer's ordered {self.quantity} exceeds the available stock")

def process_order(catalog: dict, order: dict):
    order_prod = order.keys()
    total = 0
    for order_id in list(order_prod):
        if catalog.get(order_id) == None:
            raise ProcessLookupError(order_id)
        elif catalog.get(order_id).get("stock") < order.get(order_id):
            raise OutOfStockError(order.get(order_id))
        else: 
            catalog.update(
                {
                    order_id: {
                        "price": catalog.get(order_id).get("price"),
                        "stock": (catalog.get(order_id).get("stock") - order.get(order_id))
                    }
                }
            )
            print(catalog)
            total += catalog.get(order_id).get("price") * order.get(order_id)
        return float(total)