#!/usr/bin/env python3
"""
Script to fetch openaiapi.json from a URL and save it locally.
"""

import requests
import json
import sys


def fetch_openaiapi_json(url: str, output_file: str = "openaiapi.json") -> bool:
    """
    Fetch openaiapi.json from the specified URL and save it to a local file.

    Args:
        url (str): The URL to fetch the JSON from
        output_file (str): The local filename to save the JSON to

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"Fetching openaiapi.json from: {url}")

        # Make the HTTP request
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Try to parse the response as JSON
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Error: Response is not valid JSON: {e}")
            return False

        # Save the JSON to a local file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Successfully saved openaiapi.json to: {output_file}")
        print(f"File size: {len(response.content)} bytes")

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching from URL: {e}")
        return False
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """Main function to handle command line arguments and execute the fetch."""
    if len(sys.argv) < 2:
        print("Usage: python fetch_openaiapi.py <URL> [output_filename]")
        print("Example: python fetch_openaiapi.py https://api.openai.com/openapi.json")
        print(
            "Example: python fetch_openaiapi.py https://api.openai.com/openapi.json my_openapi.json"
        )
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "openaiapi.json"

    # Validate URL
    if not url.startswith(("http://", "https://")):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)

    # Fetch and save the JSON
    success = fetch_openaiapi_json(url, output_file)

    if success:
        print("Operation completed successfully!")
        sys.exit(0)
    else:
        print("Operation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
