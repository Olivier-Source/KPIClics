import pyautogui
import random
import time

# Fonction pour générer un intervalle irrégulier
def get_random_interval():
    min_interval = 1  # Intervalle minimum en secondes
    max_interval = 5  # Intervalle maximum en secondes
    return random.uniform(min_interval, max_interval)

# Fonction pour générer un nombre de clics irrégulier
def get_random_clics():
    min_interval = 1  # Intervalle minimum de clics
    max_interval = 3  # Intervalle maximum de clics
    return random.uniform(min_interval, max_interval)  

# Fonction pour simuler des clics de souris
def simulate_mouse_clicks(num_clicks):
    for _ in range(num_clicks):
        # Générer des coordonnées de clic aléatoires
        x = random.randint(0, 1920)  # Remplacez 1920 par la largeur de votre écran
        y = random.randint(0, 1080)  # Remplacez 1080 par la hauteur de votre écran
        
        # Déplacer la souris et cliquer
        pyautogui.moveTo(x, y, duration=0.2)  # Durée du déplacement de la souris
        pyautogui.click()
        
        # Attendre un intervalle irrégulier
        interval = get_random_interval()
        time.sleep(interval)

# Durée de la boucle en secondes
duration = 600  # 10 minutes

# Heure de début de la boucle
start_time = time.time()

while time.time() - start_time < duration:
    num_clicks = get_random_clics()
    simulate_mouse_clicks(num_clicks)
