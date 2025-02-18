
### **🐍 script.py**
```python
import json

try:
    with open("applications.json", "r") as file:
        applications = json.load(file)
except FileNotFoundError:
    applications = []

while True:
    company = input("Enter company name: ")
    status = input("Enter status (Applied/Interview/Offer/Rejected): ")
    applications.append({"Company": company, "Status": status})

    if input("Add another? (yes/no): ").lower() != "yes":
        break

with open("applications.json", "w") as file:
    json.dump(applications, file, indent=4)

print("\n📂 Data Saved!")
