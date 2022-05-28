import exp


def check_p(exp): 
    if '(' in exp:
        return True 
    else: 
        return False

def slicer(exp):
    if check_p(exp): 
        pass
    else: 
        return exp.split('+')
