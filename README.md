# Proof of Concept for FIRST.org EPSS Score API

## Description

[FIRST](https://first.org/) (Forum of Internet Response and Security Teams) provides a predictive scoring system for
CVEs called the [Exploit Prediction Scoring System](https://www.first.org/epss/user-guide). This threat intelligence
value allows users to prioritize CVE remediation with an evidence-based observation model predicting the likelihood of
CVE exploit within the next 30 days.

### Probabilities and Percentiles

The EPSS consists of two components:
 * **probability score** - the likelihood that this CVE is exploited within the next 30 days;
_global raw score_
 * **percentile** - in what percentile among all known CVEs does this probability reside; _local
relative score_

See [EPSS - Probability, Percentile, and Binning](https://www.first.org/epss/articles/prob_percentile_bins) for more
information. 

## Usage

The tool is run as `$ python epss.py` and provides a prompt:

`Enter a CVE identifier (CVE-YYYY-XXXXX) or press ENTER to get today's CVEs: `

### Specific CVE

If the user provides a CVE identifier (e.g. `CVE-2020-9491`), the script invokes the FIRST EPSS API (`https://api.first.org/data/v1/epss`) via GET HTTP
request and displays the 

```text
Retrieving EPSS score for CVE-2020-9491: https://api.first.org/data/v1/epss?cve=CVE-2020-9491
Response: {'status': 'OK', 'status-code': 200, 'version': '1.0', 'access': 'public', 'total': 1, 'offset': 0, 'limit': 100, 'data': [{'cve': 'CVE-2020-9491', 'epss': '0.009540000', 'percentile': '0.356180000', 'date': '2023-01-12'}]}
EPSS score for CVE-2020-9491: 0.954%
```

### Today's CVEs

If the user does not provide any input, the script invokes the FIRST EPSS API (`https://api.first.org/data/v1/epss`) via GET HTTP
request and displays the 100 most recently published CVEs as of today with the accompanying EPSS probability and percentile scores. 

```text
Retrieving CVES for 2023-01-12: https://api.first.org/data/v1/epss?date=2023-01-12
Response: {'status': 'OK', 'status-code': 200, 'version': '1.0', 'access': 'public', 'total': 192993, 'offset': 0, 'limit': 100, 'data': [{'cve': 'CVE-2023-23455', 'epss': '0.008900000', 'percentile': '0.296850000', 'date': '2023-01-12'}, {'cve': 'CVE-2023-23454', 'epss': '0.008900000', 'percentile': '0.296850000', 'date': '2023-01-12'}, ...]}
Retrieved 100 CVEs for 2023-01-12
...
CVE: CVE-2023-22622 | EPSS: 2.76% | Percentile:  82%
CVE: CVE-2023-22551 | EPSS: 1.05% | Percentile:  51%
CVE: CVE-2023-22492 | EPSS: 0.89% | Percentile:  30%
CVE: CVE-2023-22487 | EPSS: 9.03% | Percentile:  94%
CVE: CVE-2023-22479 | EPSS: 0.89% | Percentile:  27%
CVE: CVE-2023-22477 | EPSS: 0.95% | Percentile:  36%
...
```

### Future Enhancements

* There is also code which retrieves the 100 "most dangerous" CVES (i.e. EPSS percentile > 95%, ordered descending) but it is not invocable from the current prompt 
* Adding additional context from the NIST NVD database
* Searching for CVEs by CPE or CVSS v3.1 metrics vector