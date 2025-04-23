"""
Network-Wide Settings Update Script (Final Submission Version)

✅ Purpose:
Simulates sending network-wide configuration updates — specifically for NTP and SYSLOG settings —
as would be done through a network controller or SDN API.

🛠️ Tools Used:
- Python 3 (standard interpreter)
- No external libraries needed for simulation

🔧 Techniques Used:
- Function-based approach for modular code
- Parameterized inputs to simulate dynamic configuration
- Printed output to simulate REST API response

📐 Why This Is a Mock:
In a real environment, such updates would be performed by sending
HTTP POST/PUT requests to a network controller (like Cisco DNA Center or an SDN controller).
Since Packet Tracer does not allow this externally, we simulate the API behavior by printing expected actions.
"""

# This mock version only prints what would be sent to a real API
def update_settings(ntp_ip, syslog_ip):
    """
    Simulates pushing NTP and SYSLOG server settings to the network.
    
    Parameters:
    ntp_ip (str): IP address of the NTP (time) server
    syslog_ip (str): IP address of the SYSLOG (logging) server

    Procedure:
    - Accepts two IP addresses (one for NTP, one for SYSLOG)
    - Prints simulated REST API configuration push
    """
    print("Sending NTP and SYSLOG settings to network...")  # Announce start of configuration
    print(f"NTP Server: {ntp_ip}")  # Show simulated NTP server IP
    print(f"SYSLOG Server: {syslog_ip}")  # Show simulated SYSLOG server IP
    print("Status: Success (simulated)")  # Indicate mock success message

# Main execution block
if __name__ == "__main__":
    # Example configuration values to simulate a real update
    update_settings("172.16.10.10", "172.16.20.20")
