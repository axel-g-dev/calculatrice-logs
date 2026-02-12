import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Démarrage du programme")

def addition(a, b):
    logging.info(f"Démarrage de l'addition de a={a} et b={b}")
    return a + b

def division(a, b):
    if b == 0:
        logging.error("Division par 0")
        return None
    logging.info(f"Démarrage de la division de a={a} et b={b}")
    return a / b

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
print("Résultat de l'addition :", resultat_addition)

resultat_division = division(x, y)
if resultat_division is not None:
    print("Résultat de la division :", resultat_division)
else:
    print("Division impossible")

logging.info("Fin du programme")