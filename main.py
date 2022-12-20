
    #'''create a babylonian function.
    
    #Args:
        #S (int): number
        #d (int): numnber
        
    #Returns:
        #float: result
    #'''
def main(S, d):
    a = (S - d ** 2 ) / (2 * d)
    b = a + d
    x = b - a ** 2 / (2 * b)
    return x
S = 10
d = 6
print(main(S,d))