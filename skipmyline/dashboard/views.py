# import requests
# from django.shortcuts import render

# def dashboard(request):
#     # ngrok URL
#     ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"

#     try:
#         response = requests.get(ngrok_url)
#         response.raise_for_status()
#         data = response.json()
#         print("Full API Response:", data)
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         data = {}  

#     # Extract data
#     qr_data = data.get("QR:", [])
#     ranks_data = data.get("RANKS:", {})
#     total_products_in_stock = len(qr_data)
#     out_products_str = "No products out of stock"
#     empty_shelves = ranks_data.get("empty_racks", [])
#     mismatch_info = ranks_data.get("mismatch_info", {})
#     stock_info = ranks_data.get("stock_info", {})

#     print("Stock Info Found:", stock_info)

#     # Process stock information
#     rack_status = {}

#     for rack, stock_list in stock_info.items():
#         if stock_list and isinstance(stock_list[0], dict):  # Ensure it's a dict inside a list
#             product_status = [
#                 (product, 'full_stock' if stock_level == 2 else 'low_stock' if stock_level == 1 else 'no_stock' if stock_level == 0 else 'default')  # Handle unknown stock levels
#                 for product, stock_level in stock_list[0].items()
#             ]
#             rack_status[rack] = product_status

#     print("Processed Rack Status:", rack_status)

#     out_products = data.get("OutProducts:", [])
#     out_products_str = ", ".join(out_products) if out_products else "No products out of stock"

#     context = {
#         "total_products_in_stock": total_products_in_stock,
#         "total_products_out_of_stock": len(out_products),
#         "shelves_out_of_stock_percentage": out_products_str,
#         "shelf_usage_percentage": 100 - 20,  # Placeholder percentage
#         "loaded_shelves_count": 5 - len(empty_shelves),
#         "empty_shelves_count": len(empty_shelves),
#         "products": qr_data,  
#         "mismatch_info": mismatch_info,  
#         "rack_status": rack_status,
#         "out_products_str": out_products_str,
#     }

#     return render(request, "dashboard/dashboard.html", context)





import requests
from django.shortcuts import render

def dashboard(request):
    # ngrok URL (commented out since it's not in use)
    ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"

    try:
        response = requests.get(ngrok_url)
        response.raise_for_status()
        data = response.json()
        print("Full API Response:", data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = {}

    # Extract data
    qr_data = data.get("QR:", [])
    ranks_data = data.get("RANKS:", {})
    total_products_in_stock = len(qr_data)
    out_products = data.get("OutProducts:", [])
    out_products_str = ", ".join(out_products) if out_products else "No products out of stock"
    
    # Extracting rack-related data
    empty_shelves = ranks_data.get("empty_racks", [])
    mismatch_info = ranks_data.get("mismatch_info", {})
    stock_info = ranks_data.get("stock_info", {})

    # Process stock information to update availability and stock level
    rack_status = {}
    for rack, stock_list in stock_info.items():
        if stock_list and isinstance(stock_list[0], dict):  # Ensure it's a dict inside a list
            product_status = [
                (product, 'full_stock' if stock_level == 2 else 'low_stock' if stock_level == 1 else 'no_stock' if stock_level == 0 else 'default')
                for product, stock_level in stock_list[0].items()
            ]
            rack_status[rack] = product_status

    # Calculate product availability for the table
    for product in qr_data:
        product_name = product["P_name"]
        for rack, stock_list in stock_info.items():
            if stock_list:
                for stock_item in stock_list[0].items():
                    if stock_item[0] == product_name:
                        product["stock_level"] = stock_item[1]

    # Calculate percentage for shelf usage
    total_shelves = 5  # Assuming there are 5 racks as per the example
    loaded_shelves_count = total_shelves - len(empty_shelves)
    shelf_usage_percentage = (loaded_shelves_count / total_shelves) * 100

    # Context data to pass to the template
    context = {
        "total_products_in_stock": total_products_in_stock,
        "total_products_out_of_stock": len(out_products),
        "shelves_out_of_stock_percentage": out_products_str,
        "shelf_usage_percentage": shelf_usage_percentage,
        "loaded_shelves_count": loaded_shelves_count,
        "empty_shelves_count": len(empty_shelves),
        "products": qr_data,
        "mismatch_info": mismatch_info,
        "rack_status": rack_status,
        "out_products_str": out_products_str,
    }

    return render(request, "dashboard/dashboard.html", context)
