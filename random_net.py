import random
import ipaddress
import json
import os

# File where used networks will be stored
MEMORY_FILE = "used_networks.json"

def load_memory():
    """Loads the list of already used subnets from the JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_memory(used_list):
    """Saves the updated list back to the JSON file."""
    with open(MEMORY_FILE, "w") as f:
        json.dump(used_list, f, indent=4)

def generate_random_subnet():
    """Generates a random /24 private subnet."""
    choice = random.choice(['A', 'B', 'C'])
    
    if choice == 'A':
        # 10.x.x.0/24
        cidr = f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.0/24"
    elif choice == 'B':
        # 172.16.x.0/24 - 172.31.x.0/24
        cidr = f"172.{random.randint(16, 31)}.{random.randint(0, 255)}.0/24"
    else:
        # 192.168.x.0/24
        cidr = f"192.168.{random.randint(0, 255)}.0/24"

    return cidr

def get_unique_subnet():
    """Loops until it finds a subnet that hasn't been used yet."""
    used_subnets = load_memory()
    
    while True:
        candidate = generate_random_subnet()
        
        if candidate not in used_subnets:
            # Found a unique one!
            used_subnets.append(candidate)
            save_memory(used_subnets)
            return ipaddress.IPv4Network(candidate)
        else:
            print(f"Skipping duplicate: {candidate}")

# --- Main Execution ---
if __name__ == "__main__":
    try:
        net = get_unique_subnet()
        
        print(f"--- Unique /24 LAN Generated ---")
        print(f"Network ID:    {net}")
        print(f"Usable Hosts:  {net.num_addresses - 2}")
        print(f"Saved to:      {MEMORY_FILE}")
        
    except KeyboardInterrupt:
        print("\nProcess cancelled.")