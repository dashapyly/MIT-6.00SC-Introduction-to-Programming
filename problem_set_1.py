# coding: utf-8

# In[1]:

def evaluate_poly(poly, x):
    evaluate_poly = 0
    x = float(x)
    assert type(poly) == tuple
    assert type(x) == float
    for i in range (0,len(poly)):
        evaluate_poly = evaluate_poly + poly[i]*(x**i)
    return float(evaluate_poly)
evaluate_poly((0.0,0.0,5.0,9.3,7.0),-13)


# In[3]:

def compute_deriv(poly):
    compute_deriv = []
    assert len(poly) > 0
    assert type(poly) == tuple
    #assert type(x) == float
    for i in range (1,len(poly)):
        elem_deriv = [poly[i]*i]
        compute_deriv = compute_deriv + elem_deriv
    compute_deriv = tuple(compute_deriv)                                              
    return compute_deriv
compute_deriv((-13.39,0.0,17.5,3.0,1.0))


# In[4]:

def compute_root(poly,x_0, error):
    x_0 = float(x_0)
    error = float(error)
    assert error > 0
    itteration = 0
    assert len(poly) > 1
    x = x_0
    while abs(evaluate_poly(poly,x)) > error:
        x = x - evaluate_poly(poly,x)/evaluate_poly(compute_deriv(poly),x)
        itteration +=1
    answer = (x, itteration)
    return answer 
compute_root((-13.39,0.0,17.5,3.0,1.0), 0.1, 0.0001)
