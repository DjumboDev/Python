class Rectangle:

    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def get_surface(self):
        return self.hauteur * self.largeur
    
    def get_largeur(self):
        return self.largeur
    
    def get_hauteur(self):
        return self.hauteur

rectangle1 = Rectangle(16,15)
rectangle1.get_surface()
print(rectangle1.get_surface())