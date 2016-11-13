import math
import pylab as pl
class Period_Doubing:
    def __init__(self,F ):
        self.n_uranium_A1 = [0]
        self.n_uranium_B1= [0.2]
        self.t = [0]
        self.g=9.8
        self.length=9.8
        self.dt = 3*math.pi/225
        self.time = [0]
        self.nsteps = int(10000//(3*math.pi/225) + 1)
        self.q_1 = 1/2
        self.F=F
        self.D=2/3
        self.n_uranium_A2=[0]
        self.n_uranium_B2=[0]
    def calculate(self):
        for i in range(self.nsteps):
            self.n_uranium_A1.append(self.n_uranium_A1[i] -\
            ((self.g/self.length)*math.sin(self.n_uranium_B1[i])+\
            self.q_1*self.n_uranium_A1[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.n_uranium_B1.append(self.n_uranium_B1[i] + self.n_uranium_A1[i+1]*self.dt)
            if self.n_uranium_B1[i+1]<-math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]+2*math.pi
            if self.n_uranium_B1[i+1]>math.pi:
                self.n_uranium_B1[i+1]=self.n_uranium_B1[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
        for i in range(self.nsteps):
            if self.t[i]%(2*math.pi/self.D)<0.0002:
               self.n_uranium_A2.append(self.n_uranium_A1[i])
               self.n_uranium_B2.append(self.n_uranium_B1[i])
    def show_results(self):
        pl.title('$\omega$ versue $\Theta$')
        pl.plot(self.n_uranium_B2, self.n_uranium_A2,'.')
        pl.xlabel('$\Theta$($radians$)')
        pl.ylabel('$\omega$($radians/s$)')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
a =  Period_Doubing(1.465)
a.calculate()
a.show_results()
from __future__ import division
from visual import *
from math import *
# add some constants
q=0.5
l=9.8
g=9.8
f=2/3
dt=3*pi/500
theta0=0.2
omega0=0
# add three ceilings
ceil1=box(pos=(-25,5,0),size=(3,0.5,2),material=materials.bricks)
ceil2=box(pos=(0,5,0),size=(3,0.5,2),material=materials.bricks)
ceil3=box(pos=(25,5,0),size=(3,0.5,2),material=materials.bricks)
ball1=sphere(pos=(-25+l*sin(theta0),3-l*cos(theta0),0),radius=1,material=materials.emissive,color=color.red)
ball2=sphere(pos=(l*sin(theta0),3-l*cos(theta0),0),radius=1,material=materials.emissive,color=color.yellow)
ball3=sphere(pos=(25+l*sin(theta0),3-l*cos(theta0),0),radius=1,material=materials.emissive,color=color.green)
ball1.omega=omega0
ball2.omega=omega0
ball3.omega=omega0
ball1.theta=theta0
ball2.theta=theta0
ball3.theta=theta0
ball1.t=0
ball2.t=0
ball3.t=0
ball1.F=1.35
ball2.F=1.44
ball3.F=1.465
string1=curve(pos=[ceil1.pos,ball1.pos],color=color.red)
string2=curve(pos=[ceil2.pos,ball2.pos],color=color.yellow)
string3=curve(pos=[ceil3.pos,ball3.pos],color=color.green)
po1=arrow(pos=ball1.pos,axis=(5*ball1.omega*cos(ball1.theta),5*ball1.omega*sin(ball1.theta),0),color=color.red)
po2=arrow(pos=ball2.pos,axis=(5*ball2.omega*cos(ball2.theta),5*ball2.omega*sin(ball2.theta),0),color=color.yellow)
po3=arrow(pos=ball3.pos,axis=(5*ball3.omega*cos(ball3.theta),5*ball3.omega*sin(ball3.theta),0),color=color.green)
while True:
    rate(100)
    ball1.omega=ball1.omega-((g/l)*sin(ball1.theta)+q*ball1.omega-ball1.F*sin(f*ball1.t))*dt
    ball2.omega=ball2.omega-((g/l)*sin(ball2.theta)+q*ball2.omega-ball2.F*sin(f*ball2.t))*dt
    ball3.omega=ball3.omega-((g/l)*sin(ball3.theta)+q*ball3.omega-ball3.F*sin(f*ball3.t))*dt
    angle1_new=ball1.theta+ball1.omega*dt
    while angle1_new>pi:
        angle1_new-=2*pi
    while angle1_new<-pi:
        angle1_new+=2*pi
    angle2_new=ball2.theta+ball2.omega*dt
    while angle2_new>pi:
        angle2_new-=2*pi
    while angle2_new<-pi:
        angle2_new+=2*pi
    angle3_new=ball3.theta+ball3.omega*dt
    while angle3_new>pi:
        angle3_new-=2*pi
    while angle3_new<-pi:
        angle3_new+=2*pi
    ball1.theta=angle1_new
    ball2.theta=angle2_new
    ball3.theta=angle3_new
    ball1.pos=(-25+l*sin(ball1.theta),3-l*cos(ball1.theta),0)
    ball2.pos=(l*sin(ball2.theta),3-l*cos(ball2.theta),0)
    ball3.pos=(25+l*sin(ball3.theta),3-l*cos(ball3.theta),0)
    string1.pos=[ceil1.pos,ball1.pos]
    string2.pos=[ceil2.pos,ball2.pos]
    string3.pos=[ceil3.pos,ball3.pos]
    po1.pos=ball1.pos
    po2.pos=ball2.pos
    po3.pos=ball3.pos
    po1.axis=(5*ball1.omega*cos(ball1.theta),5*ball1.omega*sin(ball1.theta),0)
    po2.axis=(5*ball2.omega*cos(ball2.theta),5*ball2.omega*sin(ball2.theta),0)
    po3.axis=(5*ball3.omega*cos(ball3.theta),5*ball3.omega*sin(ball3.theta),0)
    ball1.t=ball1.t+dt
    ball2.t=ball2.t+dt
    ball3.t=ball3.t+dt
