import sys
from datetime import date

import requests


def get_epss_score_for_cve(cve:str) -> str:
    cve_url = EPSSAPI.api_url + f"?cve={cve}"
    print(f"Retrieving EPSS score for {cve}: {cve_url}")
    response = requests.get(cve_url)
    if response.status_code != 200:
        print(f"[Error] Response: {response}")
        pass
    else:
        print(f"Response: {response.json()}")
        return response.json().get("data")[0].get("epss")


class EPSSAPI:
    api_url = "https://api.first.org/data/v1/epss"
    #
    # def call_api(self):


def main():
    # Get CVE from command line or empty means get today's CVES
    cve = input("Enter a CVE identifier (CVE-YYYY-XXXXX) or press ENTER to get today's CVEs: ")
    if cve == "":
        print("Today's list not yet implemented")
        sys.exit(1)
    else:
        # Call the API
        epss_score = get_epss_score_for_cve(cve)
        # Parse the response and display
        print(f"EPSS score for {cve}: {epss_score}")


if __name__ == '__main__':
    main()

