<<<<<<< HEAD
import ast

def parse_code(code_string):
    """
    Parse Python code into AST.
    Returns success info or syntax error details.
    """
    try:
        tree = ast.parse(code_string)
        return {
            "success": True,
            "tree": tree
        }
    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "type": "SyntaxError",
                "line": e.lineno,
                "message": e.msg,
                "text": e.text.strip() if e.text else ""
            }
        }
=======
import ast

def parse_code(code_string):
    """
    Parse Python code into AST.
    Returns success info or syntax error details.
    """
    try:
        tree = ast.parse(code_string)
        return {
            "success": True,
            "tree": tree
        }
    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "type": "SyntaxError",
                "line": e.lineno,
                "message": e.msg,
                "text": e.text.strip() if e.text else ""
            }
        }
>>>>>>> bc15ce42fab1e1aa4ec9fe1605ff34c3e2c6ae42
