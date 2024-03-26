"""
sum = 1 +2
print(sum)

from datetime import date
date.today()
print(date.today())

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)



fact = "The Moon has no atmosphere."
fact = fact + "No sound can be heard on the Moon."
print(fact)

print("temperatures and facts about the moon".title())

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)


mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.startswith('-'): 
        item2 = item.replace('-', '')
        if item2.isnumeric():
            print(item)
    elif item.isnumeric():        
        print(item)

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print('**'.join(moon_facts))

text = ""Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.""
sentences = text.split('. ')
for sentece in sentences:
    if 'temperature' in sentece:
        print(sentece)



mass_percentage = "1/6"
#print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

#print(""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s."" % ("Moon", "Earth", "Moon", "Earth"))

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
print(subject.title())

"""

# Enter code below
name = 'Ganimides'
planet = 'Marte'
gravity = '1.43'

template = """Gravity Facts about {nombre}
--------------------------
Planet Name: {planeta}
Gravity on {nombre}: {gravedad} m/s2"""
print(template.format(nombre=name, planeta=planet, gravedad=gravity))
