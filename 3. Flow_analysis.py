"""
Flow Analysis Script (Final Version for Submission)

✅ Purpose:
Simulates a network flow trace from a source host to a destination host,
emulating how SDN controllers or tools like `traceroute` show network paths.

🛠️ Tools Used:
- Python 3.x
- Standard console output (no external libraries needed)

📐 Techniques Used:
- Static data to simulate intermediate devices ("hops")
- Clear separation of logic using a function
- Parameterized source and destination IPs
"""

def trace_flow(src_ip, dst_ip):
    """
    Simulates tracing a network flow between two endpoints.

    Parameters:
    src_ip (str): The IP address of the source host.
    dst_ip (str): The IP address of the destination host.

    Procedure:
    - Define a fixed list of mock devices representing the network path.
    - Each device has a name and the interface used.
    - Print each hop in the sequence to mimic flow analysis output.
    """
    print(f"Tracing flow from {src_ip} to {dst_ip}...\n")  # Show source and destination info
    
    # 🔁 Mock path of hops the packet would take (manually defined)
    mock_hops = [
        {"device": "R1", "interface": "Gig0/0"},        # First hop: router
        {"device": "SW1", "interface": "Gig0/1"},       # Second hop: switch
        {"device": "Firewall", "interface": "Eth0"},    # Third hop: firewall
        {"device": "Server", "interface": "Eth1"},      # Final hop: destination
    ]
    
    # 🖨️ Print each hop device and interface to simulate a traceroute-like output
    for hop in mock_hops:
        print(f"{hop['device']} via {hop['interface']}")

# 🧪 Run the function with example IPs when script is executed
if __name__ == "__main__":
    trace_flow("192.168.1.10", "172.16.0.10")
