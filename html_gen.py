#!/usr/bin/env python

contents_start = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Virustotal Results Page</title>
<link rel="icon"
      type="image/png"
      href="http://localhost:8000/favicon.png">
</head>
<body>
<center>
<h4>Hash analysis results from Virustotal.com</h4>
"""
contents_end = """
</center>
</body>
</html>
 """


def str_to_file(text, filename):
    # Write a file with the given name and the given text
    output = open(filename, "w")
    output.write(text)
    output.close()


def browse_local(webpage, filename):
    # Start your webbrowser on a local file containing the text
    # with given filename
    import webbrowser
    import os.path
    str_to_file(webpage, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))  # for Mac
