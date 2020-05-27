# Strings:
s1 = 'Hello'
s2 = 'World'
s3 = 'Hi'
print('['+s1+s2+']') # HelloWorld
print('[{:20}]'.format(s1+s2))   # [HelloWorld          ]
print('[{:<20}]'.format(s1+s2))  # [HelloWorld          ]
print(f'[{s1+s2:>20}]')  # [          HelloWorld]
print(f'[{s1+s2:^20}]')  # [     HelloWorld     ]
print(f'[{s1+s2:=^20}]') # [=====HelloWorld=====]
print(s3*3) # HiHiHi
print('HiHi',end='') # HiHiHaHa
print('HaHa')

print('HiHi',end=' >> ')  # HiHi >> Ha
print('Ha\nHa')           # Ha


print('\033[31mHello!\033[m')
# Style: 0, 1, 4, 7
# Text color: 30-37
# Back color: 40-47