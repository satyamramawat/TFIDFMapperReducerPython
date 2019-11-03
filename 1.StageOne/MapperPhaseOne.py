## Author - Satyam Ramawat
## satyamramawat@gmail.com

#!/usr/bin/env python 
from string import punctuation
import sys

for line in sys.stdin:
    line = line.translate(str.maketrans('','',punctuation)).strip('\t')
    line_contents = line.split(" ")
    doc_name = line_contents[0]
    line_contents.remove(doc_name)
    for content in line_contents:
      content = content.rstrip()
      key = content + "," + doc_name
      print(key, 1)
