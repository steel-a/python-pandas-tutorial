n1 = 10
n2 = 0

try:
    print(n1/n2)
except Exception as ex:
    print("Error:", ex)
    # 'pass' to do nothing
else:
    print('No error')
finally:
    print('Finally ends!')
