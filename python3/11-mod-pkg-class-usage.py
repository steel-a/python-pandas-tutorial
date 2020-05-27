# Import module AS
import _my_module as mm
print(mm.double(2), mm.triple(2))

# Import packages and modules
import my_package as mpk
import my_package.numbers as mnum
import my_package.texts as mtxt
mpk.rootPackageFunction()
print(mnum.double(2))
mtxt.showLine()
mpk.texts.showLine()

# Import package
import my_package
print(my_package.numbers.triple(2))

###########################
#      Classes usage      #
###########################
import _my_class as mc
cl = mc.MyClass()
cl2 = mc.MyClass(2)
print('Class Double:',cl.double(),cl2.double())

# Import using from ... import
from my_package.my_class import MyClass
clpkg = MyClass()
clpkg2 = MyClass(2)
print('Class Triple:', clpkg.triple(), clpkg2.triple())
