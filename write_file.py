from random import choice
narco = ['heroin', 'opium', 'crack', 'herb',
        'marijuana', 'shroom', 'xanax', 'amphetamines',
        'coke', 'benzos', 'pcp', 'dmt', 'lsd', '']
with open('write.txt', 'a') as file:
    file.write(f'I dont do {choice(narco)}\n')
    file.write(f'I dont do {choice(narco)}\n')
    file.write(f'I dont do {choice(narco)}\n')
    file.write(f'I dont do {choice(narco)}\n')
    file.write(f'I dont do {choice(narco)}\n')
