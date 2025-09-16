class  Towel:
    def __init__(self, color: str, size: str):  #construtor
        self.color: str = color #atributos
        self.size: str = size
        self.wetness: int = 0
#como são criada

    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum:{self.wetness}" 



#referencia
towel = Towel("green", "G") #objeto
toalha = Towel ("red", "p") 
outra = toalha
mais_outras = toalha
toalha.color ="blue"
outra.color = "blue"


print(towel.color) #vermelha
towel.color = "white"
print(towel.color)#branco
print(towel.size)
print(towel.wetness)


