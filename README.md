Unique Private Subnet Generator

This Python script generates random /24 private subnets and keeps a persistent record of them to ensure you never use the same network twice. It is a simple, lightweight solution for network administrators and developers who need to quickly assign non-overlapping local networks without the headache of tracking them manually.
Features

    Randomized Selection: Automatically picks a random /24 subnet from standard private IPv4 ranges (Class A, Class B, or Class C).

    Collision Prevention: Saves every generated subnet to a local JSON file (used_networks.json).

    Automatic Retries: If the script generates a subnet that is already in your ledger, it silently skips the duplicate and rolls again until it finds a completely unique one.

    Zero External Dependencies: Built entirely with standard Python libraries (random, ipaddress, json, os). No pip install required!

How It Works

    The script randomly chooses a private IP block:

        10.0.0.0/8

        172.16.0.0/12

        192.168.0.0/16

    It generates a valid /24 CIDR notation within that chosen block.

    It checks used_networks.json to see if that exact CIDR has been issued before.

    If it is unique, it displays the network details to the console and permanently saves it to the memory file.

Usage

Simply run the script from your terminal.
Bash

python generate_subnet.py

Example Output:
Plaintext

--- Unique /24 LAN Generated ---
Network ID:    172.23.145.0/24
Usable Hosts:  254
Saved to:      used_networks.json