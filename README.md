# Sematic-web

= Sujet de TP noté NTriples

Vous devrez écrire, dans l'un des langages proposés ci-desssous, un parseur capable de lire des fichiers contenant des données N-triples représentées sous forme canonique :

- un triplet par ligne,
- chaque triplet est de la forme "s p o .", où s est un sujet, p, un prédicat, o un objet, chacun séparé par une seule espace,
et avec une espace et un point pour terminer la ligne,
- les sujets sont soit des URIs entre chevrons, soit des noeuds anonymes,
- les prédicats sont des URIs entre chevrons,
- les objets sont soit des URIs entre chevrons, soit des noeuds anonymes, soit des littéraux,
- les littéraux sont des chaînes entre guillemets, pouvant éventuellement contenir des guillemets échappés (\"), et éventuellement suivis d'un type ou d'une annotation de langue,
- les types sont identifiés à l'aide de la séquence "^^" et suivis d'une URI,
- les annotations de langue sont identifiées à l'aide du caractère "@" et suivies d'un identifiant,
- il n'y a pas de commentaire dans le document,
- la dernière ligne peut être une ligne vide, ou non.

Lors de son exécution, votre programme se verra fourni en ligne de commande le nom d'un fichier, ainsi qu'une requête sous forme d'une chaîne de caractères. Cette chaîne contiendra trois champs, séparés chacun par une espace, représentant le sujet, le prédicat et l'objet. Pour le sujet et le prédicat, la valeur pourra être :

- une valeur littérale (URI ou noeud anonyme),
- le caractère "?" ayant valeur de joker.

Pour les objets, la valeur pourra être :

- une valeur littérale (URI, noeud anonyme, chaîne de caractère avec type ou annotation de langue éventuelles),
- le caractère "?" ayant valeur de joker,
- la séquence "?@" suivie d'une identifiant (par exemple, "?@fr") ayant valeur de joker, mais uniquement pour les objets ayant la bonne annotation.

Par exemple, la requête "? <http://www.w3.org/2000/01/rdf-schema#label> ?@fr" renverra tous les triplets ayant pour prédicat <http://www.w3.org/2000/01/rdf-schema#label> et pour objet une valeur littérale en langue "fr", quel que soit le sujet.

La requête "? ? ?" renverra tous les triplets.

L'ordre dans lequel les triplets sont affichés n'a pas d'importance.

Enfin, le programme affichera, *sur la sortie d'erreur*, le nombre de triplets affichés (par exemple "17 results").

Les langages de programmation autorisés sont les suivants :

- C,
- C++,
- Java,
- Javascript,
- Typescript,
- Python 3,
- Go.

Quel que soit le langage choisi, vous ne pourrez utiliser que les fonctionnalités disponibles dans la bibliothèque standard, sauf autorisation explicite.

== Critères d'évaluation

Votre programme sera testé sur des fichiers volumineux (plusieurs millions de triplets). Quatre requêtes différentes seront testées, valant chacune 5 points (5 points si le résultat obtenu est correct, 0 sinon).

La qualité du code source ne sera pas évaluée, en revanche, un programme trop lent ou consommant trop de ressource pourra donner lieu à une pénalité.

Afin de tester le bon fonctionnement de votre outil, vous pourrez utiliser le programme fourni par l'enseignant. Trouver des bugs dans ce programme pourra donner lieu à un bonus.
