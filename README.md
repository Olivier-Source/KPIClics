Dans ce petit script, en python, vous avez une simulation de clics aléatoires, à des endroits aléatoires de votre écran pour empêcher la traque de votre activité via des KPI Clics, par exemple en ESN.

La fonction get_random_clics() génère un nombre aléatoire de clics à effectuer.
La fonction get_random_interval() génère des temps de latences aléatoires.
La fonction simulate_mouse_clicks() génère les déplacements et les clics.

la variable duration est définie à 600 secondes, correspondant à 10 minutes pour que l'execution du script dure 10 minutes, pendant lesquels vous pouvez prendre un café.

À chaque itération de la boucle, la fonction get_random_clics() est appelée pour déterminer le nombre aléatoire de clics à simuler. 
Ensuite, la fonction simulate_mouse_clicks() est appelée pour simuler les clics avec l'intervalle irrégulier spécifié.

Assurez-vous d'adapter les valeurs min_interval et max_interval dans get_random_clics() en fonction de vos besoins, et ajustez la résolution de l'écran dans les appels à random.randint(0, 1920) et random.randint(0, 1080) selon votre propre configuration.

N'hésitez pas à ajuster la durée de la boucle.
