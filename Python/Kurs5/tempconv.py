#!/usr/bin/python
import cgi, os, sys
sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
sys.stdout.write("<h2>Fahrenheit coverted to Celsius</h2>")

form = cgi.FieldStorage()
fahr = float(form["temp"].value)
celsius = 5.0 * (fahr - 32.0) / 9.0
sys.stdout.write("%.1f Fahrehite equals %.1f Celsius" % (fahr, celsius))
sys.stdout.write("</body></html>")
