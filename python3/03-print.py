# Strings:
s1 = 'Hello'
s2 = 'World'
s3 = 'Hi'
print('['+s1+s2+']') # HelloWorld
print('[{:20}]'.format(s1+s2))   # [HelloWorld          ]
print('[{:<20}]'.format(s1+s2))  # [HelloWorld          ]
print('[{:>20}]'.format(s1+s2))  # [          HelloWorld]
print('[{:^20}]'.format(s1+s2))  # [     HelloWorld     ]
print('[{:=^20}]'.format(s1+s2)) # [=====HelloWorld=====]
print(s3*3) # HiHiHi
print('HiHi',end='') # HiHiHaHa
print('HaHa')

print('HiHi',end=' >> ')  # HiHi >> Ha
print('Ha\nHa')           # Ha
