import requests
import sys
from bs4 import BeautifulSoup
from colorama import Fore, Style


def GetURL():
    url = input(Fore.CYAN + "URL> " + Style.RESET_ALL)
    
    try:
        r = requests.get(url)
        response_code = r.status_code
        response_text = r.text  

        soup = BeautifulSoup(response_text, "html.parser") 
        
        print(Fore.GREEN + f"Request Completed! Status Code: {response_code}" + Style.RESET_ALL)
        
        while True:
            task = input(Fore.YELLOW + "task> " + Style.RESET_ALL).strip()

            if task.startswith("get"):
                if task == "get_html":
                    print(Fore.BLUE + response_text + "..." + Style.RESET_ALL) 
                elif task == "get_title":
                    titles = soup.find_all("h1, h2, h3")
                    if titles:
                        for i, title in enumerate(title, 1):
                             print(Fore.MAGENTA + f"[{i}] {title.get_text()}" + Style.RESET_ALL)
                    else:
                       print(Fore.RED + "No  titles found!" + Style.RESET_ALL)

            elif task == "0":
                print(Fore.RED + "Exiting..." + Style.RESET_ALL)
                sys.exit()


            else:
                print(f"Invalid Command => {task}")
                

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


