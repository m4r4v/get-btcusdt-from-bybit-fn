# Bybit BTCUSDT Price Fetcher

A simple Python script that fetches the latest BTCUSDT price from the Bybit exchange using the official pybit SDK.

## Features

- Uses the official Bybit Python SDK (pybit)
- Fetches the latest BTCUSDT price from Unified Trading API
- Clean JSON output with no logging messages
- No API credentials required (uses public endpoints)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/get-btcusdt-from-bybit-fn.git
cd get-btcusdt-from-bybit-fn
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:

```bash
python main.py
```

This will output only the latest BTCUSDT price in JSON format:

```json
{
  "success": true,
  "price": 101178.0,
  "timestamp": "2025-06-21T19:41:56.478217",
  "symbol": "BTCUSDT"
}
```

## License

MIT
