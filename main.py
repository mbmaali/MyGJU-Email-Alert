import requests
# import selenium


mygju_url = "https://mygju.gju.edu.jo/faces/index.xhtml"

def check_website_status():
    # global mygju_url
    try:
        response = requests.get(mygju_url, timeout=5)
        if response.status_code ==200:
            return f"Website is working!"
        else:
            return f"Website returned error {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Website is NOT working  ({e})"
    



print(check_website_status())
