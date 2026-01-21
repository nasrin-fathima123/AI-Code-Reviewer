import ast

def clean_code(messy_code: str):
    """
    Cleans and formats Python code using AST.
    """
    try:
        tree = ast.parse(messy_code)
        formatted_code = ast.unparse(tree)
        return {
            "success": True,
            "code": formatted_code
        }
    except SyntaxError:
        return {
            "success": False,
            "code": messy_code
        }
"""
    example for testing
    def calculate(x,y):
    unused_variable = 100
    another_unused= 200
    result = x+y
    return result
"""
