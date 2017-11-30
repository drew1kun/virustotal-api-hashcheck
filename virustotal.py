#!/usr/bin/env python

from __future__ import print_function
import json
from virus_total_apis import PublicApi as VirusTotalPublicApi

# import time

API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'

virustotal = VirusTotalPublicApi(API_KEY)


with open("sample_hash_input.txt", "r") as f:
    lines = f.read().splitlines()

response = virustotal.get_file_report(lines[0])

json_f = open("json_dump.txt", "w")
json_f.write(json.dumps(response, sort_keys=False, indent=4))
json_f.close()

# print(json.dumps(response, sort_keys=False, indent=4))
# print(json.loads(response)[0])

# for line in lines:
#    # time.sleep(15)
#    # response = virustotal.get_file_report(line)
#    # print(json.dumps(response, sort_keys=False, indent=2))
