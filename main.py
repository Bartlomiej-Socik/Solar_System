from ursina import *
from astronomical_object import *
import numpy as np
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

r_scale = 1e6
r_position = 1e10

def rotation(astronomical_ob,ob):
    astronomical_ob.rotation_y = astronomical_ob.rotation_y+(1/ob.sidereal_day)

def Orbital_period(astronomical_ob,ob,ex):
    try:
        astronomical_ob.x = np.cos(t*(100/ob.sidereal_year))*ob.distance_sun/ex
        astronomical_ob.z = np.sin(t*(100/ob.sidereal_year))*ob.distance_sun/ex
    except Exception:
        astronomical_ob.x = np.cos(t*(100/ob.sidereal_year))*ob.distance_center_planet/ex
        astronomical_ob.z = np.sin(t*(100/ob.sidereal_year))*ob.distance_center_planet/ex

def update():

    rotation(sphere0,Sun)
    rotation(sphere1,Mercury)
    rotation(sphere2,Venus)
    rotation(sphere3,Earth), rotation(moon3_01,Moon)
    rotation(sphere4,Mars), rotation(moon4_01,Phobos), rotation(moon4_02,Deimos)
    rotation(sphere5,Jupiter), rotation(moon5_01,Io), rotation(moon5_02,Europa), rotation(moon5_03,Ganymede), rotation(moon5_04,Callisto)
    rotation(sphere6,Saturn), rotation(moon6_05,Rhea), rotation(moon6_06,Titan), rotation(moon6_08,Iapetus)
    rotation(sphere7,Uranus), rotation(moon7_03,Titania), rotation(moon7_04,Oberon)
    rotation(sphere8,Neptune), rotation(moon8_01,Triton)
    
    global t
    t = t + 0.000002
    angle = np.pi*40/180
    
    Orbital_period(sphere1,Mercury,1e9)
    Orbital_period(sphere2,Venus,1e9)
    Orbital_period(sphere3,Earth,1e9), Orbital_period(moon3_01,Moon,1e8)
    Orbital_period(sphere4,Mars,1e9), Orbital_period(moon4_01,Phobos,1e7), Orbital_period(moon4_02,Deimos,1e7)
    Orbital_period(sphere5,Jupiter,1e9), Orbital_period(moon5_01,Io,6e8), Orbital_period(moon5_02,Europa,6e8), Orbital_period(moon5_03,Ganymede,9e8), Orbital_period(moon5_04,Callisto,9e8)
    Orbital_period(sphere6,Saturn,1e9), Orbital_period(ring,Saturn,1e9), Orbital_period(moon6_05,Rhea,3e8), Orbital_period(moon6_06,Titan,5.8e8), Orbital_period(moon6_08,Iapetus,7e8)
    Orbital_period(sphere7,Uranus,1e9), Orbital_period(moon7_03,Titania,5e8), Orbital_period(moon7_04,Oberon,5e8)
    Orbital_period(sphere8,Neptune,1e9), Orbital_period(moon8_01,Triton,2e8)



app = Ursina()
window.color = color.black
background_music = Audio('Assets\Interstellar Main Theme - Hans Zimmer.mp3', volume=0.5, pitch=1, loop=True, autoplay=True)
background_music.play()

sphere0 = Entity(model='sphere', collider='mesh', texture=load_texture(Sun.texture), scale=Sun.radius/1e7, position = (0,0,0), shader=lit_with_shadows_shader)
sphere1 = Entity(name=Mercury.name, model='sphere', texture=load_texture(Mercury.texture), scale=Mercury.radius/r_scale)
sphere2 = Entity(name=Venus.name, model='sphere', texture=load_texture(Venus.texture), scale=Venus.radius/r_scale)
sphere3 = Entity(name=Earth.name, model='sphere', texture=load_texture(Earth.texture), scale=Earth.radius/r_scale)
sphere4 = Entity(name=Mars.name, model='sphere', texture=load_texture(Mars.texture), scale=Mars.radius/r_scale)
sphere5 = Entity(name=Jupiter.name, model='sphere', texture=load_texture(Jupiter.texture), scale=Jupiter.radius/r_scale)
sphere6 = Entity(name=Saturn.name, model='sphere', texture=load_texture(Saturn.texture), scale=Saturn.radius/r_scale)
sphere7 = Entity(name=Uranus.name, model='sphere', texture=load_texture(Uranus.texture), scale=Uranus.radius/r_scale)
sphere8 = Entity(name=Neptune.name, model='sphere', texture=load_texture(Neptune.texture), scale=Neptune.radius/r_scale)

ring = Entity(model='sphere',texture=load_texture('Assets\Textures\S_rings.png'), collider='mesh', position=(sphere6.x, sphere6.y, sphere6.z), scale=sphere6.scale*3, scale_y=2)
moon3_01 = Entity(name=Moon.name, parent=sphere3, model='sphere', texture=load_texture(Moon.texture), scale=Moon.radius_scale_planet)
moon4_01 = Entity(name=Phobos.name, parent=sphere4, model='Assets\models_3D\Phobos.glb', scale=Phobos.radius_scale_planet)
moon4_02 = Entity(name=Deimos.name, parent=sphere4, model='Assets\models_3D\Deimos.glb', scale=Deimos.radius_scale_planet)
moon5_01 = Entity(name=Io.name, parent=sphere5, model='sphere', texture=load_texture(Io.texture), scale=Io.radius_scale_planet)
moon5_02 = Entity(name=Europa.name, parent=sphere5, model='sphere', texture=load_texture(Europa.texture), scale=Europa.radius_scale_planet)
moon5_03 = Entity(name=Ganymede.name, parent=sphere5, model='sphere', texture=load_texture(Ganymede.texture), scale=Ganymede.radius_scale_planet)
moon5_04 = Entity(name=Callisto.name, parent=sphere5, model='sphere', texture=load_texture(Callisto.texture), scale=Callisto.radius_scale_planet)
moon6_05 = Entity(name=Rhea.name, parent=sphere6, model='sphere', texture=load_texture(Rhea.texture), scale=Rhea.radius_scale_planet)
moon6_06 = Entity(name=Titan.name, parent=sphere6, model='sphere', texture=load_texture(Titan.texture), scale=Titan.radius_scale_planet)
moon6_08 = Entity(name=Iapetus.name, parent=sphere6, model='sphere', texture=load_texture(Iapetus.texture), scale=Iapetus.radius_scale_planet)
moon7_03 = Entity(name=Titania.name, parent=sphere7, model='sphere', texture=load_texture(Titania.texture), scale=Titania.radius_scale_planet)
moon7_04 = Entity(name=Oberon.name, parent=sphere7, model='sphere', texture=load_texture(Oberon.texture), scale=Oberon.radius_scale_planet)
moon8_01 = Entity(name=Triton.name, parent=sphere8, model='sphere', texture=load_texture(Triton.texture), scale=Triton.radius_scale_planet)

star0 = Entity(model='sphere', color=color.white, scale=4, position=(2000, 1000, 200), shader=lit_with_shadows_shader)


t = -np.pi

LightSun = PointLight(shadows=True)
txt = Text(text="Solar System", x=-0.88, y=-0.45)

DropdownMenu(text='Planet', color=color.gray, buttons=(
    DropdownMenuButton('Mercury'),
    DropdownMenuButton('Venus'),
    DropdownMenuButton('Earth'),
    DropdownMenuButton('Mars'),
    DropdownMenuButton('Jupiter'),
    DropdownMenuButton('Saturn'),
    DropdownMenuButton('Uranus'),
    DropdownMenuButton('Neptune'),
    ),)

EditorCamera()

app.run()
