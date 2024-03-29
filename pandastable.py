import pandas as pd
import os


table_class = "rwd-table"

html = """<style>
@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";
.rwd-table {
  margin: 1em 0;
	border: 1px;
  min-width: 300px;
}
.rwd-table tr {border-top: 1px solid #ddd; border-bottom: 1px solid #ddd; } 
.rwd-table th {display: none; } 
.rwd-table td {border:1; display: block; } 
.rwd-table td:first-child {padding-top: .5em; } 
.rwd-table td:last-child {padding-bottom: .5em; } 
.rwd-table td:before {content: attr(data-th) ": "; font-weight: bold; width: 6.5em; display: inline-block; } 
@media (min-width: 480px) {
	.rwd-table td:before {display: none; } 
	} .rwd-table th, .rwd-table td {text-align: left; 
	} 
@media (min-width: 480px) {
	.rwd-table th, .rwd-table td {
	display: table-cell; padding: .25em .5em; }
	.rwd-table th:first-child, 
	.rwd-table td:first-child {padding-left: 0; } 
	.rwd-table th:last-child, .rwd-table td:last-child {padding-right: 0; } } 
	h1 {font-weight: normal; letter-spacing: -1px; color: #34495E; } 
	.rwd-table {background: #34495E; color: #fff; border-radius: .4em; overflow: hidden; } 
	.rwd-table tr {border-color: #46637f; } 
	.rwd-table th, 
	.rwd-table td {margin: .5em 1em; } @media (min-width: 480px) {
	.rwd-table th, .rwd-table td {padding: 1em !important; } } 
	.rwd-table th, .rwd-table td:before {color: #dd5; } </style>

<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>"""

html += """
<style>
table, td, th {
  border: 1px solid black;
}

table {
  width: 0;
  border-collapse: collapse;
}
</style>
"""


html += """<style>
table.blueTable {
  border: 1px solid #1C6EA4;
  background-color: #EEEEEE;
  width: 0%;
  text-align: left;
  border-collapse: collapse;
}
table.blueTable td, table.blueTable th {
  border: 1px solid #AAAAAA;
  padding: 3px 2px;
}
table.blueTable tbody td {
  font-size: 13px;
}
table.blueTable tr:nth-child(even) {
  background: #D0E4F5;
}
table.blueTable thead {
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  border-bottom: 2px solid #444444;
}
table.blueTable thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  border-left: 2px solid #D0E4F5;
}
table.blueTable thead th:first-child {
  border-left: none;
}

table.blueTable tfoot {
  font-size: 14px;
  font-weight: bold;
  color: #FFFFFF;
  background: #D0E4F5;
  background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  border-top: 2px solid #444444;
}
table.blueTable tfoot td {
  font-size: 14px;
}
table.blueTable tfoot .links {
  text-align: right;
}
table.blueTable tfoot .links a{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 5px;
}
</style>
"""

# df = pd.read_excel(filename, index=1)
df = pd.read_excel("001.xlsx", engine='openpyxl')
# df.to_html("001.html")
html += "<table class='blueTable'>"
# html += "<table>"
html2 = ""
add = ""

def header():
	"Create the header of the column"
	add = ""
	for d in df:
		add += f"<th>{d}</th>"
	add += "<tr>"
	return add

def content_of_table():
	"This are the tds"
	add = ""
	for i in range(0, len(df)):
		for d in df:
			add += f"<td>{df[d][i]}</td>"
		add += "<tr>"
	return add


def main(html):
	"Builds up the table with the functions made for it"
	html += header()
	html += content_of_table()
	return html

html = main(html)


html += "</table>"
print(html)

with open("file.html", "w") as file:
	file.write(html)
os.startfile("file.html")
