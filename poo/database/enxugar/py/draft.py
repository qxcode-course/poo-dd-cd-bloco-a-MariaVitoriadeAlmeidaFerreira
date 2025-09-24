class Towel: #this
    def __init__(self, color: str, size: str):  #construtor
        self.color: str = color #atributos
        self.size: str = size
        self.wetness: int = 0
        #como são criada

    def dry(self, amount: int ) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print ("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def getMaxWetness(self) -> int:
        #maximo de agua
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def __str__(self): #toString
            return f"cor: {self.color}, tamanho: {self.size}, Umidade: {self.wetness}" 
    

def main():
  toalha = Towel("", "") #3. objeto manipulado
  while True: #4 loop infinito
      line: str = input()
      #print("$" + line) 
      args: list[str] = line.split(" ")
      if args[0] == "end":
        break
      elif args[0] == "criar":
          color = args[1]
          size = args[2]
          toalha = Towel(color, size)

      elif args[0] == "mostrar":
          print(toalha)
      elif args[0] == "dry":
          amount: int = int(args[1])
          toalha.dry(amount)
      else:
          print("fail")
  
main()



