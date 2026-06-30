# Layer 2 ARP Network Security Lab

## Overview

This repository contains a set of Python scripts built using **Scapy** to study and understand **ARP (Address Resolution Protocol)** behavior in a controlled, isolated lab environment.

The goal of this project is to gain hands-on experience with Layer 2 networking concepts, including how devices resolve IP-to-MAC mappings, how ARP tables behave under changing network conditions, and how those behaviors can be observed and analyzed from a defensive security perspective.

All testing is performed in isolated virtual machines or personal lab hardware only.

---

## Learning Objectives

This lab was designed to explore:

- ARP protocol mechanics (request/reply behavior)
- IP-to-MAC address resolution
- Ethernet frame structure
- Layer 2 network trust assumptions
- ARP cache behavior in hosts
- Switch MAC learning behavior (CAM table concepts)
- Network anomaly detection fundamentals
- Packet crafting and inspection using Scapy

---

## Lab Environment

- Kali Linux (VM / Raspberry Pi)
- Ubuntu Linux (VM)
- Python 3
- Scapy
- Wireshark (packet inspection)
- tcpdump (CLI packet capture)

---

## Scripts

### 1. ARP Detector (arpDetector.py)

A monitoring tool designed to observe changes in IP-to-MAC address mappings.

**Purpose:**
- Detect potential ARP inconsistencies in a network
- Observe ARP cache changes over time
- Reinforce understanding of how ARP tables update dynamically

**Key Concepts:**
- ARP caching behavior
- Network anomaly detection
- IP/MAC mapping validation

---

### 2. ARP Communication Simulator (ARP Behavior Study Script) (arpSpoof.py)

A Scapy-based script used to study how ARP responses influence host ARP tables in a controlled environment.

**Purpose:**
- Understand how ARP replies are processed by network hosts
- Observe how ARP tables can be influenced in a lab setting
- Study the risks of trusting unauthenticated ARP responses

**Key Concepts:**
- ARP request/reply structure
- Layer 2 trust model
- Packet crafting with Scapy
- Network behavior observation

---

### 3. Layer 2 Traffic Generation / MAC Behavior Simulator (MACflood.py)

A Python script used to generate synthetic Layer 2 traffic to observe how network devices handle MAC address learning behavior.

**Purpose:**
- Study how switches learn and update MAC address tables
- Observe network behavior under high variability of source MAC addresses
- Understand CAM table limitations and switching behavior

**Key Concepts:**
- Ethernet MAC addressing
- Switch CAM table behavior
- Frame forwarding logic
- Network resource constraints

---

## Key Takeaways

This lab reinforces practical understanding of:

- How ARP enables communication in local networks
- Why ARP lacks authentication and must be monitored in enterprise environments
- How switches and hosts maintain address resolution tables
- How network anomalies can be detected through observation
- The importance of segmentation, monitoring, and access controls in enterprise systems

---

## Security & Ethical Notice

This repository is intended strictly for **educational and research purposes** within isolated environments under the user's control.

No scripts are intended for use on networks or systems without explicit authorization.

---

## Future Improvements

- Add ARP cache monitoring dashboard (Python or logging-based)
- Implement detection alerts for ARP table changes
- Expand analysis using Wireshark packet captures
- Extend into broader Layer 2 / Layer 3 network security lab
- Document defensive mitigations (port security, DHCP snooping, Dynamic ARP Inspection)

---

## Author

**Nathaniel Rocha-Torres**  
Data & Computer Science Student | IT Analyst  
Focused on cybersecurity, networking, and enterprise IT systems  
