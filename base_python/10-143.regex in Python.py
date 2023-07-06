import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

email = 'jose@tecladocode.com'
parts =email.split('@')

name = parts[0]
domain = parts[1]

print(name)
print(domain)