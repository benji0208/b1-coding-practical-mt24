 

class controller:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
        self.e_prev = 0
     
        
    def control(self,e):
        u = self.Kp*e + self.Kd*(e - self.e_prev)
        self.e_prev = e
        return u




    
