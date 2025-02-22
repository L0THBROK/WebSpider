import http.cookies
import requests
from termcolor import cprint
import time

def extract_cookies(url):
    try:
        response = requests.get(url)
        cookies = http.cookies.SimpleCookie(response.headers.get('Set-Cookie'))
        return cookies
    except requests.exceptions.RequestException as e:
        cprint(f"Error during request: {e}", 'red')
        return None

def extract_metadata(url):
    try:
        response = requests.head(url)
        metadata = response.headers
        return metadata
    except requests.exceptions.RequestException as e:
        cprint(f"Error during request: {e}", 'red')
        return None

if __name__ == "__main__":
    cprint("Welcome by L0THBROK", 'green')

    while True:
        url = input("Enter the website URL (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            break

        cookies = extract_cookies(url)
        if cookies:
            cprint("\nCookies:", 'yellow')
            for cookie, morsel in cookies.items():
                print(f"- {cookie}: {morsel.value}")

        metadata = extract_metadata(url)
        if metadata:
            cprint("\nMetadata:", 'cyan')
            for key, value in metadata.items():
                print(f"- {key}: {value}")

        time.sleep(1)  # Pause for 1 second before the next iteration
