import requests

def check_circuit():
    url = "http://localhost:44777"
    print(f"Attempting to access {url}...")
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print(f"Successfully accessed {url}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_circuit()