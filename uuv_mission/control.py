 

class controller:
    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
        self.e_prev = 0
        self.total_error = 0
     
        
    def control(self,e):
        u = self.Kp*e + self.Kd*(e - self.e_prev)
        self.total_error += e
        self.e_prev = e
        return u
    def get_total_error(self):
        return self.total_error
    




    
