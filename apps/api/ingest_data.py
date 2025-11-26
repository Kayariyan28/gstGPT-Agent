import requests
import json

url = "http://localhost:8000/chat/ingest"

gst_knowledge = [
    "Goods and Services Tax (GST) is a destination-based tax on consumption of goods and services. It is proposed to be levied at all stages right from manufacture up to final consumption with credit of taxes paid at previous stages available as setoff. In a nutshell, only value addition will be taxed and burden of tax is to be borne by the final consumer.",
    "The GST replaces a slew of indirect taxes with a unified tax and is therefore set to reshape the country's 2.4 trillion dollar economy.",
    "There are three components of GST: CGST (Central Goods and Services Tax), SGST (State Goods and Services Tax), and IGST (Integrated Goods and Services Tax).",
    "CGST is collected by the Central Government on an intra-state sale (e.g., transaction happening within Maharashtra).",
    "SGST is collected by the State Government on an intra-state sale (e.g., transaction happening within Maharashtra).",
    "IGST is collected by the Central Government for inter-state sale (e.g., Maharashtra to Tamil Nadu).",
    "GSTR-1 is a monthly or quarterly return that should be filed by every registered GST taxpayer. It contains details of all outward supplies i.e., sales.",
    "GSTR-3B is a self-declared summary monthly return. It is filed by every registered GST taxpayer for each tax period. It contains summary figures of sales, input tax credit (ITC) claimed, and net tax payable.",
    "Input Tax Credit (ITC) means at the time of paying tax on output, you can reduce the tax you have already paid on inputs and pay the balance amount.",
    "The standard GST rates in India are 0%, 5%, 12%, 18%, and 28%.",
    "GSTIN is a 15-digit Goods and Services Tax Identification Number."
]

payload = {"texts": gst_knowledge}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Successfully ingested {len(gst_knowledge)} documents.")
        print("Response:", response.json())
    else:
        print(f"Failed to ingest. Status: {response.status_code}")
        print("Response:", response.text)
except Exception as e:
    print(f"Error: {e}")
