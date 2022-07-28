from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
class PD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
            if self.rotation_x < 90:
                self.rotation_x+=0.1
        else:
            self.world_position += self.forward * self.speed * time.dt * self.lifetime
            if self.y>3:
                help_position = self.world_position-(0,2,0)
            else:
                help_position = self.world_position
            destroy(self)
            if help_position[1]<0:
                help_position=(help_position[0],0.5,help_position[2])
            invoke(Audio, 'files/sound/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = help_position)
            pdpd.position=help_position
            destroy(boom,delay = 5)
class HJD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
            if self.rotation_x < 90:
                self.rotation_x+=0.6
        else:
            self.world_position += self.forward * self.speed * time.dt
            help_position = self.world_position
            destroy(self)
            invoke(Audio, 'files/sound/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = help_position)
            hjdpd.position=help_position
            destroy(boom,delay = 5)
class kt(Entity):
    def __init__(self):
        super().__init__(model='files/3d/kt.obj',collider='box',color=color.red,position=(random.randint(-75,75),100,random.randint(-100,100)))
    def update(self):
        if self.y>1.5:
            self.y-=0.1
        if abs(self.x-player.x)<5:
            if abs(self.z-player.z)<5:
                if abs(self.y-player.y)<2:
                    if pdslhelp.x<20:
                        pdslhelp.x+=10
                    else:
                        pdslhelp.x=30
                    if player.life<20:
                        player.life+=1
                    destroy(self)
class tk(Entity):
    def __init__(self,z,life=4,time=15,time1=30):
        super().__init__(model='files/3d/tk.obj',collider='box',position=(-130,1,z))
        time=random.randint(12,17)
        time1 = random.randint(27, 34)
        self.time=time
        self.time1=time1
        self.life=life
    def update(self):
        if self.rotation_y==180:
            if not (player.x-self.x>0 and player.x-self.x<10 and abs(self.z-player.z)<3):
                self.x+=self.life/10
            else:
                self.time=random.randint(12,17)
                self.look_at(player,axis='left')
                invoke(Audio, 'files/sound/fs.ogg')
                PD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-(-89,90,0))
        if self.rotation_y==0:
            if not (self.x-player.x>0 and self.x-player.x<10 and abs(self.z-player.z)<3):
                self.x-=self.life/10
            else:
                self.time=random.randint(12,17)
                self.look_at(player,axis='left')
                invoke(Audio, 'files/sound/fs.ogg')
                PD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-(-89,90,0))
        if self.x>130:
            self.rotation_y=0
        if self.x<-130:
            self.rotation_y=180
        if self.life<1:
            self.life=0
            player.jif+=0.1
            destroy(self,delay=0.5)
        if abs(self.x-pdpd.x)<11:
            if abs(self.z-pdpd.z)<11:
                if abs(self.y-pdpd.y)<7:
                    self.life-=0.1
        if abs(self.x-pdpd.x)<17:
            if abs(self.z-pdpd.z)<17:
                if abs(self.y-pdpd.y)<7:
                    self.life-=0.1
        if abs(self.x-pdpd.x)<5:
            if abs(self.z-pdpd.z)<5:
                if abs(self.y-pdpd.y)<7:
                    self.life-=0.2
        if abs(self.x-hjdpd.x)<11:
            if abs(self.z-hjdpd.z)<11:
                if abs(self.y-hjdpd.y)<7:
                    self.life-=0.1
        if abs(self.x-hjdpd.x)<17:
            if abs(self.z-hjdpd.z)<17:
                if abs(self.y-hjdpd.y)<7:
                    self.life-=0.1
        if abs(self.x-hjdpd.x)<5:
            if abs(self.z-hjdpd.z)<5:
                if abs(self.y-hjdpd.y)<7:
                    self.life-=0.2
        if self.time<0:
            self.time=0
        if self.time>0:
            self.time-=0.01
        if self.time==0:
            self.time=random.randint(12,17)
            self.look_at(player,axis='left')
            invoke(Audio, 'files/sound/fs.ogg')
            if abs(self.x-player.x)<40 and abs(self.z-player.z)<40 :
                PD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-(-55,90,0))
            else:
                PD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=self.world_position+(0,2.5,0),
                   rotation=self.world_rotation-((((pow((self.x-player.x)**2+(self.z-player.z)**2,0.5)/2)/36)*0.1)+3,90,0))
            self.rotation_y = 180
        if self.time1<0:
            self.time1=0
        if self.time1>0:
            self.time1-=0.01
        if self.time1 == 0:
            self.time1 = random.randint(12, 17)
            self.look_at(player, axis='left')
            for n in range(6):
                invoke(Audio, 'files/sound/fs.ogg')
                HJD(model="files/3d/hjd.obj",
                    scale=0.1,
                    position=self.world_position+(0, (random.randint(0, 20) / 10)+3, 0),
                    rotation=self.world_rotation-((((pow((self.x-player.x)**2+(self.z-player.z)**2,0.5)/2)/36)*0.6)+10, random.randint(-10, 10)+90, 0))
            self.rotation_y = 0
        if player.life==0:
            destroy(self)
class fj(Entity):
    def __init__(self,z,life=0.1):
        super().__init__(model='files/3d/fj1.obj',collider='box',position=(-200,50,z))
        self.life=life
    def update(self):
        self.x+=0.7
        if self.x>200:
            destroy(self,delay=0.5)
        if self.life<0.1:
            player.jif+=0.3
            destroy(self,delay=0.5)
        if abs(self.x-pdpd.x)<20:
            if abs(self.z-pdpd.z)<20:
                if abs(self.y-pdpd.y)<15:
                    self.life-=0.1
        if abs(self.x-hjdpd.x)<20:
            if abs(self.z-hjdpd.z)<20:
                if abs(self.y-hjdpd.y)<15:
                    self.life-=0.1
        if random.randint(1,10)==1 :
            invoke(Audio, 'files/sound/fs.ogg')
            PD(model="files/3d/hjd.obj",
               scale=1,
               position=self.world_position,
               rotation=(90,0,0))
def input(key):
    if key == "escape":
        quit()
    if key == 'left mouse down' and cdpdhelp.x==0 and pdslhelp.x>0:
        cdpd = cdpdhelp.x
        cdpd=3
        cdpdhelp.x = cdpd
        pdslhelp.x -=1
        invoke(Audio, 'files/sound/fs.ogg')
        PD(model="files/3d/hjd.obj",
               scale=0.1,
               position=player.camera_pivot.world_position,
               rotation=player.camera_pivot.world_rotation)
    if key == "w" or key=="s":
        tkdz.rotation = player.world_rotation
    if key=="a":
        tkdz.rotation = player.world_rotation+(0,-90,0)
    if key=="d":
        tkdz.rotation = player.world_rotation+(0,90,0)
    if key=="f" and cdhjdhelp.x==0 and pdslhelp.x>14:
        cdhjd = cdhjdhelp.x
        cdhjd=3
        cdhjdhelp.x = cdhjd
        for n in range(15):
            pdslhelp.x-=1
            invoke(Audio, 'files/sound/fs.ogg')
            HJD(model="files/3d/hjd.obj",
                   scale=0.1,
                   position=player.camera_pivot.world_position+(0,(random.randint(0,20)/10),0),
                   rotation=tkdz.world_rotation-(random.randint(25,45),random.randint(-10,10),0))
    if key=="y" and ctk.z==0:
        invoke(Audio, 'files/sound/nb.ogg')
        ctk.z=75
def update():
    tkdz.position = player.world_position+(0,0.5,0)
    tkp.position = player.world_position+(0,1,0)
    tkp.rotation = player.world_rotation
    cdpd = cdpdhelp.x
    if cdpd<0:
        cdpd=0
    if cdpd!=0:
        cdpd-=0.01
    cdpdhelp.x = cdpd
    cdhjd = cdhjdhelp.x
    if cdhjd<0:
        cdhjd=0
    if cdhjd!=0:
        cdhjd-=0.0005
    cdhjdhelp.x = cdhjd
    pdsl1=pdslhelp.x
    player.y=0.5
    cdp.text=('paodanCD(1fa):'+str(round(cdpd,3)))
    cdh.text=('huojiandanCD(15fa):'+str(round(cdhjd,3)))
    pdsl.text=('paodanshuliang:'+str(int(pdsl1))+'/30')
    playerlife.text=('life:'+str(int(player.life)))
    jf.text = ('jifen:' + str(int(player.jif)))
    if kttime.x!=0:
        kttime.x-=0.01
    if kttime.x<0:
        kttime.x=0
    if kttime.x==0:
        kt()
        kttime.x=15
    if pdpd.y!=-10:
        if pdpd.rotation_z<0:
            pdpd.rotation_z=0
        if pdpd.rotation_z!=0:
            pdpd.rotation_z-=0.01
        if pdpd.rotation_z==0:
            pdpd.y=-10
            pdpd.rotation_z=0.1
    if hjdpd.y!=-10:
        if hjdpd.rotation_z<0:
            hjdpd.rotation_z=0
        if hjdpd.rotation_z!=0:
            hjdpd.rotation_z-=0.01
        if hjdpd.rotation_z==0:
            hjdpd.y=-10
            hjdpd.rotation_z=0.1
    player.speed=player.life/2
    if player.life<0:
        player.life=0
    if abs(player.x-pdpd.x)<8:
            if abs(player.z-pdpd.z)<8:
                if abs(player.y-pdpd.y)<7:
                    player.life-=0.1
    if abs(player.x-pdpd.x)<15:
        if abs(player.z-pdpd.z)<15:
            if abs(player.y-pdpd.y)<7:
                player.life-=0.1
    if abs(player.x-pdpd.x)<5:
        if abs(player.z-pdpd.z)<5:
            if abs(player.y-pdpd.y)<7:
                player.life-=0.2
    if abs(player.x-hjdpd.x)<8:
        if abs(player.z-hjdpd.z)<8:
            if abs(player.y-hjdpd.y)<7:
                player.life-=0.1
    if abs(player.x-hjdpd.x)<15:
        if abs(player.z-hjdpd.z)<15:
            if abs(player.y-hjdpd.y)<7:
                player.life-=0.1
    if abs(player.x-hjdpd.x)<5:
        if abs(player.z-hjdpd.z)<5:
            if abs(player.y-hjdpd.y)<7:
                player.life-=0.2
    if lifefz.z!=0:
        lifefz.z-=0.01
    if lifefz.z<0:
        lifefz.z=0
    if int(player.life)==0 and lifefz.x==0:
        lifefz.x=1
        invoke(Audio, 'files/sound/no.ogg')
    if int(player.life)>0 and lifefz.z==0 and ctk.z==0:
        lifefz.z=1
        invoke(Audio, 'files/sound/fdj.ogg')
    if ctk.x==0:
        tk(z=random.randint(1,6)*45-130)
        fj(z=player.z)
        ctk.x=10
    if ctk.x<0:
        ctk.x=0
    if ctk.x!=0:
        ctk.x-=0.01
    if ctk.z<0:
        ctk.z=0
    if ctk.z!=0:
        ctk.z-=0.01
    if int(player.life)==0:
        player.life=0
app = Ursina()
Sky()
player = FirstPersonController(speed=10,scale=2.5,life=20,jif=0)
ground1 = Entity(model = 'cube',scale = (300,1,300),color = color.lime,texture = "td.png",texture_scale = (300,300),collider="box")
wall1 = Entity(model = 'cube',scale = (300,8,1),color = color.white,texture = "sky.png",texture_scale = (300,8),collider = "box",position = (0,4,150))
wall2 = Entity(model = 'cube',scale = (300,8,1),color = color.white,texture = "sky.png",texture_scale = (300,8),collider = "box",position = (0,4,-150))
wall3 = Entity(model = 'cube',scale = (1,8,300),color = color.white,texture = "sky.png",texture_scale = (300,8),collider = "box",position = (150,4,0))
wall4 = Entity(model = 'cube',scale = (1,8,300),color = color.white,texture = "sky.png",texture_scale = (300,8),collider = "box",position = (-150,4,0))
tkdz = Entity(model = 'files/3d/mtk.obj',texture = 'files/3d/mtk.mtl',collider="box")
tkp = Entity(model = 'files/3d/mtkp.obj',color=color.white,texture = 'files/3d/mtkp.mtl',collider="box")
cdpdhelp = Entity(model = 'cube',position=(0,-5,0))
cdhjdhelp = Entity(model = 'cube',position=(0,-5,0))
pdslhelp = Entity(model = 'cube',position=(20,-5,0))
kttime = Entity(model = 'cube',position=(0,-5,0))
lifefz = Entity(model = 'cube',position=(0,-5,0))
ctk = Entity(model = 'cube',position=(1,-5,0))
pdpd = Entity(model = 'cube',scale=0.01,position=(0,-10,0),rotation_z=0.1)
hjdpd = Entity(model = 'cube',scale=0.01,position=(0,-10,0),rotation_z=0.1)
cdp=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.4))
cdh=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.34))
pdsl=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.46))
playerlife=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.28))
jf=Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.6,-0.22))
for v in range(6):
    tk(z=v*45-130)
    if v!=6:
        for n in range(4):
            y=1
            x=v*45-130+22
            z=n*45-130+30
            m = Entity(model='cube', scale=(10, 1, 10), color=color.white, texture="td.png", texture_scale=(10, 10),
                       collider="box", position=(x, y, z))
            m = Entity(model='cube', scale=(10, 8, 1), color=color.white, texture="td.png", texture_scale=(10, 8),
                       collider="box", position=(x, y + 3, z + 5))
            m = Entity(model='cube', scale=(10, 8, 1), color=color.white, texture="td.png", texture_scale=(10, 8),
                       collider="box", position=(x, y + 3, z - 5))
            m = Entity(model='cube', scale=(1, 8, 10), color=color.white, texture="td.png", texture_scale=(10, 8),
                       collider="box", position=(x + 5, y + 3, z))
            m = Entity(model='cube', scale=(1, 8, 4), color=color.white, texture="td.png", texture_scale=(8, 4),
                       collider="box",
                       position=(x - 5, y + 3, z + 3))
            m = Entity(model='cube', scale=(1, 8, 4), color=color.white, texture="td.png", texture_scale=(8, 4),
                       collider="box",
                       position=(x - 5, y + 3, z - 3))
            m = Entity(model='cube', scale=(1, 4, 2), color=color.white, texture="td.png", texture_scale=(4, 2),
                       collider="box",
                       position=(x - 5, y + 6, z))
            m = Entity(model='cube', scale=(10, 1, 8), color=color.white, texture="td.png", texture_scale=(10, 8),
                       collider="box", position=(x, y + 6, z - 1))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x + 4, y + 6, z + 4))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x + 3, y + 5, z + 4))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x + 2, y + 4, z + 4))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x + 1, y + 3, z + 4))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x, y + 2, z + 4))
            m = Entity(model='cube', scale=(1, 1, 2), color=color.white, texture="td.png", texture_scale=(2, 1),
                       collider="box",
                       position=(x - 1, y + 1, z + 4))
app.run()
