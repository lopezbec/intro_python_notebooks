def GRADING_SoftM(accuracy_score_1, accuracy_score_l2,accuracy_score_estop,accuracy_score_final):


    grades={"accuracy_score_1":False, 
            "accuracy_score_l2":False, 
            "accuracy_score_estop":False,
            "accuracy_score_final":False}


    try:
        if(round(accuracy_score_1,2)==0.97): grades["accuracy_score_1"]=True
    except: grades["accuracy_score_1"]=False

    try:
        if(accuracy_score_l2==1.0 ): grades["accuracy_score_l2"]=True
    except: grades["accuracy_score_l2"]=False


    try:
        if(accuracy_score_estop==1.0): grades["accuracy_score_estop"]=True
    except: grades["accuracy_score_estop"]=False
    
    try:
        if(accuracy_score_final==0.9333333333333333): grades["accuracy_score_final"]=True
    except: grades["accuracy_score_final"]=False



    for x in grades:
        print (x,':',grades[x])
        
    
