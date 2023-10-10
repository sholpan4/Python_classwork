import re

# ^ - string start 
# $ - end of the str

pattern = r'(?P<month>[A-Za-z]+) (\d+) *$'
text = 'Oct 10, Sep 3, Arp 4'
matched = re.search(pattern, text)
if matched:
    print("Group 0", matched.group(0))
    print("Group 1", matched.group('month'))
    print("Group 2", matched.group(2))