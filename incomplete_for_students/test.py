import model

m = model.Model()

print("Default model: {}\n".format(m))

print("test_1: Reglage des moteurs a la meme vitesse ###")
m.m1.speed = 0.1
m.m2.speed = 0.1
linear_speed, rotation_speed = m.dk()
print("linear_speed= {}\nrotation_speed= {}".format(linear_speed, rotation_speed))
if (linear_speed == 0.1):
	print ("test_1 OK\n")
else:
	print ("nok\n")


print("test_2: Reglage des vitesses opposees pour les deux moteurs ###")
m.m1.speed = 0.1
m.m2.speed = -0.1
linear_speed, rotation_speed = m.dk()
print("linear_speed= {}\nrotation_speed= {}".format(linear_speed, rotation_speed))
if (linear_speed == 0.0):
	print ("test_2 OK\n")
else:
	print ("nok\n")

print ("test_2: Reglage des vitesses differentes ###")
m.m1.speed = 0.1
m.m2.speed = 0.2
linear_speed, rotation_speed = m.dk()
print("linear_speed= {}\nrotation_speed= {}".format(linear_speed, rotation_speed))
if (linear_speed ):
	print ("test_3 OK\n")
else:
	print ("nok\n")


