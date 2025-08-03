# SpeedTest Checker

A simple Python script to check your internet connection speed (download, upload, and ping).

## Features
- Measures download speed (Mbps)
- Measures upload speed (Mbps)
- Shows ping latency (ms)
- Automatic server selection
- Command-line interface

## Requirements
- Python 3.6+
- speedtest-cli library

## Installation

1.Clone this repository:
```bash
   git clone https://github.com/muranja/speedtest-checker.git
   cd speedtest-checker
```

2.(Optional but recommended) Create a virtual environment:
```bash
# Windows:
python -m venv venv
venv\Scripts\activate
```

## macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3.Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Make sure you're in the project directory:
```bash
cd speedtest-checker
```
5. Run the speed test:
```bash
python speedtest-checker
```


## Understanding Results
Download Speed: How fast data comes from the internet to your device

Upload Speed: How fast data goes from your device to the internet

Ping: How quickly your device communicates with the internet (lower is better)
