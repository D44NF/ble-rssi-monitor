import asyncio
import threading
from bleak import BleakScanner
import customtkinter as ctk

devices = {}
rows = {}
show_unknown = True

def detection_callback(device, advertisement_data):
    name = device.name or "Unknown"
    rssi = advertisement_data.rssi

    devices[device.address] = {
        "name": name,
        "rssi": rssi
    }

async def ble_loop():
    scanner = BleakScanner(detection_callback)
    await scanner.start()

    while True:
        await asyncio.sleep(0.5)

def start_ble():
    asyncio.run(ble_loop())

threading.Thread(target=start_ble, daemon=True).start()

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x700")
app.title("BLE Radar UI")

title = ctk.CTkLabel(app, text="Bluetooth Radar", font=("Arial", 28, "bold"))
title.pack(pady=10)

def toggle_unknown():
    global show_unknown
    show_unknown = checkbox.get()

def reload_list():
    global rows
    for widget in table_frame.winfo_children():
        widget.destroy()
    rows = {}

checkbox = ctk.CTkCheckBox(app, text="Show Unknown Devices", command=toggle_unknown)
checkbox.select()
checkbox.pack(pady=5)

reload_button = ctk.CTkButton(app, text="Reload", command=reload_list)
reload_button.pack(pady=5)

table_frame = ctk.CTkScrollableFrame(app, width=850, height=550)
table_frame.pack(pady=10)

header = ctk.CTkFrame(table_frame)
header.pack(fill="x", pady=5)

ctk.CTkLabel(header, text="Device Name", font=("Arial", 18, "bold"), width=500).pack(side="left", padx=10)
ctk.CTkLabel(header, text="RSSI", font=("Arial", 18, "bold"), width=200).pack(side="right", padx=10)

def update_ui():
    global rows

    snapshot = list(devices.items())

    for addr, dev in snapshot:

        name = dev["name"]

        if not show_unknown and name == "Unknown":
            continue

        if addr not in rows:
            row = ctk.CTkFrame(table_frame)
            row.pack(fill="x", pady=3)

            name_label = ctk.CTkLabel(row, text=name, font=("Arial", 16), width=500, anchor="w")
            name_label.pack(side="left", padx=10)

            rssi_label = ctk.CTkLabel(row, text=str(dev["rssi"]), font=("Arial", 16), width=200)
            rssi_label.pack(side="right", padx=10)

            rows[addr] = (name_label, rssi_label)

        else:
            _, rssi_label = rows[addr]
            rssi_label.configure(text=str(dev["rssi"]))

    app.after(300, update_ui)

update_ui()
app.mainloop()