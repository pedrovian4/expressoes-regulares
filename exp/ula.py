import exp

def indetifier(exps:list): 
    language=set()
    for  exp in exps: 
        if '*' == exp[-1] or '^' == exp [-1]:
            language.add(exp[0:-1])
        else: 
            language.add(exp)
        for index,char in enumerate(exp): 
            if char == '^':
                for plus_l in over_plus(exp[index-1]): 
                    language.add(exp[0:index-1]+plus_l)
            if char == '*':
                for star_l in star(exp[index-1]): 
                    if star_l =='':
                        star_l = '\u03BB'	
                    language.add(exp[0:index-1]+star_l)
    return language
                 
                 
                 
                    
                    
def over_plus(char): 
    exp=[]
    for i in range(1,4):
        exp=[*exp, char*i]  
    return exp
                
        
    

def star(char):
    exp=[]
    for i in range(5):
        exp=[*exp, char*i]  
    return exp