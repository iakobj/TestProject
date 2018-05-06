class enemy:
    def __init__(self, health, strength, defence):
        self.life = health
        self.strength = strength
        self.defence = defence

# Velites – A class of light infantry in the army of the Roman Republic.
Velites = enemy(100, 50, 30)

# Quaestionarius – An interrogator or torturer.
Quaestionarius = enemy(300, 100, 70)

# Legionary – The heavy infantry that was the basic military force of the ancient Roman army in the period of the late Roman Republic and the Roman Empire.
Legionary = enemy(450, 180, 200)

# Speculatores and Exploratores – The scouts and reconnaissance element of the Roman army.
Speculatores = enemy(80, 30, 20)


