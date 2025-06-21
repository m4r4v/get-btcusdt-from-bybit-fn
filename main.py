"""
Simple Bybit BTCUSDT Price Fetcher

This script uses the pybit SDK to fetch the latest BTCUSDT price from Bybit's Unified Trading API.
"""

import json
import logging
from datetime import datetime
from pybit.unified_trading import HTTP

# Configure basic logging
# Set logging level based on whether we're in a cloud function or running locally
if __name__ == "__main__":
    # When running as a script, disable logging to only show JSON output
    logging.basicConfig(level=logging.CRITICAL)
else:
    # When imported as a module (e.g., in cloud function), enable normal logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
logger = logging.getLogger(__name__)

def get_btcusdt_price():
    """
    Fetch the latest BTCUSDT price from Bybit using the pybit SDK.
    
    Returns:
        dict: A dictionary containing the price information
    """
    try:
        # Log the start of the function
        logger.info("Starting to fetch BTCUSDT price from Bybit")
        
        # Initialize the HTTP client for Unified Trading API
        # No API key/secret needed for public endpoints
        client = HTTP(testnet=False)
        
        # Fetch the ticker information for BTCUSDT
        # Using the Unified Trading API's market.ticker endpoint
        response = client.get_tickers(
            category="spot",  # Use spot category
            symbol="BTCUSDT"  # The trading pair we want
        )
        
        # Check if the response is successful
        if response["retCode"] == 0 and "result" in response and "list" in response["result"]:
            # Extract the ticker data
            ticker_data = response["result"]["list"][0]
            latest_price = float(ticker_data.get("lastPrice", 0))
            
            # Log the successful price fetch
            logger.info(f"Successfully fetched BTCUSDT price: {latest_price}")
            
            # Prepare the result
            result = {
                "success": True,
                "price": latest_price,
                "timestamp": datetime.now().isoformat(),
                "symbol": "BTCUSDT"
            }
            
            return result
        else:
            # Log warning if the response format is unexpected
            logger.warning(f"Unexpected response format: {response}")
            
            return {
                "success": False,
                "error": "Unexpected response format",
                "timestamp": datetime.now().isoformat(),
                "symbol": "BTCUSDT"
            }
            
    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"Error fetching BTCUSDT price: {str(e)}")
        
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat(),
            "symbol": "BTCUSDT"
        }

def main():
    """
    Main function to run the script.
    """
    # Get the latest BTCUSDT price
    result = get_btcusdt_price()
    
    # Print the result as JSON
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
