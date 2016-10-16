import pylab as pl
from math import*
class cannon_shell:
    def __init__(self, time_step=0.1, initial_velocity=1000, initial_vx=707,initial_vy=707,grav = 9.8,B_m=0.00004,a=0.0065,T=300,arf=2.5):
        self.v = [initial_velocity]
        self.g = grav
        self.bm = B_m
        self.a = a
        self.T = T
        self.arf = arf
        self.t = [0]
        self.x = [0]
        self.y = [0]
        self.vx = [initial_vx]
        self.vy = [initial_vy]
        self.dt = time_step   
    def run(self):
        _time = 0 
        while(self.vy[-1] >= -self.vy[0]):
            self.x.append(self.x[-1] + self.dt * self.vx[0])
            self.y.append(self.y[-1] + self.dt * self.vy[-1])
            self.vy.append(self.vy[-1] - self.g * self.dt )
            self.t.append(_time)
            _time += self.dt            
        self.x.append(self.x[-1]+ self.vx[0] * (self.vy[-2]+self.vy[0])/self.g)
        self.y.append(0)
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        #pl.title("cannon_shell without air resistance", fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.ylim(0,45000)
        #pl.legend([plot],["ideal"],loc="best")
a = cannon_shell()
a.run()
a.show_results()
b = cannon_shell(initial_vx=866,initial_vy=500)
b.run()
b.show_results()
c = cannon_shell(initial_vx=500,initial_vy=866)
c.run()
c.show_results()
d = cannon_shell(initial_vx=643,initial_vy=766)
d.run()
d.show_results()
e = cannon_shell(initial_vx=766,initial_vy=643)
e.run()
e.show_results()
pl.title("ideal")
show()
