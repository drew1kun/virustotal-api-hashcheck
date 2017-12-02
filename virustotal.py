#!/usr/bin/env python

from __future__ import print_function
from virus_total_apis import PublicApi as VirusTotalPublicApi
import json
import sys
import time
import HTML


API_KEY = '2a11b9bed44b9580bde1033624b38d32fad0c470a8611dc5928ee8d85060745a'

virustotal = VirusTotalPublicApi(API_KEY)


f = open(sys.argv[1])
lines = f.readlines()

for line in lines:
    time.sleep(15)
    response = virustotal.get_file_report(line)
    # Convert json to dictionary:
    json_data = json.loads(json.dumps(response))

#    html = """<html><table border="1">
#    <tr><th>hash_value (MD5)</th>
#    <th>FORTINET detection names </th>
#    <th>Number of engines detected</th>
#    <th>Scan Date</th></tr>"""

    table_data = [
            [
                'hash_value (MD5)',
                'FORTINET detection names',
                'Number of engines detected',
                'Scan Date']
            ]

    if json_data['results']['response_code'] == 1 and \
       'Fortinet' in json_data['results']['scans']:
#            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
#            html += "<tr><td>{}</td>".format(json_data['results']['scans']['Fortinet']['result'])
#            html += "<tr><td>{}</td>".format(json_data['results']['positives'])
#            html += "<tr><td>{}</td>".format(json_data['results']['scan_date'])
            table_data += [
                        json_data['results']['md5'],
                        json_data['results']['scans']['Fortinet']['result'],
                        json_data['results']['positives'],
                        json_data['results']['scan_date']
                    ]
    elif json_data['results']['response_code'] == 1 and \
            'Fortinet' not in json_data['results']['scans']:
#            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
#            html += "<tr><td>{}</td>".format('Not known to Fortinet')
            table_data += [
                        json_data['results']['md5'],
                        'Not known to Fortinet'
                    ]
    else:
#            html += "<tr><td>{}</td>".format(json_data['results']['md5'])
#            html += "<tr><td>{}</td>".format('Hash is not in database')
            table_data += [
                        json_data['results']['md5'],
                        'Hash is not in database'
                    ]

#    html += "</tr>"
#    html += "</table></html>"

f.close()

htmlcode = HTML.table(table_data)
print(htmlcode)

contents = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Virustotal Results Page</title>
</head>
<body>

</body>
</html>
'''


def main():
    browseLocal(contents)


def strToFile(text, filename):
    # Write a file with the given name and the given text
    output = open(filename, "w")
    output.write(text)
    output.close()


def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    # Start your webbrowser on a local file containing the text
    # with given filename
    import webbrowser
    import os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))  # for Mac

main()
