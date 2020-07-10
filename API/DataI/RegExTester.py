import re

pattern = '\d{2}/\d{2}/\d{4}'

str = '22/12/2000'

result = re.search(pattern, str)

if result != None:
    print('good')

