siglos = ["XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI"]

print("Lista de siglos desde 1000 hasta 2000:")
anyactual = 1000
for siglo in siglos:
    print("año", anyactual, "- siglo", siglo)
    anyactual += 100
