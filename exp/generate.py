
import exp

from .slicer import slicer
from .ula import  indetifier 
def generate(exp):
    ne= slicer(exp)
    language= indetifier(ne)
    return language
    
    
