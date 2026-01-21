import ast


messy = "def hello(x,y):return x+y"

tree = ast.parse(messy)
print(ast.unparse(tree))

# Fixed spacing, indentation
# AST only fixes Format,not LOGIC
