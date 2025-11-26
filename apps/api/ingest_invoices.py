import requests
import json
from datetime import date

url = "http://localhost:8000/invoices/"

invoices = [
    {
        "invoice_number": "INV-2324-001",
        "invoice_date": "2023-10-05",
        "gstin": "27ABCDE1234F1Z5",
        "counterparty_gstin": "27XYZAB5678G1Z9",
        "counterparty_name": "Tech Solutions Pvt Ltd",
        "invoice_type": "B2B",
        "items": [
            {
                "hsn_code": "9983",
                "description": "Software Development Services",
                "quantity": 1,
                "unit_price": 50000.00,
                "taxable_value": 50000.00,
                "gst_rate": 18.0
            }
        ]
    },
    {
        "invoice_number": "INV-2324-002",
        "invoice_date": "2023-10-15",
        "gstin": "27ABCDE1234F1Z5",
        "counterparty_gstin": "27LMNOP9012H1Z3",
        "counterparty_name": "Global Traders",
        "invoice_type": "B2B",
        "items": [
            {
                "hsn_code": "8517",
                "description": "Networking Equipment",
                "quantity": 2,
                "unit_price": 25000.00,
                "taxable_value": 50000.00,
                "gst_rate": 18.0
            },
            {
                "hsn_code": "9987",
                "description": "Installation Charges",
                "quantity": 1,
                "unit_price": 5000.00,
                "taxable_value": 5000.00,
                "gst_rate": 18.0
            }
        ]
    },
    {
        "invoice_number": "INV-2324-003",
        "invoice_date": "2023-10-25",
        "gstin": "27ABCDE1234F1Z5",
        "counterparty_gstin": "29PQRST3456J1Z7",
        "counterparty_name": "Bangalore Retailers",
        "invoice_type": "B2B",
        "items": [
            {
                "hsn_code": "8471",
                "description": "Laptops",
                "quantity": 5,
                "unit_price": 40000.00,
                "taxable_value": 200000.00,
                "gst_rate": 18.0
            }
        ]
    }
]

for inv in invoices:
    try:
        response = requests.post(url, json=inv)
        if response.status_code == 200:
            print(f"Created invoice {inv['invoice_number']}")
        else:
            print(f"Failed to create invoice {inv['invoice_number']}: {response.text}")
    except Exception as e:
        print(f"Error creating invoice {inv['invoice_number']}: {e}")
