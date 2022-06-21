with open('pi_million_digits.txt') as pi:
    content = pi.read()
    print(content[:50])
if "1409" in content:
    print('yes')
    print(content.find('14'))
content.replace('\n', '')
print(len(content))

pi_float = float(content.replace(' ', '').replace('\n', ''))
print(f'{pi_float:.100}')
