def GRADING(m_train, m_test,train_set_x_flatten,sigmoid,initialize_with_zeros,propagate,params,predict,d):


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
        if(round(sigmoid(np.array([0,2,3]))[2],2)==round(0.9525741268224334,2)): grades["sigmoid"]=True
    except: grades["sigmoid"]=False
    try:
        if(initialize_with_zeros(3)[0].shape[0]==3): grades["initialize"]=True
    except: grades["initialize"]=False
    try:
        if(round(propagate(np.array([[1.],[2.]]) , 2, np.array([[1.,2.,-1.],[3.,4.,-3.2]]).T, np.array([0,0,1]).reshape((-1,1)))[1],2)==round(8.801545319394334,2)): grades["propagate"]=True
    except: grades["propagate"]=False
    try:
        if(round(params['b'],2)==round(1.9253598300845747,2)): grades["Batch_GD"]=True
    except: grades["Batch_GD"]=False
    try:
        if(predict(np.array([[0.1124579],[0.23106775]]), -0.5,np.array([[1.,-1.1,-3.2],[1.2,2.,0.1]]).T)[0,0]==0): grades["predict"]=True
    except: grades["predict"]=False
    try:
        if(round(d['costs'][3],2)==round(0.37600686694802077,2)): grades["model"]=True
    except: grades["model"]=False

    for x in grades:
        print (x,':',grades[x])