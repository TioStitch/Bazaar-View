import requests

data = requests.get(url = "https://api.hypixel.net/v2/skyblock/bazaar").json()

def view(item_type: str, item_amount: int):

    print("[BazaarView] Status da API: {}".format(check_api_status()))

    bazaar_products = data["products"]
    selected_product = bazaar_products[item_type]
    quick_status = selected_product["quick_status"]


    sell_price = quick_status["sellPrice"]
    buy_price = quick_status["buyPrice"]

    print()
    print("PRODUCT ID: {}".format(quick_status["productId"]))
    print()
    print("Bazaar:")
    print("Unidade: 1x")
    print("Valor de Compra: {0:.2f}".format(buy_price))
    print("Valor de Venda: {0:.2f}".format(sell_price))
    print()
    print("Sua quantidade: {}x".format(item_amount))
    print("Valor de Compra: {0:.2f}".format((item_amount * buy_price)))
    print("Valor de Venda: {0:.2f}".format((item_amount * sell_price)))
    print()
    
    return 0

def check_api_status():
    return data["success"];

def start_application():
    print("[BazaarView] Insira o tipo do item junto com a sua data")
    print("[BazaarView] Exemplo: (INK_SACK:3) ou (EMERALD)")

    item_type:str = input("->")

    print("[BazaarView] Tipo do Item: {}".format(item_type))

    print("[BazaarView] Insira a quantidade do item:")
    item_amount:float = float(input("->"))

    print("[BazaarView] Quantidade selecionada{}".format(item_amount))

    print()
    print("Processando item...")
    view(item_type, item_amount)

start_application()