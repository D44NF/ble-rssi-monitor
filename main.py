import asyncio
import threading
from bleak import BleakScanner
import customtkinter as ctk

devices = {}
rows = {}

def detection_callback(device, advertisement_data):
    name = device.name or "Unbekannt"
    rssi = advertisement_data.rssi

    if device.address not in devices:
        devices[device.address] = {
            "name": name,
            "rssi": rssi
        }
    else:
        devices[device.address]["rssi"] = rssi


#BLE LOOP
async def ble_loop():
    scanner = BleakScanner(detection_callback)
    await scanner.start()

    while True:
        await asyncio.sleep(0.5)

def start_ble():
    asyncio.run(ble_loop())

threading.Thread(target=start_ble, daemon=True).start()


#UI
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("600x500")
app.title("📡 Bluetooth Tabelle")

title = ctk.CTkLabel(app, text="Bluetooth Geräte", font=("Arial", 20))
title.pack(pady=10)

frame = ctk.CTkScrollableFrame(app, width=550, height=400)
frame.pack(pady=10)

header = ctk.CTkFrame(frame)
header.pack(fill="x")

ctk.CTkLabel(header, text="Gerät", width=300).pack(side="left")
ctk.CTkLabel(header, text="RSSI", width=100).pack(side="right")


def update_ui():
    global rows

    for addr, dev in list(devices.items()):

        if addr not in rows:
            row = ctk.CTkFrame(frame)
            row.pack(fill="x", pady=2)

            name_label = ctk.CTkLabel(row, text=dev["name"], width=300, anchor="w")
            name_label.pack(side="left")

            rssi_label = ctk.CTkLabel(row, text=str(dev["rssi"]), width=100)
            rssi_label.pack(side="right")

            rows[addr] = rssi_label

        else:
            rows[addr].configure(text=str(dev["rssi"]))

    app.after(300, update_ui)

update_ui()

app.mainloop()