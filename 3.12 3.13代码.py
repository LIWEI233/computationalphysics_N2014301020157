import math
import pylab as pl
class harmonic:
    def __init__(self, w_0 = 0, theta_01=0.2,theta_02=0.2+0.001, time_of_duration = 400, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=1.2,D=2/3):
        self.n_uranium_A1 = [w_0]
        self.n_uranium_B1= [theta_01]
        self.n_uranium_A2 = [w_0]
        self.n_uranium_B2= [theta_02]
        self.a=[math.log(abs(theta_02-theta_01))]
        self.t = [0]
        self.g=g
        self.length=length
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.q=q
        self.F=F
        self.D=D
    def calculate(self):
        for i in range(self.nsteps):
            self.n_uranium_A1.append(self.n_uranium_A1[i] -((self.g/self.length)*math.sin(self.n_uranium_B1[i])+self.q*self.n_uranium_A1[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B1.append(self.n_uranium_B1[i] + self.n_uranium_A1[i+1]*self.dt)
            if self.n_uranium_B1[i+1]<-math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]+2*math.pi
            if self.n_uranium_B1[i+1]>math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]-2*math.pi
            else:
                pass
            self.n_uranium_A2.append(self.n_uranium_A2[i] -((self.g/self.length)*math.sin(self.n_uranium_B2[i])+self.q*self.n_uranium_A2[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B2.append(self.n_uranium_B2[i] + self.n_uranium_A2[i+1]*self.dt)
            if self.n_uranium_B2[i+1]<-math.pi:
                self.n_uranium_B2[i+1]=self.n_uranium_B2[i+1]+2*math.pi
            if self.n_uranium_B2[i+1]>math.pi:
                self.n_uranium_B2[i+1]=self.n_uranium_B2[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
            self.a.append(math.log(abs(self.n_uranium_B2[i+1]-self.n_uranium_B1[i+1])))
    def show_results(self):
        pl.plot(self.t, self.a)
        pl.xlabel('time ($s$)')
        pl.ylabel('angle difference(radians)')
        pl.title('angle difference versus time')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
        pl.xlim(0, 150)
        pl.ylim(-15, 5)
a = harmonic()
a.calculate()
a.show_results()
from __future__ import division
from math import *
from pylab import *
def change_amp(F):
    q = 0.5
    l = 9.8
    g = 9.8
    f = 2/3
    dt = pi/100
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    an=[theta0]
    av=[omega0] 
    while t[-1] < 6000*pi:
        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)
        if (t[-1]-(3*pi)/4)%(3*pi) <= dt:
            an.append(angle_new)
            av.append(avelo_new)
        t_new = t[-1] + dt
        t.append(t_new)
    return an,av
ang = change_amp(1.2)[0]
ave = change_amp(1.2)[1]
scatter(ang,ave,s=10)
title('angular velocity versus angle when F=1.2')
xlabel('theta(radians)')
ylabel('omega(radians/s)')
grid(True)
show()
from __future__ import division
from math import *
from pylab import *
def change_amp(theta0):
    q = 0.51
    l = 9.8
    g = 9.8
    f = 2/3
    dt = 0.04
    F=0.5
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    while t[-1] < 150:
        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > pi:
            angle_new -= 2*pi
        while angle_new < -pi:
            angle_new += 2*pi
        angle.append(angle_new)
        t_new = t[-1] + dt
        t.append(t_new)
    return angle,t
angle_1 = change_amp(0.2)[0]
t = change_amp(0.2)[1]
angle_2 = change_amp(0.201)[0]
dtheta=[]
for i in range(len(angle_1)):
    dtheta.append(abs(angle_1[i-1]-angle_2[i-1]))
plot(t,dtheta)
semilogy(t,dtheta)
title('angle difference versus time')
xlabel('time(s)')
ylabel('angle difference(radians)')
xlim(0,150)
ylim(0,100)
grid(True)
show(）
