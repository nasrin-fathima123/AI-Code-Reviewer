import ast

class ErrorFinder(ast.NodeVisitor):
    def __init__(self):
        self.var_created = set()   # Box 1: created variables
        self.var_used = set()      # Box 2: used variables
        self.given_import = set()  # Box 3: given imports
        self.used_import = set()   # Box 4: used imports

    def visit_Assign(self, node):
        # when we see: x = 5 or import requests or any other unused import
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.var_created.add(target.id)
        self.generic_visit(node)

    def visit_Import(self, node):
        # Capture imported modules: import requests
        for alias in node.names:
            self.given_import.add(alias.name.split('.')[0])
        self.generic_visit(node)

    def visit_Name(self, node):
        # When we see: print(x)
        if isinstance(node.ctx, ast.Load):
            self.var_used.add(node.id)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # Capture imports: from requests import get
        if node.module:
            self.given_import.add(node.module.split('.')[0])
        self.generic_visit(node)

    def visit_Attribute(self, node):
        # Capture attribute access: requests.get() -> requests used
        if isinstance(node.value, ast.Name):
            self.used_import.add(node.value.id)
        self.generic_visit(node)


def detect_errors(code):
    """
    Find unused variables and unused imports
    """
    tree = ast.parse(code)
    finder = ErrorFinder()
    finder.visit(tree)

    unused_var = finder.var_created - finder.var_used
    unused_imports = finder.given_import - finder.used_import

    return [
        {
            "unused_variables": list(unused_var),
            "unused_imports": list(unused_imports)
        }
    ]
