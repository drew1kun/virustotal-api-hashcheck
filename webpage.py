#!/usr/bin/env python

contents = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Hello World Webpage</title>
</head>
<body>
Hello, World!
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
