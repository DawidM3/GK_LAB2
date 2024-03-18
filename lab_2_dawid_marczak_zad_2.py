import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
szerokosc = 400
wysokosc = 400
ekran = pygame.display.set_mode((szerokosc, wysokosc))

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
zolty = (255, 255, 0)

# Rysowanie tła
ekran.fill(bialy)

# Rysowanie czarnego koła
pygame.draw.circle(ekran, czarny, (szerokosc // 2, wysokosc // 2), 100)

# Rysowanie żółtego kwadratu
pygame.draw.rect(ekran, zolty, (szerokosc // 2 - 50, wysokosc // 2 - 50, 100, 100))

# Aktualizacja ekranu
pygame.display.update()

# Czekaj na zamknięcie okna
czekaj = True
while czekaj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            czekaj = False

pygame.quit()
