#!/usr/bin/env python

from __future__ import print_function
from virus_total_apis import PublicApi as VirusTotalPublicApi
import json
import sys
import time

# import webserver

API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'

virustotal = VirusTotalPublicApi(API_KEY)


f = open(sys.argv[1])
lines = f.readlines()

for line in lines:
    time.sleep(15)
    response = virustotal.get_file_report(line)
    # Convert json to dictionary:
    json_data = json.loads(json.dumps(response))

    html = """<html><table border="1">
    <tr><th>hash_value (MD5)</th><th>FORTINET detection names </th><th>Number of engines detected</th><th>Scan Date</th></tr>"""

    if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:
            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
            html += "<tr><td>{}</td>".format(json_data['results']['scans']['Fortinet']['result'])
            html += "<tr><td>{}</td>".format(json_data['results']['positives'])
            html += "<tr><td>{}</td>".format(json_data['results']['scan_date'])

    elif json_data['results']['response_code'] == 1 and \
            'Fortinet' not in json_data['results']['scans']:
            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
            html += "<tr><td>{}</td>".format('Not known to Fortinet')
    else:
            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
            html += "<tr><td>{}</td>".format('Hash is not in database')

    html += "</tr>"
    html += "</table></html>"

f.close()
