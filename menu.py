
class Menu:
    def __init__(self):
        pass

    def main_menu(self):
        print("1 : choisir une catégorie")
        print("2 : Voir mes produits substitués")
        print("3 : réinitialiser la base de donnée")
        choice = ""
        while choice != "1" and choice != "2" and choice != "3":
            choice = input("Choisissez une option (si vous utilisez le programme pour la première fois, "
                           "réinitialisez la base de donnée avec le choix 3 : ")
        return choice

    def menu_category(self):
        choice = ""
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            choice = input("Choisissez une catégorie d'aliment : ")
        return choice

    def menu_products(self):
        choice = input("Choisissez un aliment que vous souhaitez substituer : ")


