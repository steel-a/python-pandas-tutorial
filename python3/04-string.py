n1 = "MariaDB"
print('Len:',len(n1)) # 7
print('Count:',n1.count('a')) # 2
print('Count:',n1.count('a',3,10)) # 1
print('Find:',n1.find("ria")) # 2
print('RFind:',n1.rfind("DB")) # 5
print('Find:',n1.find("Paul")) # -1

print('In:','ria' in n1) # True

print(n1[2])       # r
print(n1[2:5])     # ria
print(n1[2:20])    # riaDB
print(n1[1:20:2])  # aiD
print(n1[:2])      # Ma
print(n1[2:])      # riaDB
print(n1[1::2])    # aiD

print(n1.replace('ria','uau')) # MauauDB

n2 = '     test    '
print('Strip:',n2.strip())
print('RStrip:',n2.rstrip())
print('LStrip:',n2.lstrip())

n3 = 'Lorem Ipsum is simply dummy text of the printing'
splited = n3.split()
print(splited[1]) # Ipsum
print('-'.join(splited)) # Lorem-Ipsum-is-simply-dummy-text-of-the-printing

n4 = """Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s"""
