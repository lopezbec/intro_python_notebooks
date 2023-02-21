def GRADING_LogRNN(m_train, m_test,train_set_x_flatten,sigmoid_in,initialize_with_zeros,propagate_in,params,predict_in,d):


    grades={"reshaping":False, 
            "sigmoid":False, 
            "initialize":False,
            "propagate":False,
            "Batch_GD":False,
            "predict":False,
            "model":False}


    try:
        if(m_train==209 and m_test==50 and train_set_x_flatten.shape[1]==12288): grades["reshaping"]=True
    except: grades["reshaping"]=False
    try:
        if(round(sigmoid_in,2)==round(0.9525741268224334,2)): grades["sigmoid"]=True
    except: grades["sigmoid"]=False
    try:
        if(initialize_with_zeros(3)[0].shape[0]==3): grades["initialize"]=True
    except: grades["initialize"]=False
    try:
        if(round(propagate_in,2)==round(8.801545319394334,2)): grades["propagate"]=True
    except: grades["propagate"]=False
    try:
        if(round(params['b'],2)==round(1.9253598300845747,2)): grades["Batch_GD"]=True
    except: grades["Batch_GD"]=False
    try:
        if(predict_in==0): grades["predict"]=True
    except: grades["predict"]=False
    try:
        if(round(d['costs'][3],2)==round(0.37600686694802077,2)): grades["model"]=True
    except: grades["model"]=False

    for x in grades:
        print (x,':',grades[x])