import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(1)


Network_Security_Types = {
    0: "Open (no password)",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK",
    5: "WPA2-PSK"
}   


print ("---- Network Scanner ----")
print("Scanning for networks...")
networks = wlan.scan()
def signal_strength(rssi):
    if rssi >= -50:
        return "Amazing"
    elif rssi >= -60:
        return "Good"
    elif rssi >= -70:
        return "Okay"
    else:
        return "Weak"

print(f"Found {len(networks)} available networks:")

for net in networks:
    ssid = net[0].decode("utf-8")
    ssid = ssid.strip("\x00")
    if ssid == "":
        ssid = "(HIDDEN NETWORK)"
    rssi = net[3]
    signal_rating = signal_strength(rssi)
    security_code = net[4]
    security_label = Network_Security_Types.get(security_code, "Unknown: Could not find it.")

    print(f"SSID: {ssid}, Signal: {rssi} ({signal_rating}), Security: {security_label}")

    if security_label == "Open (no password)" or security_label == "WEP":
        print("This network uses weak or has no security and is susceptible to attacks.")
