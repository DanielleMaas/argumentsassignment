# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# partone


def greet(name, hello='Hello, <name>!'):
    replacingname = hello.replace('<name>', name)
    print(replacingname)
    return(replacingname)


Firstname = "Sam"
greet(Firstname)
greet(Firstname, "What's up, <name>!")


# parttwo


def force(mass, body='earth'):
    celestialbody = {
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15,
        'saturn': 10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.58
    }
    valueofbody = celestialbody[body]
    calculateforce = mass * round(valueofbody,1)
    return calculateforce

mass = 1.0

force(mass,)

# partthree
# gravity is defined as 6674*10 to the -11nd power
# distance can be entered in meters and will be caculated to the 2nd power
# for some reason dividing by 1000 was necessary to get the right result/ get a pass in wincpy check



def pull(m1, m2, d):
    gravity = 6674*10**-11
    d = d**2
    calculation = gravity * ((m1*m2)/d)/1000
    return(calculation)
