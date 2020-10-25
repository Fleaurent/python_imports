# 1. import module next to script
import SimpleModule
from SimpleModule import simplefunction

# 2. import module from package
import Package
from Package import Module
from Package.Module import moduleMethod

# 3. import module from subpackage
from Package import SubPackage
from Package.SubPackage import SubModule
from Package.SubPackage.SubModule import subModuleMethod

# 4. import subpackage with intrapackage reference
from Package.AnotherSubPackage.AnotherSubModule import anotherSubModuleMethod

if __name__ == "__main__":
    print("\n1. module next to script")
    SimpleModule.simplefunction()
    simplefunction()

    print("\n2. module from package")
    Package.Module.moduleMethod()
    Module.moduleMethod()
    moduleMethod()

    print("\n3. module from subpackage")
    Package.SubPackage.SubModule.subModuleMethod()
    SubPackage.SubModule.subModuleMethod()
    SubModule.subModuleMethod()
    subModuleMethod()

    print("\n4. intrapackage reference in submodule")
    anotherSubModuleMethod()
