from __future__ import division
G=globals()
def Back(x,z):
	glBlendFunc(GL_SRC_ALPHA,GL_ONE)
	glColor4f(1-z,abs(z-.5),z,.4)
	glBegin(GL_QUADS)
	glVertex2f(160+160*cos(x/10),512*sin(x/10))
	glVertex2f(160+160*cos(x/20),512*sin(x/100))
	glVertex2f(160+160*cos(x/30),0)
	glVertex2f(160+160*cos(x/40),0)
	glVertex2f(160+240*cos(x/10),200+300*sin(x/5))
	glVertex2f(160+160*cos(x/10),300+300*sin(x/10))
	glVertex2f(160-240*cos(x/10),400+300*sin(x/100))
	glVertex2f(160-160*cos(x/10),512)
	glEnd()
Time={}
V=0
for v in range(0,400,40):
	Time[V+v]=lambda v=v:F(Cannon(0,v*.75,530,piC7,4,15))
	Time[V+v+10]=lambda v=v:F(Cannon(1,320-v*.75,530,piC9,4,15))
	Time[V+v+20]=lambda:F(Gattle(2,160,530,pi32,5,20))
V=350
for v in range(0,400,20):
	Time[V+v]=lambda v=v:F(Cannon(0,-8,v,0,5,20))
	Time[V+v+1]=lambda v=v:F(Cannon(2,328,v,pi,5,15))
Time[800]=lambda:F(CannonCannon(160))
Time[1200]=lambda:F(Complement(160))
"""
for v in range(900,1200,45):Time[v]=lambda v=v:(F(Gattle((v%60)//30,0,1300-v,piC6,6,8,6)),F(Gattle(1+(v%60)//30,320,1300-v,piCA,6,10,5)))
for v in range(1202,1400,60):Time[v]=lambda:F(LaserC(0,-24+64,520,0,5,pi32))
for v in range(1230,1400,60):Time[v]=lambda:F(LaserC(1,-24+80,520,0,5,pi32))
Time[1400]=lambda:F(LaserC(1,-24,0,0,5,pi12))
"""#"""
"""
v=1111;v[1]=1;repeat(4){
ds_grid_set_region(0,v,0,v+1,0,mis)
ds_grid_set_region(0,v,2,v+1,2,-64)
ds_grid_set_region(0,v,3,v+1,3,v[1])
ds_grid_set_region(0,v,5,v+1,5,4)
ds_grid_set_region(0,v,6,v+1,6,12)
ds_grid_set_region(0,v,7,v+1,7,128-use.hrd*16)
ds_grid_set(0,v,1,240+240*v[1])
ds_grid_set(0,v+1,1,240+240*v[1])
ds_grid_set(0,v,4,270-45*v[1])
ds_grid_set(0,v+1,4,270+45*v[1])
v+=64;v[1]*=-1}
v=1450;repeat(4){dsg(v,mis,240,-64,0,270,4,8,128-use.hrd*16);v+=96}
v=1444;repeat(4+use.hrd){
ds_grid_set_region(0,v,0,v+1,0,snk)
ds_grid_set_region(0,v,2,v+1,2,v-1440)
ds_grid_set_region(0,v,5,v+1,5,v-1400>>6)
ds_grid_set_region(0,v,6,v+1,6,8)
ds_grid_set_region(0,v,7,v+1,7,48-use.hrd*8)
ds_grid_set(0,v,1,-16)
ds_grid_set(0,v+1,1,496)
ds_grid_set(0,v,3,v[1])
v[1]*=-1
ds_grid_set(0,v+1,3,v[1])
ds_grid_set(0,v+1,4,180)
v+=384/(4+use.hrd)}
"""
