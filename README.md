# Seerstone

Seerstone is a CLI tool for approximate IP geolocation based on network measurements collected from multiple geographic locations.

## How It Works

Seerstone uses multiple Globalping probes located in different cities around the world.

For each probe, the tool performs:

* ICMP ping
* Traceroute

The collected data is used to calculate a simple `measurement` score based on:

* Average RTT
* Packet loss
* Hop count

The probes are then sorted by their measurement score, and the **TOP 3 probes** with the lowest scores are returned as the current estimate.

## Architecture

```text
Target IP
    ↓
Globalping Probes
    ↓
Ping + Traceroute
    ↓
Network Measurements
    ↓
Measurement Score
    ↓
TOP 3 Probes
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/seerstone.git
cd seerstone
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run Seerstone with a target IP address:

```bash
python seerstone.py <TARGET_IP>
```

Example:

```bash
python seerstone.py 2.56.11.26
```

## Example

```text
========================================
             SEERSTONE
========================================

Target: 2.56.11.26
Probes: 12

Starting measurements...

========================================
             TOP 3 PROBES
========================================

1. Frankfurt, DE → measurement = 15.22
2. Amsterdam, NL → measurement = 26.67
3. Prague, CZ → measurement = 28.89
```

In this test, the target IP was located in Frankfurt, and the Frankfurt probe produced the lowest measurement score.

## Limitations

Seerstone is currently an experimental MVP.

Network latency is affected by more than geographic distance. Results can be influenced by:

* ISP routing
* Network peering
* Network congestion
* Packet loss
* ICMP filtering
* Asymmetric routing

Because of this, Seerstone should be considered an **approximate network-based location estimator**, not an exact IP geolocation system.

## Technologies

* Python
* Requests
* Globalping API
* ICMP Ping
* Traceroute


## Future Development

Possible improvements include:

* Dynamic Globalping probe discovery
* Support for a larger number of probes
* Multi-stage localization
* Geographic search areas based on multiple probes
* Additional measurements inside the estimated area
* Improved measurement weighting
* Better handling of packet loss and ICMP filtering
* Final approximate coordinate estimation
