from ursina import *
import math

G_const = 6.6743015151515151515e-11

class Object:
    def __init__(self, id, name, distance_sun, radius, mass, sidereal_day, sidereal_year, texture):
        self.id = id
        self.name = name
        self.distance_sun = distance_sun
        self.radius = radius
        self.mass = mass
        self.sidereal_day = sidereal_day
        self.sidereal_year = sidereal_year
        self.texture = texture
    def gravitation(self):
        g = G_const*self.mass/(self.radius**2)
        return g
    def escape_velocityI(self):
        VI = math.sqrt(G_const*self.mass/self.radius)
        return VI
    def escape_velocityII(self):
        VII = math.sqrt(2)*VI
        return VII
    def order(self):
        return int(self.id[2:4])

class Moons:
    def __init__(self, id, name, name_planet, distance_center_planet, radius_scale_planet, mass, sidereal_day, sidereal_year, texture):
        self.id = id
        self.name = name
        self.name_planet = name_planet
        self.distance_center_planet = distance_center_planet
        self.radius_scale_planet = radius_scale_planet
        self.mass = mass
        self.sidereal_day = sidereal_day
        self.sidereal_year = sidereal_year
        self.texture = texture


Sun =       Object("0.00.00", "Sun", 0, 696000000, 1.9891e30, 25.375, 0, 'assets\Textures\Sun.png')
Mercury =   Object("0.01.00", "Mercury", 57909170000, 2439700, 3.302e23, 58.625, 88.0, 'assets\Textures\Mercury.png')
Venus =     Object("0.02.00", "Venus", 108208926000, 6052000, 4.8685e24, 243, 224.7, 'assets\Textures\Venus.png')
Earth =     Object("0.03.00", "Earth", 149597887000, 6378000, 5.9742e24, 1, 365.2, 'assets\Textures\Earth.png')
Mars =      Object("0.04.00", "Mars", 227936637000, 3402500, 6.419e23, 1.02,687, 'assets\Textures\Mars.png')
Jupiter =   Object("0.05.00", "Jupiter", 778412027000, 71492000, 1.8986e27, 0.41, 4333, 'assets\Textures\Jupiter.png')
Saturn =    Object("0.06.00", "Saturn", 1426725413000, 60268000, 5.685168e26, 0.44, 10756, 'assets\Textures\Saturn.png')
Uranus =    Object("0.07.00", "Uranus", 2870972220000, 25559000, 8.6841e25, 0.718, 30707.5, 'assets\Textures\pUranus.png')
Neptune =   Object("0.08.00", "Neptune", 4498252900000, 24764000, 1.024396e26, 0.67, 60223.3, 'assets\Textures\pNeptune.png')
##Ceres

Moon =      Moons("0.03.01", "Moon", Earth, 384400000, 0.2727, 7.347e22, 27.3, 27.3, 'assets\Textures\Moon.png')
Phobos =    Moons("0.04.01", "Phobos", Mars, 9375000, 0.0032, 1.072e16, 0.319, 0.319, None)
Deimos =    Moons("0.04.02", "Deimos", Mars, 23460000, 0.0018, 1.476e15, 1.262, 1.262, None)
Io =        Moons("0.05.01", "Io", Jupiter, 421700000, 0.02547, 8.93e22, 1.769, 1.769, 'assets\Textures\Io.png')
Europa =    Moons("0.05.02", "Europa", Jupiter, 671034000, 0.0218, 4.8e22, 3.55, 3.55, 'assets\Textures\Europa.png')
Ganymede =  Moons("0.05.03", "Ganymede", Jupiter, 1070412000, 0.0368, 1.48e23, 7.15, 7.15, 'assets\Textures\Ganymede.png')
Callisto =  Moons("0.05.04", "Callisto", Jupiter, 1882709000, 0.0337, 1.08e23, 16.69, 16.69, 'assets\Textures\Callisto.png')
Rhea =      Moons("0.06.05", "Rhea", Saturn, 527100000, 0.01267, 2.3e21, 4.5, 4.5, 'assets\Textures\Moon.png')  #similar appearance to the moon.
Titan =     Moons("0.06.06", "Titan", Saturn, 1222000000, 0.0427, 1.345e23, 16, 16, 'assets\Textures\Titan.png')
Iapetus =   Moons("0.06.08", "Iapetus", Saturn, 3561000000, 0.0119, 1.8e21, 79.3, 79.3, 'assets\Textures\Iapetus.png')
Titania =   Moons("0.07.03", "Titania", Uranus, 436300000, 0.03, 3.53e21, 8.71, 8.71, 'assets\Textures\Moon.png') #similar appearance to the moon.
Oberon =    Moons("0.07.04", "Oberon", Uranus, 583500000, 0.029, 3e21, 13.46, 13.46, 'assets\Textures\Moon.png') #similar appearance to the moon.
Triton =    Moons("0.08.01", "Triton", Neptune, 354800000, 0.0546, 2.14e22, 5.88, 5.88, 'assets\Textures\Triton.png')

print(Uranus.order())
print(Neptune.order())