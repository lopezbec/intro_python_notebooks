def GRADING(layer_sizes,initialize_parameters,forward_propagation,compute_cost,
            backward_propagation,update_parameters,nn_model,predict,forward_propagation_test_case,
            compute_cost_test_case,backward_propagation_test_case,update_parameters_test_case,nn_model_test_case,predict_test_case):

    import numpy as np

    grades={"layer_sizes":False, 
            "initialize_parameters":False, 
            "forward_propagation":False,
            "compute_cost":False,
            "backward_propagation": False,
            "update_parameters":False,
            "nn_model":False, 
            "predict":False}
    
    n_0, n_1, n_2 = layer_sizes(np.ones((18,8)), np.ones((18,2)))
    try:
        if(n_0== 8 and n_1==4 and n_2==2): grades["layer_sizes"]=True
    except: grades["layer_sizes"]=False

    parameters = initialize_parameters(n_0, n_1, n_2)
    try:
        if(parameters["W1"].shape[1]==8 and
           parameters["b1"].shape[0]==4 and
           parameters["W2"].shape[1]==4 and
           parameters["b2"].shape[0]==2): grades["initialize_parameters"]=True
    except: grades["initialize_parameters"]=False

    X_assess, parameters = forward_propagation_test_case()
    A2, cache = forward_propagation(X_assess, parameters)
    try:
        if(round(np.mean(cache['Z1']),2)==0.26 and 
        round(np.mean(cache['A1']),2)==0.09 and
        round(np.mean(cache['Z2']),2)==-1.31 and
        round(np.mean(cache['A2']),2)==0.21): grades["forward_propagation"]=True
    except: grades["forward_propagation"]=False

    A2, Y_assess, parameters = compute_cost_test_case()
    try:
        if(round(compute_cost(A2, Y_assess),4)==0.6931): grades["compute_cost"]=True
    except: grades["compute_cost"]=False


    parameters, cache, X_assess, Y_assess = backward_propagation_test_case()
    grads = backward_propagation(parameters, cache, X_assess, Y_assess)

    try:
        if((round(grads["dW1"][0,1],3)==-0.007 and
        round(grads["db1"][1,0],3)==0.002 and
        round(grads["dW2"][0,2],3)==-0.001 and
        round(grads["db2"][0,0],3)==-0.167)): grades["backward_propagation"]=True
    except: grades["backward_propagation"]=False


    parameters, grads = update_parameters_test_case()
    parameters = update_parameters(parameters, grads)

    try:
        if((round(parameters["W1"][3,1],5)==-0.0599 and
    round(parameters["b1"][1,0],6)==1.3e-5 and
    round(parameters["W2"][0,1],4)==-0.0446 and
    round(parameters["b2"][0,0],5)==0.0001)): grades["update_parameters"]=True
    except: grades["update_parameters"]=False

    X_assess, Y_assess = nn_model_test_case()
    parameters = nn_model(X_assess, Y_assess, 4, num_iterations=10000, print_cost=False)

    try:
        if((round(parameters["W1"][2,1],2)==-1.1 and
        round(parameters["b1"][3,0],2)==-0.36 and
        round(parameters["W2"][-0,2],2)==2.01 and
        round(parameters["b2"][0,0],2)==0.2)): grades["nn_model"]=True
    except: grades["nn_model"]=False


    parameters, X_assess = predict_test_case()
    predictions = predict(parameters, X_assess)
    try:
        if(round(np.mean(predictions),4)==0.6667): grades["predict"]=True
    except: grades["predict"]=False


    for x in grades:
        print (x,':',grades[x])
        
    