import tkinter as tk
import requests
import json
from tkinter import messagebox

# Correct API base URL
base_url = "https://api.abuseipdb.com/api/v2/check/"

ip_list = []

headers = {
    'Accept': 'application/json',
    'Key': 'b805668b00a4a2fb72f2d554d51aacc93a7941d9a8f6ac58eb2d94b37094a1c06caa939d677b0798'  # Use an environment variable for security
}

def check_ip():
    ip_input = ip_entry.get("1.0", "end-1c")
    ip_addresses = [ip.strip() for ip in ip_input.splitlines() if ip.strip()]
    
    if not ip_addresses:
        messagebox.showerror("Error", "No valid IP addresses entered!")
        return

    for ip in ip_addresses:
        url = f"{base_url}"
        
        # Request data for the current IP
        response = requests.get(url, headers=headers, params={'ipAddress': ip, 'maxAgeInDays': '90'})
        
        if response.status_code == 200:
            decoded_response = response.json()
            raw_output = decoded_response.get("data", {})
            
            # Extract the desired fields
            formatted_output = {
                '\nIP Address': raw_output.get("ipAddress"),
                'ISP': raw_output.get("isp"),
                'Country Code': raw_output.get("countryCode"),
                'Domain': raw_output.get("domain"),
                'Abuse Rating': raw_output.get("abuseConfidenceScore")
            }
            output_string = '\n'.join([f"{key}: {value}" for key, value in formatted_output.items()])
            print(output_string)
        else:
            print(f"Error fetching data for {ip}: {response.status_code}")

# Set up the main window
root = tk.Tk()
root.title("IP Address Checker")

label = tk.Label(root, text="Enter IP addresses:")
label.pack(pady=10)

ip_entry = tk.Text(root, height=10, width=40)
ip_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_ip)
submit_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
