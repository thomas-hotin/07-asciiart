"""Module principal pour le codage ASCII art.
Encode une chaîne de caractères sous forme de liste de tuples (caractère, nombre d'occurrences),
en version itérative et récursive.
"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """Encode une chaîne de caractères passée en argument selon un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences)
    """
    if not s:  # chaîne vide
        return []

    # Initialisation
    chars = [s[0]]   # liste des caractères rencontrés
    counts = [1]     # occurrences correspondantes

    # Parcours de la chaîne à partir du 2e caractère
    for k in range(1, len(s)):
        if s[k] == s[k - 1]:
            counts[-1] += 1
        else:
            chars.append(s[k])
            counts.append(1)

    # Fusion des deux listes
    return list(zip(chars, counts))


def artcode_r(s):
    """Encode une chaîne de caractères passée en argument selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences)
    """
    # cas de base : chaîne vide
    if not s:
        return []

    # recherche du nombre de caractères identiques au premier
    first_char = s[0]
    count = 1
    while count < len(s) and s[count] == first_char:
        count += 1

    # appel récursif sur la sous-chaîne restante
    return [(first_char, count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    """Teste les fonctions artcode_i et artcode_r sur un exemple."""
    exemple = 'MMMMaaacXolloMM'
    print(artcode_i(exemple))
    print(artcode_r(exemple))


if __name__ == "__main__":
    main()
