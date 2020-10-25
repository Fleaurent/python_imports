# Intrapackage Reference
# a) absolute import from Package (prefer!)
from Package.SubPackage import SubModule

# b) relative import from current submodule
from ..SubPackage import SubModule


def anotherSubModuleMethod():
    print("anotherSubModuleMethod()")
    SubModule.subModuleMethod()
