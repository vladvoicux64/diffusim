import math
from scipy.special import erfinv


def medium_distance():
    """
    Distanta medie teoretica
    """
    return 0


def medium_position():
    """
    Pozitie medie teoretica
    """
    return (0, 0)


def medium_step(sigma):
    """
    Media lungimii pasilor
    sigma: deviatia standard a componentele vectorului
    """
    return sigma * math.sqrt(math.pi / 2)


def standard_dev_step(sigma):
    """
    Deviatia standard a pasului
    sigma: deviatia standard a componentelor vectorului
    """
    return math.sqrt((4 - math.pi) / 2 * sigma ** 2)


def SE(n, sigma):
    """
    Eroarea standard
    n: Numarul de simulari
    sigma: Deviatia standard a v.a.
    """
    return math.sqrt(n) * sigma


def SEM(n, sigma):
    """
    Eroarea standard a mediei
    n: Numarul de simulari
    sigma: Deviatia standard a v.a.
    """
    return sigma / math.sqrt(n)


def normal_quantile(mean, sigma, p):
    """
    Cuantila normala
    mean: Media distributiei
    sigma: Deviatia standard a distributiei
    p: Percentila
    """
    return float(mean + sigma * math.sqrt(2) * erfinv(2 * p - 1))


def error_confidence_interval(n, mean, sigma, alpha):
    """
    Intervalul de incredere
    n: Numarul de simulari
    mean: Media distributiei
    sigma: Deviatia standard a distributiei
    alpha: Nivel de semnificatie
    """
    z = normal_quantile(mean, sigma, 1 - alpha / 2)
    return (-z * SEM(n, sigma), z * SEM(n, sigma))


def num_sim_for_conf_level_with_error(mean, sigma, alpha, epsilon):
    """
    Numarul de simulari necesar pentru a obtine un anumit nivel de incredere cu
    o anumita eroare
    mean: Media distributiei
    sigma: Deviatia standard a distributiei
    alpha: Nivelul de semnificatie
    epsilon: Modulul erorii
    """
    z = normal_quantile(mean, sigma, 1 - alpha / 2)
    return math.ceil(z ** 2 * sigma ** 2 / epsilon ** 2)


def print_theoretical_stats(num_sim, num_steps, sigma_vector_component, epsilon, alpha):
    """
    Afisarea tuturor datelor calculate
    nim_sim: Numarul de simulari
    num_steps: Numarul de pasi per simulare
    sigma_vector_component: Deviatia standard a componentelor vectorului de
    miscare
    epsilon: Modulul erorii
    alpha: Nivelul de semnificatie
    """
    sigma_step = standard_dev_step(sigma_vector_component)
    sigma_dist = math.sqrt(num_steps) * sigma_step
    print("Valori teoretice pentru variabilele simulate:")
    print(f"Pozitia medie finala: {medium_position()}")
    print(f"Distanta medie a centrului de masa fata de origine: {
          medium_distance()}")
    print(f"Marimea medie a pasului: {medium_step(sigma_vector_component)}")
    print(f"Deviatia standard a distantelor finale: {sigma_dist}")
    print(f"Numarul de simulari pentru a obtine eroare in modul de {epsilon} cu o probabilitate de {
          alpha * 100}%: {num_sim_for_conf_level_with_error(0, sigma_dist, alpha, epsilon)}")
    print(f"Intervalul de incredere obtinut cu {num_sim} de simulari si nivel de incredere {
          1 - alpha}: {error_confidence_interval(num_sim, 0, sigma_dist, alpha)}")
    print('\n')
