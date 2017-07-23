import re
match = re.search('pattern', 'Awesome pattern in my string')
if match:
    print(match.group())
text = """Hello, 123.123.123.123
I'm here 456
"""
print(re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', text))
print(text)
