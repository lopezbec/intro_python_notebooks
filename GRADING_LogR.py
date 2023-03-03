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
        if(round(cost,3)==round(0.2183301938265977,3)): grades["cost"]=True
    except: grades["cost"]=False
    try:
        if(round(grad[1],3)==round(2.5662341155107558,3)): grades["grad"]=True
    except: grades["grad"]=False

    try:
        if(round(theta_GD[2],3)==round(3.7260375718483822,3)): grades["theta_GD"]=True
    except: grades["theta_GD"]=False

    try:
        if(round(cost_GD,3)==round(2.13484831,3)): grades["cost_GD"]=True
    except: grades["cost_GD"]=False

    try:
        if(round(prob_new_student[0,0],3)==round(0.7762466784809318,3)): grades["predict"]=True
    except: grades["predict"]=False

    try:
        if(round(cost_Reg[0],3)==round(2.02044154,3)): grades["cost_Reg"]=True
    except: grades["cost_Reg"]=False

    try:
        if(round(grad_Reg[4],3)==round(0.015914488662613836,3)): grades["grad_Reg"]=True
    except: grades["grad_Reg"]=False


    for x in grades:
        print (x,':',grades[x])
