# test.py (On buggy-update branch)

def divide_numbers(a, b):
    """
    Dividing numbers with logging.
    """
    print(f"Dividing ne  {a} by {b}")  # <--- AST Trigger (Warning)
    
    # I removed the check because I don't think b will be 0
    return a / b                   # <--- LLM Trigger (ZeroDivisionError Risk)