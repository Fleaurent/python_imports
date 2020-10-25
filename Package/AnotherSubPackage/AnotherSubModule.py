# Intrapackage Reference
# a) absolute import from Package (prefer!)
from Package.SubPackage import SubModule

# b) relative import from current submodule
from ..SubPackage import SubModule


print("initialized: ", __name__)  # Package.AnotherSubPackage.AnotherSubModule


def anotherSubModuleMethod():
    print("anotherSubModuleMethod()")
    SubModule.subModuleMethod()
