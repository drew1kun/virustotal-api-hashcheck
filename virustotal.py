#!/usr/bin/env python

from __future__ import print_function

# Install virustotal-api from pip before using API:
from virus_total_apis import PublicApi as VirusTotalPublicApi

import json
import sys
import time
import HTML  # Install module before using HTML

import html_gen
import webserver

# Access Virustotal.com API
API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'
virustotal = VirusTotalPublicApi(API_KEY)

# ===== BUILDING HTML TABLE =======
header_row = [
    'hash_value (MD5)',
    'FORTINET detection names',
    'Number of engines detected',
    'Scan Date'
]
table_data = [header_row]

# open the file as first command line argument for hash list analysis
f = open(sys.argv[1])
lines = f.readlines()
for line in lines:
    response = virustotal.get_file_report(line)

    # Convert json to dictionary:
    json_data = json.loads(json.dumps(response))

    if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:
            table_data.append([
                json_data['results']['md5'],
                json_data['results']['scans']['Fortinet']['result'],
                json_data['results']['positives'],
                json_data['results']['scan_date']
                ])
    elif json_data['results']['response_code'] == 1 and \
            'Fortinet' not in json_data['results']['scans']:

            table_data.append([
                json_data['results']['md5'],
                'Not known to Fortinet',
                json_data['results']['positives'],
                json_data['results']['scan_date']
                ])
    else:
            table_data.append([
                line,
                'Hash is not in database'
                '--',
                '--'
                ])
    time.sleep(15)

f.close()

htmltable = HTML.table(table_data)
# ================================

# ====== BUILDING HTML PAGE ======
contents = html_gen.contents_start + htmltable + html_gen.contents_end
html_gen.str_to_file(contents, filename='index.html')
# ===============================

# ======= RUN WEB SERVER ========
webserver.start(port=8000)
# ===============================
