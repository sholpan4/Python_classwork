import re

pattern = r",\s*"
text = """June 24, 
August 9,\tDec 12"""

result = re.split(pattern, text)
print(result)

pattern = r"[A-Za-z]+ [0-9]{2}"
result_text = re.sub(pattern, "Gleb", text)

print(result_text)

