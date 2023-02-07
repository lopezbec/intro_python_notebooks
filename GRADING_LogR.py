def GRADING_LogR(sigmoid,cost,grad,theta_GD,cost_GD,prob_new_student,cost_Reg,grad_Reg):


    grades={"sigmoid":False, 
            "cost":False, "grad":False,
            "theta_GD":False,"cost_GD":False,
            "predict":False,
            "cost_Reg":False,"grad_Reg":False}


    try:
        if( sigmoid(0)==0.5): grades["sigmoid"]=True
    except: grades["sigmoid"]=False
    try:
        if(cost==0.2183301938265977): grades["cost"]=True
    except: grades["cost"]=False
    try:
        if(grad[1]==2.5662341155107558): grades["grad"]=True
    except: grades["grad"]=False

    try:
        if(theta_GD[2]==3.7260375718483822): grades["theta_GD"]=True
    except: grades["theta_GD"]=False

    try:
        if(cost_GD==0.2034977556513879): grades["cost_GD"]=True
    except: grades["cost_GD"]=False

    try:
        if(prob_new_student[0,0]==0.7762466784809318): grades["predict"]=True
    except: grades["predict"]=False

    try:
        if(cost_Reg[0]==2.134848314665857): grades["cost_Reg"]=True
    except: grades["cost_Reg"]=False

    try:
        if(grad_Reg[4]==0.015914488662613836): grades["grad_Reg"]=True
    except: grades["grad_Reg"]=False


    for x in grades:
        print (x,':',grades[x])
