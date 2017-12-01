#!/usr/bin/env python

from __future__ import print_function
from virus_total_apis import PublicApi as VirusTotalPublicApi
import json
import sys
import time

API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'

virustotal = VirusTotalPublicApi(API_KEY)


f = open(sys.argv[1])
lines = f.readlines()

for line in lines:
    time.sleep(15)
    response = virustotal.get_file_report(line)
    # Convert json to dictionary:
    json_data = json.loads(json.dumps(response))
    if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:
        print(json_data['results']['md5'],
            "|",
            json_data['results']['scans']['Fortinet']['result'],
            "|",
            json_data['results']['positives'],
            "|",
            json_data['results']['scan_date'],
            "|")
    elif json_data['results']['response_code'] == 1 and \
         'Fortinet' not in json_data['results']['scans']:
        print(line, "|", "hash is not known to Fortinet", "|")
    else:
        print(line, "|", "hash is not in virustotal database", "|")

f.close()
