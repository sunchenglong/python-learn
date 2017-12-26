import re
print re.match("\d-\d-\d","1-2-3")
print re.match("\d-\d-\d","1-22-33")
print re.match("\d+-\d+-\d+","2017-19-10")
