# test.py (On buggy-update branch)

def divide_numbers(a, b):
    """
    Dividing numbers with logging.
    """
    print(f"Dividing hehene  {a} by {b}")  # <--- AST Trigger (Warning)
    
    # I removed the check because I don't think b will be 0
    return 0 / 0                   # <--- LLM Trigger (ZeroDivisionError Risk)