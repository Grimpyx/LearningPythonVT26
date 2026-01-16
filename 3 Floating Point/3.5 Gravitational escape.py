import math
G = 6.674e-11

def escape(M,r,V):
    v_e_squared = 2 * G * M / r
    v_inf_squared = math.pow(V,2) - v_e_squared

    if v_inf_squared > 0: print(f"Excess speed: {math.sqrt(v_inf_squared)}")
    else: print("the object won't escape")