# DCN420-SDN-Controller-Mock-Scripts
Simulated SDN controller scripting using Python and REST API mockups. Includes ticket handling, inventory queries, flow analysis, and network configuration updates. Completed for DCN420 at Seneca Polytechnic.
# SDN Controller Mock Scripting – DCN420 Term Project (Part 3)

**Course:** DCN420 – Software Defined Networks  
**Date:** Jan - April 2025  
**Institution:** Seneca Polytechnic  
**Team Members:** Dhanak, Ogundipe, Odutayo

---

## 🧠 Overview
As part of a term project for DCN420, our group was responsible for Part 3: scripting controller functionality via REST APIs. Due to limitations with Packet Tracer, which doesn't support REST API interaction, we implemented **mock Python scripts** to simulate expected controller tasks.

Each script reflects real-world SDN controller logic: from ticket creation to flow analysis and network updates — all via simulated REST API requests and responses.

---

## 🛠️ Simulated Features

| Script | Purpose |
|--------|---------|
| `1. Ticket_handeling.py` | Creates, lists, and updates mock tickets using a fake API |
| `2. Inventory_management.py` | Retrieves mock device inventory from JSONPlaceholder |
| `3. Flow_analysis.py` | Simulates packet flow tracing across hops |
| `4. Device_host_config.py` | Emulates hostname config changes on mock devices |
| `5. Update_network-wide_settings.py` | Mimics network-wide config push via pseudo-API |

---

## 🧪 Tools & Techniques
- Python 3.x  
- REST API emulation using `jsonplaceholder.typicode.com`  
- Modular script structure with simulated output  
- Presentation with flow diagrams and example logs

---

## 📎 Files Included
- `*.py`: All 5 mock scripts used for the controller simulation  
- `Dhanak_Ogundipe_OdutayoProject.pdf`: Final group report  
- `Dhanak_Ogundipe_OdutayoPresentation.pptx`: Project presentation slides

---

## 🧠 Skills Demonstrated
- Python scripting  
- REST API structure and emulation  
- SDN controller logic and abstraction  
- Presentation and technical documentation

---

## ✅ Project Status
- ✔️ All mock scripts functional and documented  
- ✔️ Presentation delivered and report submitted  

⚠️ Project Context & Constraints
This scripting project was part of a larger, multi-group assignment in DCN420, where different teams were responsible for interconnected components (e.g., firewall configuration, routing setup, SDN scripting). Our team was assigned Part 3: simulating SDN controller tasks using REST APIs.

However, due to a lack of cross-team communication, we were unable to obtain the necessary IP addresses, configurations, or outputs from the other groups. This made it infeasible to fully integrate and test live REST API interactions.

To ensure timely and complete delivery, we implemented mock scripts that simulate the controller's logic and responses using tools like jsonplaceholder.typicode.com. While the project operates in a simulated environment, it accurately reflects how SDN controllers handle tasks such as ticketing, inventory queries, and flow analysis.
