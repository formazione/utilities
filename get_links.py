# https://github.com/formazione/utilities.git

# get all links in a web page
import re


page = "html_page.html"

pattern = r'<a href="https://pythonprogramming.altervista.org/\w+'

with open(page) as file:
	content = file.read()


matches = re.findall(pattern, content)
print(matches)


