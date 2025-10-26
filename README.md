# Data Checker Project (TCP & UDP)

This repository contains Python client and server code for both TCP and UDP-based even/odd number checking, developed as part of Data Communication Phase 1 coursework.

## Overview

- **TCPClient_datachecker.py**: TCP client, sends numbers and receives even/odd check.
- **TCPServer_datachecker.py**: TCP server, receives numbers and replies even/odd result.
- **UDPClient_datachecker.py**: UDP client, sends numbers and receives even/odd check.
- **UDPServer_datachecker.py**: UDP server, receives numbers and replies even/odd result.

This code demonstrates core socket communication and shows the difference between reliable (TCP) and unreliable (UDP) protocols for educational purposes.

## How to Run

1. Clone this repository:
git clone https://github.com/dipaljoshi18/Datachecker-Project.git
cd Datachecker-Project

2. Open two terminal windows/tabs. In the first, start the server:
For TCP:
python3 TCPServer_datachecker.py
For UDP:
python3 UDPServer_datachecker.py

3. In the second window, run the client:
For TCP:
python3 TCPClient_datachecker.py
For UDP:
python3 UDPClient_datachecker.py

4. Enter numbers as prompted to receive feedback on whether each value is even or odd.

## Requirements

- Python 3.7 or higher (tested on Python 3.13.7 and Kali Linux)
- No external libraries are required

## Wireshark

Wireshark was used to capture and analyze TCP and UDP traffic for educational reflection (screenshots included in project submission).

## License

This project is educational and submitted for coursework.  
You may reuse or adapt the code for learning purposes.

---




