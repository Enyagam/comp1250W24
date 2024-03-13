import re

pattern = "e[\s\.]"
text = "Hello there everyone. I live at 123 Main Street in Toronto, Ontario"

result = re.findall(pattern=pattern, string=text)

for hit in result:
    print(hit)

