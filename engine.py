import json
from datetime import datetime
DATA = []

def add_data():
    while True:
        try:
            category = input("Enter category: ").strip()
            amount = float(input("Enter amount: ").strip())
            date = input("Enter date (YYYY-MM-DD): ").strip()
            
            
            datetime.strptime(date, "%Y-%m-%d")

           
            DATA.append({"id": len(DATA) + 1, "category": category, "amount": amount, "date": date})
            
          
            more = input("Do you want to add more data? (yes/no): ").strip().lower()
            if more != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount and date (YYYY-MM-DD).")


def filter_data(category=None, start_date=None, end_date=None):
    filtered_data = DATA
    if category:
        filtered_data = [entry for entry in filtered_data if entry["category"] == category]
    if start_date:
        filtered_data = [entry for entry in filtered_data if entry["date"] >= start_date]
    if end_date:
        filtered_data = [entry for entry in filtered_data if entry["date"] <= end_date]
    return filtered_data


def generate_report():
    category = input("Enter category filter (or press Enter to skip): ").strip()
    start_date = input("Enter start date (YYYY-MM-DD) (or press Enter to skip): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD) (or press Enter to skip): ").strip()

   
    try:
        if start_date:
            datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    
    report_data = filter_data(category if category else None, start_date if start_date else None, end_date if end_date else None)

    
    output_format = input("Choose output format (json/text): ").strip().lower()

    if output_format == "json":
        print("\nGenerated Report (JSON Format):")
        print(json.dumps(report_data, indent=2))
    elif output_format == "text":
        print("\nGenerated Report (Text Format):")
        for entry in report_data:
            print(f"ID: {entry['id']}, Category: {entry['category']}, Amount: {entry['amount']}, Date: {entry['date']}")
    else:
        print("Invalid format. Please choose 'json' or 'text'.")


add_data()
generate_report()