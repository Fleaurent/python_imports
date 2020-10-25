# Python Imports

## 1. import module next to script
```python
import SimpleModule
from SimpleModule import simplefunction
```

## 2. import module from package
```python
import Package
from Package import Module
from Package.Module import moduleMethod
```

## 3. import module from subpackage
```python
from Package import SubPackage
from Package.SubPackage import SubModule
from Package.SubPackage.SubModule import subModuleMethod
```

## 4. import subpackage with intrapackage reference
```python
# a) absolute import from Package (prefered!)
from Package.SubPackage import SubModule

# b) relative import from current submodule
from ..SubPackage import SubModule
```


# Run main.py
```bash
initialized:  SimpleModule
initialized:  Package
initialized:  Package.Module
initialized:  Package.SubPackage
initialized:  Package.SubPackage.SubModule
initialized:  Package.AnotherSubPackage
initialized:  Package.AnotherSubPackage.AnotherSubModule

1. module next to script
simplefunction()
simplefunction()

2. module from package
moduleMethod()
moduleMethod()
moduleMethod()

3. module from subpackage
subModuleMethod()
subModuleMethod()
subModuleMethod()
subModuleMethod()

4. intrapackage reference in submodule
anotherSubModuleMethod()
subModuleMethod()
```