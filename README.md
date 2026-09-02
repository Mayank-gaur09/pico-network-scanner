# 🍓 Raspberry Pi Pico 2 W — WiFi Network Scanner

**File:** [Network Scanner](./network_scanner.py)

**Description:** This project uses a Raspberry Pi Pico 2 W running MicroPython to scan for nearby WiFi networks. It shows each network's name, signal strength, security type, and flags any networks with weak or no security such as Open or WEP networks. It is essentially a small hardware based version of a network scanner running on a microcontroller.

## How It Works:

- Turning on the WiFi radio runs a scan, which gives a list of every network it can see nearby.
- Each network's name comes back as raw bytes rather than test, so it needs decoding. Hidden networks come back as a string of null bytes instead of a real name, so these are detected separately and labelled as hidden networks.
- The security type comes back as a number rather than something readable like "WEP", which is translated into an actual label by the dictionary.
- Signal Strength comes back as a negative number which gets converted into a simple word like "Good" or "Okay".
- If a network's security is Weak or non-existent, a warning is shown.

## What I Learned:

- Hidden networks don't come back as empty names but come back as a bunch of null bytes which look blank when it's printed. It took me some debugging to figure it out and strip null characters.
- Learned the basics of working with a micro-controller for the first time, as well as getting comfortable with MicroPython.

## Expected Outcome:

**scanning for nearby networks and showing name, signal, and security type**

<img width="660" height="145" alt="image" src="https://github.com/user-attachments/assets/14ea3807-29ff-46aa-b110-884b29b89791" />

## How To Run:

1. Flash MicroPython onto a Raspberry Pi Pico 2 W using Thonny.

2. Open network_scanner.py in Thonny and save it to the Pico.

3. Run the script.
