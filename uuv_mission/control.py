 
def controller(e,e_prev):
    Kp = 0.15
    Kd = 0.6
    return Kp*e + Kd*(e - e_prev)

    
