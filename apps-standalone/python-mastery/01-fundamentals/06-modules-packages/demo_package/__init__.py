"""
Package initialization file.
Can contain package-level variables and imports.
"""

package_variable = "This is a package-level variable"

# Import key functionality to make available at package level
from .subpackage import subpackage_function
from .module_in_package import *
