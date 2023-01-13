from datetime import date
import requests


def get_epss_score_for_cve(cve: str) -> str:
    """Gets the EPSS score for the provided CVE"""
    cve_url = EPSSAPI.api_url + f"?cve={cve}"
    print(f"Retrieving EPSS score for {cve}: {cve_url}")
    response = requests.get(cve_url)
    if response.status_code != 200:
        print(f"[Error] Response: {response}")
        pass
    else:
        print(f"Response: {response.json()}")
        return response.json().get("data")[0].get("epss")


def get_todays_cves_with_scores() -> list:
    """Gets latest 100 CVEs known as of today (not CVEs reported today only) in descending order by reporting ID"""
    today = str(date.today())
    cve_url = EPSSAPI.api_url + f"?date={today}"
    print(f"Retrieving CVES for {today}: {cve_url}")
    response = requests.get(cve_url)
    if response.status_code != 200:
        print(f"[Error] Response: {response}")
        pass
    else:
        print(f"Response: {response.json()}")
        return response.json().get("data")


def get_most_dangerous_cves() -> list:
    """Gets the 100 CVEs with the highest EPSS scores in descending order"""
    cve_url = EPSSAPI.api_url + f"?percentile-gt=0.95&order=!epss"
    print(f"Retrieving CVEs with EPSS score above 95%: {cve_url}")
    response = requests.get(cve_url)
    if response.status_code != 200:
        print(f"[Error] Response: {response}")
        pass
    else:
        print(f"Response: {response.json()}")
        return response.json().get("data")


class EPSSAPI:
    api_url = "https://api.first.org/data/v1/epss"
    #
    # def call_api(self):


def main():
    # Get CVE from command line or empty means get today's CVES
    cve = input("Enter a CVE identifier (CVE-YYYY-XXXXX) or press ENTER to get today's CVEs: ")
    if cve == "":
        cves = get_todays_cves_with_scores()
        print(f"Retrieved {len(cves)} CVEs for {str(date.today())}")
        # TODO: Sort by EPSS score
        for c in cves:
            print(f"CVE: {c.get('cve')} | EPSS: {c.get('epss')}")
    else:
        # Call the API
        epss_score = get_epss_score_for_cve(cve)
        # Parse the response and display
        print(f"EPSS score for {cve}: {epss_score}")


if __name__ == '__main__':
    main()
