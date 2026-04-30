📡 BLE Radar UI

A Bluetooth Low Energy (BLE) scanner with a real-time UI that displays nearby devices and continuously updates their RSSI (signal strength).

⸻

🚀 Features

* Live scanning of nearby BLE devices
* Real-time RSSI (signal strength) updates
* Clean table-based UI
* Automatically detects new devices
* Stable background scanning with UI refresh

⸻

🖥️ Preview

(Add a screenshot here of your app UI)

⸻

📦 Requirements

* Python 3.10+
* macOS / Windows / Linux (BLE support required)

⸻

🔧 Installation

Install dependencies:

pip install bleak customtkinter

⸻

▶️ Usage

Run the application:

python main.py

Make sure Bluetooth is enabled on your device before starting.

⸻

📊 How it works

* The app scans for nearby BLE devices
* Each device is stored once and updated continuously
* RSSI values indicate signal strength:
    * closer to 0 → stronger signal (closer device)
    * more negative → weaker signal (farther away)

Example:

Device Name | RSSI
AirPods     | -45
iPhone      | -62
Unknown     | -80

⸻

⚠️ Notes

* RSSI is only an approximation of distance
* macOS may limit scan frequency due to system permissions
* Some devices may appear multiple times depending on advertising behavior

⸻

🧠 Idea

This project was built as a simple BLE visualization tool to understand how Bluetooth signal strength can be used for proximity estimation.

⸻

📄 License

MIT License (optional)