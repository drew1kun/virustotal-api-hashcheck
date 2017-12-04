#!/usr/bin/env python


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
