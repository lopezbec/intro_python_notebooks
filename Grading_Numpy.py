

def GRADING_Algebra(testx,normalizeCols,dot_classic,dot_vectorized,mul_classic,mul_vectorized,Gdot_classic,Gdot_vectorized):
    
    grades={"normalizeCols":False, "dot_classic":False,"dot_vectorized":False,
            "mul_classic":False,"mul_vectorized":False,"Gdot_classic":False,"Gdot_vectorized":False}
    try:
        if(round(normalizeCols(testx)[0,0],3)==round(0.2672612419124244,3)): grades["normalizeCols"]=True
    except: grades["normalizeCols"]=False
    try:
        if(round(dot_classic,3)==round(236.14775068085237,3)): grades["dot_classic"]=True
    except: grades["dot_classic"]=False
    try:
        if(round(dot_vectorized,3)==round(236.1477506808524,3)):grades["dot_vectorized"]=True
    except: grades["dot_vectorized"]=False
    try:
        if(round(mul_classic[0],3)==round(0.27112020101848283,3)):grades["mul_classic"]=True
    except: grades["mul_classic"]=False
    try:
        if(round(mul_vectorized[0,0],3)==round(0.27112020101848283,3)):grades["mul_vectorized"]=True
    except: grades["mul_vectorized"]=False
    try:
        if(round(Gdot_classic[2],3)==round(234.36335991512357,3)):grades["Gdot_classic"]=True
    except: grades["Gdot_classic"]=False
    try:
        if(round(Gdot_vectorized[2,0],3)==round(234.36335991512334,3)): grades["Gdot_vectorized"]=True
    except: grades["Gdot_vectorized"]=False

    for x in grades:
        print (x,':',grades[x])
        
        
def GRADING_NumPy_intro(np441,npodds,x1dim,x1shape,x1size,x1sizeb,x3D_normal):

    grades={"np441":False, "npodds":False,"x1dim":False,
            "x1shape":False,"x1size":False,"x1sizeb":False,"x3D_normal":False}
    try:
        if(sum(sum(np441))==16): grades["np441"]=True
    except: grades["np441"]=False
    try:
        if(npodds[0]==1 and npodds[3]==7): grades["npodds"]=True
    except: grades["npodds"]=False
    try:
        if(x1dim==1):grades["x1dim"]=True
    except: grades["x1dim"]=False
    try:
        if(x1shape[0]==6 ):grades["x1shape"]=True
    except: grades["x1shape"]=False
    try:
        if(x1size==6):grades["x1size"]=True
    except: grades["x1size"]=False
    try:
        if(x1sizeb==48):grades["x1sizeb"]=True
    except: grades["x1sizeb"]=False
    try:
        if(sum(sum(sum(x3D_normal)))==129.60959181697206): grades["x3D_normal"]=True
    except: grades["x3D_normal"]=False


    for x in grades:
        print (x,':',grades[x])
