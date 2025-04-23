"""
Device and Host Configuration Retrieval (Mock for Replit)
Simulates fetching configs for devices and connected hosts.
"""

# This mock script uses sample data for both devices and hosts.
# It's useful for testing or learning without using real hardware.

def get_device_configurations():
    # Simulated device data using a list of dictionaries
    devices = [
        {
            "hostname": "SW1",  # Name of the switch
            "model": "2960",    # Model number
            "running_config": "interface vlan1\nip address 192.168.1.1 255.255.255.0"  # Simulated config
        },
        {
            "hostname": "R1",  # Name of the router
            "model": "4321",   # Model number
            "running_config": "interface g0/0\nip address 10.0.0.1 255.255.255.0"  # Simulated config
        }
    ]
    
    # Display each device's configuration
    print("Device Configurations:")
    for config in devices:
        print(f"Hostname: {config['hostname']}")  # Print hostname
        print(f"Model: {config['model']}")        # Print model
        print(f"Running Config:\n{config['running_config']}")  # Print config
        print("-----")  # Separator line

def get_host_details():
    # Simulated host data using a list of dictionaries
    hosts = [
        {
            "ip": "192.168.1.10",              # Host IP address
            "mac": "AA:BB:CC:DD:EE:01",        # Host MAC address
            "connected_device": "SW1"          # Device the host is connected to
        },
        {
            "ip": "10.0.0.5",                  # Host IP address
            "mac": "AA:BB:CC:DD:EE:02",        # Host MAC address
            "connected_device": "R1"           # Device the host is connected to
        }
    ]
    
    # Display each host's information
    print("Connected Hosts:")
    for host in hosts:
        print(f"IP: {host['ip']}")                  # Print IP address
        print(f"MAC: {host['mac']}")                # Print MAC address
        print(f"Connected To: {host['connected_device']}")  # Show which device it's connected to
        print("-----")  # Separator line

# This block runs when the script is executed directly
if __name__ == "__main__":
    get_device_configurations()  # Call the function to print device info
    print("\n")  # Add spacing between outputs
    get_host_details()  # Call the function to print host info
