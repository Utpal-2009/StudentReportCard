import pickle as p
#Reading the data back
try:
    with open("data", "rb") as f:
        loaded_data = p.load(f)
        print("==========Student Data==========")
        print("📂 Loaded Data from File:")
        print(loaded_data)
except FileNotFoundError:
    print("❌ Data file not found. Please run the program to save data first.")