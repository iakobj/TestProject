class Enemy:
    def __init__(self, health, strength, defence, name):
        self.health = health
        self.strength = strength
        self.defence = defence
        self.name = name

# Velites – A class of light infantry in the army of the Roman Republic.
Velites = Enemy(100, 50, 30, "Velites")

# Quaestionarius – An interrogator or torturer.
Quaestionarius = Enemy(300, 100, 70, "Quaestionarius")

# Legionary – The heavy infantry that was the basic military force of the ancient
# Roman army in the period of the late Roman Republic and the Roman Empire.
Legionary = Enemy(450, 180, 200, "Legionary")

# Speculatores and Exploratores – The scouts and reconnaissance element of the Roman army.
Speculatores = Enemy(80, 30, 20, "Speculatores")


