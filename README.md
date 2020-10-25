# Python imports

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
