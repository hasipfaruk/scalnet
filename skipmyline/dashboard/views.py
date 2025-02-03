
# import requests
# from django.shortcuts import render

# def dashboard(request):
#     # ngrok URL (it may change over time, store it properly in a config)
#     # ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"
#     ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"
#     try:
#         # response = requests.get(ngrok_url)
#         # response.raise_for_status()  # Raises HTTPError if status code is 4xx/5xx
#         # data = response.json()  # Converts response to JSON
#         # data = data  # Converts response to JSON
        
#         # Example data
#         data={
#     "OutProducts": [
#         "Gatriode, Lemon Drink",
#         "Morton Regular Salt",
#         "Imperial Fine Sugar"
#     ],
#     "QR": [
#         {
#             "Code": 794147617426,
#             "P_name": "Gatriode, Lemon Drink",
#             "P_price": 1.88,
#             "bbox": [951, 651, 1119, 819],
#             "height": 168
#         },
#         {
#             "Code": 511054320215,
#             "P_name": "Pringles, Potato Chips",
#             "P_price": 2.24,
#             "bbox": [1850, 1764, 2013, 1940],
#             "height": 176
#         },
#         {
#             "Code": 201072408854,
#             "P_name": "POWERADE Electrolyte",
#             "P_price": 1.38,
#             "bbox": [1920, 654, 2082, 820],
#             "height": 166
#         },
#         {
#             "Code": 808175554880,
#             "P_name": "Pringles Sour Cream",
#             "P_price": 2.24,
#             "bbox": [939, 1747, 1111, 1915],
#             "height": 168
#         },
#         {
#             "Code": 572310636212,
#             "P_name": "Morton Regular Salt",
#             "P_price": 12.98,
#             "bbox": [696, 1277, 892, 1467],
#             "height": 190
#         },
#         {
#             "Code": 81188508750,
#             "P_name": "Imperial Fine Sugar",
#             "P_price": 8.94,
#             "bbox": [1796, 1241, 1984, 1429],
#             "height": 188
#         }
#     ],
#     "RANKS": {
#         "mismatch_info": {
#             "1": ["small_imperial_suger"],
#             "2": ["big_imperial_suger"],
#             "3": ["big_imperial_suger", "big_imperial_suger", "pepsi_can", "pepsi_can"]
#         },
#         "stock_info": {
#             "1": [{"small_imperial_suger": 0, "big_imperial_suger": 1}],
#             "2": [{"pepsi_can": 0, "coke_can": 2}],
#             "3": [{"Power lemon": 1, "Gatredo drink": 2}],
#             "4": [{"Gourmet food": 2, "Next COla": 0}]
#         }
#     }
# }
#         # data={'OutProducts:': ['POWERADE Electrolyte', 'Gatriode, Lemon Drink'], 'QR:': [{'Code': 511054320215, 'P_name': 'Pringles, Potato Chips', 'P_price': 2.24, 'bbox': [1901, 1850, 2071, 2027], 'height': 177}, {'Code': 808175554880, 'P_name': 'Pringles Sour Cream', 'P_price': 2.24, 'bbox': [980, 1811, 1154, 1988], 'height': 177}, {'Code': 201072408854, 'P_name': 'POWERADE Electrolyte', 'P_price': 1.38, 'bbox': [1976, 706, 2151, 878], 'height': 172}, {'Code': 794147617426, 'P_name': 'Gatriode, Lemon Drink', 'P_price': 1.88, 'bbox': [985, 701, 1157, 878], 'height': 177}], 'RANKS:': {'empty_racks': [], 'mismatch_info': {'1': [], '2': ['big_imperial_suger']}, 'stock_info': {'2': ['low stock'], '5': ['no stock'], '3': ['Full stock'], '1': ['low stock']}}}
#         # data={'OutProducts:': ['POWERADE Electrolyte', 'Gatriode, Lemon Drink'], 'QR:': [{'Code': 511054320215, 'P_name': 'Pringles, Potato Chips', 'P_price': 2.24, 'bbox': [1901, 1850, 2071, 2027], 'height': 177}, {'Code': 808175554880, 'P_name': 'Pringles Sour Cream', 'P_price': 2.24, 'bbox': [980, 1811, 1154, 1988], 'height': 177}, {'Code': 201072408854, 'P_name': 'POWERADE Electrolyte', 'P_price': 1.38, 'bbox': [1976, 706, 2151, 878], 'height': 172}, {'Code': 794147617426, 'P_name': 'Gatriode, Lemon Drink', 'P_price': 1.88, 'bbox': [985, 701, 1157, 878], 'height': 177}], 'RANKS:': {'empty_racks': [1,3], 'mismatch_info': {'1': [], '1': ['big_imperial_suger','Demo'], '4': ['demo VAlue']},  'stock_info': {'1': ['Low stock'], '2': ['Full stock'], }}}
#         print("data",data)
#     except requests.exceptions.RequestException as e:
#         # Log the error or handle accordingly
#         print(f"Error fetching data: {e}")
#         data = {}  # Return empty data on error
        
    
#     # Process the data
#     # qr_data = data.get("QR:", [])
#     qr_data = data.get("QR", [])
#     # ranks_data = data.get("RANKS: ", {})
#     ranks_data = data.get("RANKS", {})

#     total_products_in_stock = len(qr_data)
#     empty_shelves = ranks_data.get("empty_racks", [])
#     mismatch_info = ranks_data.get("mismatch_info", {})
#     stock_info = ranks_data.get("stock_info", {})
#     # Rember
#     emp_rack = ranks_data.get("empty_racks", [])
#     print("emp_rack", emp_rack)

#     # Example calculation for shelf usage
    
#     # shelves_out_of_stock_percentage = len(empty_shelves) / 10 * 100 if total_products_in_stock else 0
#     shelves_out_of_stock_percentage = 255
#     print("shelves_out_of_stock_percentage", shelves_out_of_stock_percentage)

#     rack_status = {}

#     for rack, stock_list in stock_info.items():
        
        
#         if stock_list and stock_list[0].strip().lower() == 'full stock':  # Handle leading/trailing spaces
#             # print("full stock rack condition")
            
#             # print("stock_list[1].strip().lower()" , stock_list[1].strip().lower())
#             rack_status[rack] = 'full_stock'  # Green color
#         elif stock_list  and stock_list[0].strip().lower() == 'low stock':  # Ensure safe access
#                 rack_status[rack] = 'low_stock'  # Yellow color
#         # else:
#         #     rack_status[rack] = 'no_stock'  # Red color
       

#     print(rack_status)  # This will help you confirm if the dictionary is correct
#     if emp_rack:
        
#         for lst in emp_rack:
#             rack_status[lst] = 'no_stock'
#     # mismatch_info= {}  # Example data``
#     # mismatch_info= {'2': ['Mismatch in rack 2']}  # Example data
#     # mismatch_info= {'1': ['']}
#     print("mismatch info",mismatch_info)
#     out_products = data.get("OutProducts:", {})
#     if out_products:
#         my_string = ", ".join(out_products)
#     else:
#         my_string = "No any product Found!"
        
#     print("Out Product", out_products)
#     # if out_products:
#     #         for a in out_products:
#     #             "shelves_out_of_stock_percentage": a,
#     context = {
#         "total_products_in_stock": total_products_in_stock,
#         "total_products_out_of_stock": len(empty_shelves),
#         # "shelves_out_o,f_stock_percentage": shelves_out_of_stock_percentage,
#         # ////////////////////////////////////////////////////////////
        
#         # ////////////////////////////////////////////////////////////
#         "shelves_out_of_stock_percentage": my_string,
#         # "shelf_usage_percentage": 100 - shelves_out_of_stock_percentage,
#         "shelf_usage_percentage": 100 - 20,
#         "loaded_shelves_count": 5 - len(empty_shelves),
#         "empty_shelves_count": len(empty_shelves),
#         "products": qr_data,  # For the product table
#         "mismatch_info": mismatch_info,  # Ensure this is structured correctly in the template
#         # "mismatch_info": mismatch_info['1'][0],  # Ensure this is structured correctly in the template
#         "rack_status": rack_status,  # Add rack statuses to the context
#     }

#     return render(request, "dashboard/dashboard.html", context)



# new code is here
import requests
from django.shortcuts import render

def dashboard(request):
    # Store ngrok URL in an environment variable or settings file
    ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"
    
    try:
        # response = requests.get(ngrok_url)
        # response.raise_for_status()
        # data = response.json()
        
        # Mock JSON response (for testing)
        {
    "OutProducts": [
        "Gatriode, Lemon Drink",
        "Morton Regular Salt",
        "Imperial Fine Sugar"
    ],
    "QR": [
        {
            "Code": 794147617426,
            "P_name": "Gatriode, Lemon Drink",
            "P_price": 1.88,
            "bbox": [951, 651, 1119, 819],
            "height": 168
        },
        {
            "Code": 511054320215,
            "P_name": "Pringles, Potato Chips",
            "P_price": 2.24,
            "bbox": [1850, 1764, 2013, 1940],
            "height": 176
        },
        {
            "Code": 201072408854,
            "P_name": "POWERADE Electrolyte",
            "P_price": 1.38,
            "bbox": [1920, 654, 2082, 820],
            "height": 166
        },
        {
            "Code": 808175554880,
            "P_name": "Pringles Sour Cream",
            "P_price": 2.24,
            "bbox": [939, 1747, 1111, 1915],
            "height": 168
        },
        {
            "Code": 572310636212,
            "P_name": "Morton Regular Salt",
            "P_price": 12.98,
            "bbox": [696, 1277, 892, 1467],
            "height": 190
        },
        {
            "Code": 81188508750,
            "P_name": "Imperial Fine Sugar",
            "P_price": 8.94,
            "bbox": [1796, 1241, 1984, 1429],
            "height": 188
        }
    ],
    "RANKS": {
        "mismatch_info": {
            "1": ["small_imperial_suger"],
            "2": ["big_imperial_suger"],
            "3": ["big_imperial_suger", "big_imperial_suger", "pepsi_can", "pepsi_can"]
        },
        "stock_info": {
            "1": [{"small_imperial_suger": 0, "big_imperial_suger": 1}],
            "2": [{"pepsi_can": 0, "coke_can": 2}],
            "3": [{"Power lemon": 1, "Gatredo drink": 2}],
            "4": [{"Gourmet food": 2, "Next COla": 0}]
        }
    }
}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = {}

    # Extract data safely
    qr_data = data.get("QR", [])
    ranks_data = data.get("RANKS", {})
    empty_shelves = ranks_data.get("empty_racks", [])
    mismatch_info = ranks_data.get("mismatch_info", {})
    stock_info = ranks_data.get("stock_info", {})
    total_products_in_stock = len(qr_data)

    # Calculate shelf usage percentage
    total_shelves = 10  # Adjust based on your dataset
    shelves_out_of_stock_percentage = (len(empty_shelves) / total_shelves) * 100 if total_shelves else 0

    # Rack status
    rack_status = {}
    for rack, stock_list in stock_info.items():
        for stock_dict in stock_list:
            for item, qty in stock_dict.items():
                if qty == 0:
                    rack_status[rack] = 'no_stock'
                elif qty > 0 and qty <= 2:
                    rack_status[rack] = 'low_stock'
                else:
                    rack_status[rack] = 'full_stock'

    # Ensure empty racks are marked correctly
    for rack in empty_shelves:
        rack_status[rack] = 'no_stock'

    # Convert out-of-stock products to a string
    out_products = data.get("OutProducts", [])
    out_products_string = ", ".join(out_products) if out_products else "No products found"

    # Context for template
    context = {
        "total_products_in_stock": total_products_in_stock,
        "total_products_out_of_stock": len(empty_shelves),
        "shelves_out_of_stock_percentage": shelves_out_of_stock_percentage,
        "shelf_usage_percentage": 100 - shelves_out_of_stock_percentage,
        "loaded_shelves_count": total_shelves - len(empty_shelves),
        "empty_shelves_count": len(empty_shelves),
        "products": qr_data,
        "mismatch_info": mismatch_info,
        "rack_status": rack_status,
    }

    return render(request, "dashboard/dashboard.html", context)
import requests
from django.shortcuts import render

def dashboard(request):
    # Store ngrok URL in an environment variable or settings file
    ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"
    
    try:
        # response = requests.get(ngrok_url)
        # response.raise_for_status()
        # data = response.json()
        
        # Mock JSON response (for testing)
        {
    "OutProducts": [
        "Gatriode, Lemon Drink",
        "Morton Regular Salt",
        "Imperial Fine Sugar"
    ],
    "QR": [
        {
            "Code": 794147617426,
            "P_name": "Gatriode, Lemon Drink",
            "P_price": 1.88,
            "bbox": [951, 651, 1119, 819],
            "height": 168
        },
        {
            "Code": 511054320215,
            "P_name": "Pringles, Potato Chips",
            "P_price": 2.24,
            "bbox": [1850, 1764, 2013, 1940],
            "height": 176
        },
        {
            "Code": 201072408854,
            "P_name": "POWERADE Electrolyte",
            "P_price": 1.38,
            "bbox": [1920, 654, 2082, 820],
            "height": 166
        },
        {
            "Code": 808175554880,
            "P_name": "Pringles Sour Cream",
            "P_price": 2.24,
            "bbox": [939, 1747, 1111, 1915],
            "height": 168
        },
        {
            "Code": 572310636212,
            "P_name": "Morton Regular Salt",
            "P_price": 12.98,
            "bbox": [696, 1277, 892, 1467],
            "height": 190
        },
        {
            "Code": 81188508750,
            "P_name": "Imperial Fine Sugar",
            "P_price": 8.94,
            "bbox": [1796, 1241, 1984, 1429],
            "height": 188
        }
    ],
    "RANKS": {
        "mismatch_info": {
            "1": ["small_imperial_suger"],
            "2": ["big_imperial_suger"],
            "3": ["big_imperial_suger", "big_imperial_suger", "pepsi_can", "pepsi_can"]
        },
        "stock_info": {
            "1": [{"small_imperial_suger": 0, "big_imperial_suger": 1}],
            "2": [{"pepsi_can": 0, "coke_can": 2}],
            "3": [{"Power lemon": 1, "Gatredo drink": 2}],
            "4": [{"Gourmet food": 2, "Next COla": 0}]
        }
    }
}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = {}

    # Extract data safely
    qr_data = data.get("QR", [])
    ranks_data = data.get("RANKS", {})
    empty_shelves = ranks_data.get("empty_racks", [])
    mismatch_info = ranks_data.get("mismatch_info", {})
    stock_info = ranks_data.get("stock_info", {})
    total_products_in_stock = len(qr_data)

    # Calculate shelf usage percentage
    total_shelves = 10  # Adjust based on your dataset
    shelves_out_of_stock_percentage = (len(empty_shelves) / total_shelves) * 100 if total_shelves else 0

    # Rack status
    rack_status = {}
    for rack, stock_list in stock_info.items():
        for stock_dict in stock_list:
            for item, qty in stock_dict.items():
                if qty == 0:
                    rack_status[rack] = 'no_stock'
                elif qty > 0 and qty <= 2:
                    rack_status[rack] = 'low_stock'
                else:
                    rack_status[rack] = 'full_stock'

    # Ensure empty racks are marked correctly
    for rack in empty_shelves:
        rack_status[rack] = 'no_stock'

    # Convert out-of-stock products to a string
    out_products = data.get("OutProducts", [])
    out_products_string = ", ".join(out_products) if out_products else "No products found"

    # Context for template
    context = {
        "total_products_in_stock": total_products_in_stock,
        "total_products_out_of_stock": len(empty_shelves),
        "shelves_out_of_stock_percentage": shelves_out_of_stock_percentage,
        "shelf_usage_percentage": 100 - shelves_out_of_stock_percentage,
        "loaded_shelves_count": total_shelves - len(empty_shelves),
        "empty_shelves_count": len(empty_shelves),
        "products": qr_data,
        "mismatch_info": mismatch_info,
        "rack_status": rack_status,
    }

    return render(request, "dashboard/dashboard.html", context)
import requests
from django.shortcuts import render

def dashboard(request):
    # Store ngrok URL in an environment variable or settings file
    ngrok_url = "https://34da-2600-1700-d870-2a80-df0b-c905-c2b2-b7e6.ngrok-free.app/capture"
    
    try:
        # response = requests.get(ngrok_url)
        # response.raise_for_status()
        # data = response.json()
        
        # Mock JSON response (for testing)
        data={
    "OutProducts": [
        "Gatriode, Lemon Drink",
        "Morton Regular Salt",
        "Imperial Fine Sugar"
    ],
    "QR": [
        {
            "Code": 794147617426,
            "P_name": "Gatriode, Lemon Drink",
            "P_price": 1.88,
            "bbox": [951, 651, 1119, 819],
            "height": 168
        },
        {
            "Code": 511054320215,
            "P_name": "Pringles, Potato Chips",
            "P_price": 2.24,
            "bbox": [1850, 1764, 2013, 1940],
            "height": 176
        },
        {
            "Code": 201072408854,
            "P_name": "POWERADE Electrolyte",
            "P_price": 1.38,
            "bbox": [1920, 654, 2082, 820],
            "height": 166
        },
        {
            "Code": 808175554880,
            "P_name": "Pringles Sour Cream",
            "P_price": 2.24,
            "bbox": [939, 1747, 1111, 1915],
            "height": 168
        },
        {
            "Code": 572310636212,
            "P_name": "Morton Regular Salt",
            "P_price": 12.98,
            "bbox": [696, 1277, 892, 1467],
            "height": 190
        },
        {
            "Code": 81188508750,
            "P_name": "Imperial Fine Sugar",
            "P_price": 8.94,
            "bbox": [1796, 1241, 1984, 1429],
            "height": 188
        }
    ],
    "RANKS": {
        "mismatch_info": {
            "1": ["small_imperial_suger"],
            "2": ["big_imperial_suger"],
            "3": ["big_imperial_suger", "big_imperial_suger", "pepsi_can", "pepsi_can"]
        },
        "stock_info": {
            "1": [{"small_imperial_suger": 0, "big_imperial_suger": 1}],
            "2": [{"pepsi_can": 0, "coke_can": 2}],
            "3": [{"Power lemon": 1, "Gatredo drink": 2}],
            "4": [{"Gourmet food": 2, "Next COla": 0}]
        }
    }
}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = {}

    # Extract data safely
    qr_data = data.get("QR", [])
    ranks_data = data.get("RANKS", {})
    empty_shelves = ranks_data.get("empty_racks", [])
    mismatch_info = ranks_data.get("mismatch_info", {})
    stock_info = ranks_data.get("stock_info", {})
    total_products_in_stock = len(qr_data)

    # Calculate shelf usage percentage
    total_shelves = 10  # Adjust based on your dataset
    shelves_out_of_stock_percentage = (len(empty_shelves) / total_shelves) * 100 if total_shelves else 0

    # Rack status
    rack_status = {}
    for rack, stock_list in stock_info.items():
        for stock_dict in stock_list:
            for item, qty in stock_dict.items():
                if qty == 0:
                    rack_status[rack] = 'no_stock'
                elif qty > 0 and qty <= 2:
                    rack_status[rack] = 'low_stock'
                else:
                    rack_status[rack] = 'full_stock'

    # Ensure empty racks are marked correctly
    for rack in empty_shelves:
        rack_status[rack] = 'no_stock'

    # Convert out-of-stock products to a string
    out_products = data.get("OutProducts", [])
    out_products_string = ", ".join(out_products) if out_products else "No products found"

    # Context for template
    context = {
        "total_products_in_stock": total_products_in_stock,
        "total_products_out_of_stock": len(empty_shelves),
        "shelves_out_of_stock_percentage": shelves_out_of_stock_percentage,
        "shelf_usage_percentage": 100 - shelves_out_of_stock_percentage,
        "loaded_shelves_count": total_shelves - len(empty_shelves),
        "empty_shelves_count": len(empty_shelves),
        "products": qr_data,
        "mismatch_info": mismatch_info,
        "rack_status": rack_status,
    }

    return render(request, "dashboard/dashboard.html", context)
