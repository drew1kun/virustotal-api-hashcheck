# README #
This Python script allows to check list of hashes (provided in a form of text file) against the virustotal.com database
using their API

script takes a text file as an argument and returns the info about the hashes in the following form:
```
hash_value (MD5)  | FORTINET detection names | Number of engines detected | Scan Date |
```

NOTE:
Virustotal sets the quota - 4 API Queries per 1 minute, so the script is using 15 sec delay for each hash listed in
the file

## Requirements ##
Script was tested on MacOS 10.11.6

## Dependencies ##
Install python with homebrew (pip will be installed automatically in this case):
    `brew install python`

Install virustotal-api using pip:
    `pip install virustotal-api`

## Usage ##
Running script example:
    `python ./virustotal.py sample_hash_input.txt`

## Other Info ##
I had 48 hours for this task.
I had to go to work at that time so I had only 3 hours per day during 48 hour timerange.
Technically speaking, this is the result of 6 hours work starting from scratch.
If you find any issues with the script, please feel free to contact me at any time.

## Contacts ##
Andrew Shagayev <drewshg@gmail.com>
