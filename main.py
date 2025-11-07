import requests
from bs4 import BeautifulSoup
# import selenium

mygju_username =  "REDACTED"
mygju_password = "REDACTED"

mygju_url = "https://mygju.gju.edu.jo/faces/index.xhtml"
mygju_login_post_url = "https://mygju.gju.edu.jo/faces/index.xhtml"

def check_website_status():
    
    try:
        response = requests.get(mygju_url, timeout=5)
        if response.status_code == 200:
            print("Website is working")
            return 200
        
        else:
            return f"Website returned error {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Website is not working ({e})"
    
def mygju_login(username, password):


    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })

    get_resp = session.get(mygju_url)

    soup = BeautifulSoup(get_resp.text, "html.parser")
    viewstate = ""
    
    viewstate_input = soup.find("input", {"name": "javax.faces.ViewState"})
    if viewstate_input:

        viewstate = viewstate_input["value"]

    data = {
        "j_idt15": "j_idt15",
        "j_idt15:login_username": username,
        "j_idt15:login_password": password,
        "j_idt15:j_idt25": "j_idt15:j_idt25",
        "j_idt15:j_idt25:j_idt26": "",
        "javax.faces.ViewState": viewstate,

    }

    post_resp = session.post(mygju_login_post_url, data=data)
    return post_resp


def main():
    if check_website_status() == 200:
        respo = mygju_login(mygju_username, mygju_password)

        print("login response status:", respo.status_code)
        # print(respo.text)  
        if "Schedule" in respo.text:
            print("Logged in")
        else:
            print("error")


if __name__ == "__main__":
    main()