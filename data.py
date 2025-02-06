import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

search_terms = ["laptop", "wireless earbuds", "coffee mug", "smartphone", "headphones",
                "gaming chair", "keyboard", "mouse", "external hard drive", "phone case", "shoes", "socks", "dresses", "water bottle"]

# Define search results
search_results_dict = {
    "laptop": ["Dell XPS 13", "MacBook Air", "HP Spectre x360"],
    "wireless earbuds": ["AirPods Pro", "Sony WF-1000XM4", "Bose QuietComfort Earbuds"],
    "coffee mug": ["Ceramic Mug", "Travel Mug", "Insulated Mug"],
    "smartphone": ["iPhone 15", "Samsung Galaxy S24", "Google Pixel 8"],
    "headphones": ["Sony WH-1000XM5", "Bose 700", "Sennheiser Momentum 4"],
    "gaming chair": ["DXRacer", "Secretlab Titan", "Razer Iskur"],
    "keyboard": ["Logitech MX Keys", "Razer BlackWidow", "Corsair K95"],
    "mouse": ["Logitech MX Master 3", "Razer DeathAdder", "SteelSeries Rival 5"],
    "external hard drive": ["Seagate 2TB", "WD My Passport", "Samsung T7"],
    "phone case": ["OtterBox Defender", "Spigen Tough Armor", "Apple Silicone Case"],
    "shoes": [],
    "socks": [],
    "dresses": [],
    "water bottle": []
}

# Device Types
device_types = ["Mobile", "Desktop", "Tablet"]

# Search Sources
search_sources = ["Homepage", "Category Page", "Product Page"]

# Generate dataset
num_rows = 5000
data = []

start_time = datetime.now() -timedelta(days=30)

for i in range(1,num_rows+1):
    user_id = random.randint(1000, 9999)
    session_id = random.randint(50000, 999999)
    search_term = random.choice(search_terms)
    results_returned = True if len(search_results_dict[search_term]) > 0 else False # np.random.choice([True, False], p=[0.85, 0.15]) # 85% return results
    search_results = search_results_dict[search_term] # if results_returned else []
    clicked_result = results_returned and np.random.choice([True, False], p=[0.7, 0.3])
    clicked_result_name = random.choice(search_results) if clicked_result else None
    search_time_taken = round(random.uniform(0.2, 3.5), 2)
    device_type = random.choice(device_types)
    search_source = random.choice(search_sources)
    conversion = clicked_result and np.random.choice([True, False], p=[0.2, 0.8])
    timestamp = start_time + timedelta(seconds=random.randint(0, 2592000))

    data.append([i, user_id, session_id, timestamp, search_term, device_type, search_source,
                 results_returned, search_results, search_time_taken, clicked_result,
                 clicked_result_name, conversion])

df = pd.DataFrame(data, columns= ["search_id", "user_id", "session_id", "timestamp", "search_term",
                                 "device_type", "search_source", "results_returned",
                                 "search_results", "search_time_taken", "clicked_result",
                                 "clicked_result_name", "conversion"])

df.to_csv("extended_search_data.csv", index=False)