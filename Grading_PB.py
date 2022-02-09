def GRADING(test,div2,mod,sqr,plus2,pwr,ex31,doub,mult,cube,ex33,ex34,ex35,ex36):
    grades={"test":False, "Operators":False,"Functions":False,
            "ex31":False,"ex32":False,"ex33":False,"ex34":False,"ex35":False,"ex36":False,"ex37":"CHECK CODE ABOVE"}
    try:
        if(test=="I am loving this class"): grades["test"]=True
    except: grades["test"]=False
    try:
        if(div2 ==2 and mod==1 and sqr==6561 and pwr==512.0): grades["Operators"]=True
    except: grades["Operators"]=False
    try:
        if(plus2(20,34)==None and plus2(40,30)==None): grades["Functions"]=True
    except: grades["Functions"]=False
    try:
        if(ex31("1**2&3|4")=="1^2and3or4" and ex31("**&|")=="^andor"): grades["ex31"]=True
    except: grades["ex31"]=False
    try:
        if(ex32==20000 and  doub(mult(cubes(2)))==160): grades["ex32"]=True
    except: grades["ex32"]=False
    try:
        if(ex33(10)==21916.681339054318 and  ex33(2)==7.38167565355452 ): grades["ex33"]=True
    except: grades["ex33"]=False
    try:
        if(ex34([1,2,3])==[1,3] and  ex34([1,4,5,6])==[1,6] ): grades["ex34"]=True
    except: grades["ex34"]=False
    try:
        if(ex35(False, False)==True and ex35(True, False)==False and ex35(False, True)==True and ex35(True, True)==True ): grades["ex35"]=True
    except: grades["ex35"]=False
    try:
        if(ex36([2,3,4,6,3,3,6,3],[4,6,8,4,2])==2.0 and  ex36([2,3,4,6,3,3],[4,4,2])==1.5 ): grades["ex36"]=True
    except: grades["ex36"]=False
    for x in grades:
        print (x,':',grades[x])