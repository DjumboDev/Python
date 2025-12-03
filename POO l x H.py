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
width = int(input("Enter a width : "))
height = int(input("Enter a height : "))
rectangle1 = Rectangle(width,height)
print(f"width = {rectangle1.get_largeur()}, height = {rectangle1.get_hauteur()}, and area = {rectangle1.get_surface()}")