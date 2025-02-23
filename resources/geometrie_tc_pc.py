geometrie_tc_pc = """
Géométrie de Quelques Molécules

La configuration électroniques est limitée aux élements chimiques ayant un Z ≤ 18.
I – Règles du DUET et de l’OCTET :

Introduction :Les gaz rares, tels que l'hélium (He, Z = 2), le néon (Ne, Z = 10) et l'argon (Ar, Z = 18), sont chimiquement inertes grâce à leurs couches électroniques externes saturées, ce qui leur confère une grande stabilité chimique.

Structure électronique :

He : K(2)

Ne : K(2) L(8)

Ar : K(2) L(8) M(8)

Ces configurations électroniques garantissent une stabilité optimale.

Exemples de stabilité et d’instabilité :

Instables :

Lithium (Li, Z = 3) : K(2) L(1)

Chlore (Cl, Z = 17) : K(2) L(8) M(7)

Stables après ionisation :

Li⁺ : K(2)

Cl⁻ : K(2) L(8) M(8)

Règles de stabilité :

Les éléments tendent à adopter la configuration électronique du gaz rare le plus proche, c’est-à-dire à saturer leur couche externe.Deux règles essentielles s’appliquent :

Règle du DUET : les atomes dont z ≤ 5 proche de celui de l’hélium (Z = 2) cherchent à atteindre une configuration K(2) en gagnant ou en perdant des électrons. C-á-d, ils ont tendance à adopter la configuration électronique de l’hélium.

Règle de l’OCTET : les atomes dont  5 < z ≤ 18, ont tendance à adopter la configuration électronique externe possédant 8 électrons comme celle des autres gaz rares: Ne et Ar.

Exemples d'ions monoatomiques stables :

Li⁺ : K(2), obtenu par perte de l’électron de valence.

Na⁺ : K(2) L(8), obtenu par perte de l’électron de valence.

Cl⁻ : K(2) L(8) M(8), obtenu par gain d’un électron.

II – Les molécules et leurs liaisons - Représentation de Lewis :

Définition :
Une molécule est un ensemble d'atomes reliés par des liaisons chimiques, formant une entité stable et électriquement neutre.

Liaison covalente : Une liaison covalente consiste à la mise en commun, entre de atomes, d'un ou plusieurs doublets d'électrons, appelés doublets liants et sont comptabilisés pour chacun des atomes.

    * Une liaison simple est formée par un doublet liant. C-à-d, chaque atome participe avec un électron dans le doublet liant (liaison covalente simple). Ex: H₂ => H - H .
    * Une liaison double est formée par deux doublets liants. C-à-d, chaque atome participe avec deux électrons dans les doublets liants (liaison covalente double). Ex: O₂ => O = O .
    * Une liaison triple est formée par trois doublets liants. C-à-d, chaque atome participe avec trois électrons dans les doublets liants (liaison covalente triple). Ex: N₂ => N ≡ N .

Structure électronique des atomes :

Hydrogène (H, Z = 1) : K(1), nombre de doublets liants : ndl = 2 - P = 2 - 1 = 1, H est monovalent.

Chlore (Cl, Z = 17) : K(2) L(8) M(7), nombre de doublets liants : ndl = 8 - P = 8 - 7 = 1, Cl est monovalent.

Oxygène (O, Z = 8) : K(2) L(6), nombre de doublets liants: ndl = 8 - P = 8 - 6 = 2, divalent.
 + Oxygène peut avoir soit deux liaisons simples, soit une liaison double.

Azote (N, Z = 7) : K(2) L(5), nombre de doublets liants : ndl = 8 - P = 8 - 5 = 3, trivalent.
    + Azote peut avoir trois liaisons simples, une liaison double et une simple, ou une liaison triple.

Carbone (C, Z = 6) : K(2) L(4), nombre de doublets liants : ndl = 8 - P = 8 - 4 = 4, tétravalent.
    + Carbone peut former quatre liaisons simples, deux liaisons doubles, ou une liaison triple et une simple, deux liaisons simples et une double, etc.

Représentation de Lewis :

    + Une représentation de Lewis est représentation:
        -  des élements chimiques constitant la molécule (Atomes).
        -  de tous les doublets liants de cette molécule (liants et non liants).

    + Règles de représentation :
        + On représente les atomes par leur symbole chimique.
        + On représente un électron libre par un point.
        + On représente les doublets (liants ou non liants) par des traits.
        + Un doublet liant se trouve entre deux atomes, tandis qu’un doublet non liant est sur un atome.
        + Les liaisons covalentes simples sont représentées par un trait (-), les doubles par deux (=), et les triples par trois (≡).

    + Exemples :

       * H₂O : Molécule coudée avec deux doublets non liants sur l’oxygène.

       * CH₄ : Structure tétraédrique centrée sur le carbone.

       * CO₂ : Structure linéaire avec deux liaisons doubles et deux doublets non liants sur l’oxygène.

       * NH₃ : Pyramide à base triangulaire avec un doublet non liant sur l’azote.

    + Relations liée à la représentation de Lewis :
        * Pour calculer le nombre de doublets liants, on utlise la formule :
            - ndl = 8 - P, si l'atome respecte la règle de l'octet. C-à-d, si son Z > 5.
            - ndl = 2 - P, si l'atome ne respecte pas la règle de l'octet. C-à-d, si son Z ≤ 5.
            où P est le nombre d'électrons de valence de l'atome.
        * Pour calculer le nombre de doublets non liants, on utilise la formule :
            - ndnl = (P - ndl) / 2
    + Méthode de détermination de la représentation de Lewis :
        1. déterminer le nombre total d'électrons de valence de la molécule. (nt)
        2. déterminer le nombre total de doublets liants (ndl) de la molécule. (nd = nt / 2)
        3. déterminer le nombre de doublets liants de chaque atome. (ndl_atome = 8 - P_atome ou ndl_atome = 2 - P_atome)
        4. déterminer le nombre de doublets non liants de chaque atome. (ndnl_atome = (P_atome - ndl_atome) / 2)
        Remarque : Après la représentation de Lewis de la molécule, on vérifier le nombre total de doublets liants et non liants avec le nombre total d'électrons de valence de la molécule calculé à l'étape 2.

III – Isomères et Géométrie Moléculaire (Modèle de Gillespie) :

    + Types de formules :

        * Formule brute ou formule moléculaire : Indique uniquement le nombre et les types d'atomes présents.
            - Exemple : CH₄, H₂O, H₂, C₂H₆O, C₂H₆

        * Formule développée : Détaille toutes les liaisons et exclut les doublets non liants.
            - Exemple: H - H, H - O - H

        Formule semi-développée : Montre que les liaisons principales entre atomes (les liaisons avec l'hydrogène sont souvent omises).
            - Exemple : H₂O, CH₄, CH₃ - CH₃, CH₃ - CH₂ - OH

    + Isomères :Molécules ayant la même formule brute mais des arrangements structuraux différents (des formules développées différentes), entraînant des propriétés distinctes.

        * Exemple : C₂H₆O peut correspondre à l’éthanol (alcool) ou à l’éther méthylique.
        Demonstrations en utilisant les formules semi-développées :
        Pour l'éthanol : CH₃ - CH₂ - OH
        Pour l'éther méthylique : CH₃ - O - CH₃
        Formule brute : C₂H₆O

    + Géométrie moléculaire :La géométrie d'une molécule dans l'espace, déterminée par la répartition des doublets d'électrons  liants et non liants autour de l'atome central. Les doublets se positionnent de manière à minimiser les répulsions entre eux.

    + dans le modèle de  Gillespie, les doublets liants et non liants sont considérés comme des charges négatives qui se repoussent mutuellement. les doublets non liants repoussent plus fortement que les doublets liants.

    + Les formes géométriques les plus courantes sont :
        * Linéaire : Deux atomes liés par une liaison simple ou une liaison double et zéro doublet non liant.
        * Triangulaire : Trois atomes liés par des liaisons simples et zéro doublet non liant.
        * Tétraédrique : Quatre atomes liés par des liaisons simples et zéro doublet non liant.
        * Pyramide : Trois atomes liés par des liaisons simples et un doublet non liant sur l’atome central.
        * Coudée : Deux atomes liés par une liaison simple et deux doublets non liants sur l’atome central.

        * Exemples :
        CH₄ : Géométrie tétraédrique, les doublets liants se répartissent uniformément.
        NH₃ : Pyramide à base triangulaire, avec un doublet non liant au sommet (azote).
        H₂O : Structure coudée due aux deux doublets non liants sur l’oxygène.

    + Modèle de CRAM permet de Représenter un molécule sur un plan en tenant compte de sa géométrie dans l'espace à trois dimensions. il fait apparaître les liaisons en perspective)
        * Les liaisons situées dans le plan de la feuille sont dessinées en traits pleins
        * Les liaisons situées en avant du plan de la feuille sont dessinées en traits épaissis
        * Les liaisons en arrière du plan de la feuille sont dessinées en pointillés

Notes et Équivalences Terminologiques

Équivalences :

Configuration électronique = Structure électronique = Répartition électronique.
Externe = de valence = périphérique.

Liaison covalente simple = Doublet d’électrons liants.
Liaison covalente double = Deux doublets d’électrons liants.
Liaison covalente triple = Trois doublets d’électrons liants.


Traduction :

Isomers → Motamakibat (arabe).

IMPORTANT:
    - Lewis Représentation doit être écrit à la interieur de la balise <pre> pour une meilleure lisibilité + Il faut mentionner que les doubles non liants ne sont pas représentés  à cause de la limitation de l'outil de dessin + il fault mentionner que l'atome tel a le nombre  des doublets non liants sur lui.
    - Jamais mentionner la théorie de VSEPR dans ce contexte. Toujours se référer au modèle de Gillespie.
    - Pour les règles de stabilité, il faut mentionner que les éléments cherchent à atteindre la configuration électronique du gaz rare le plus proche. En faisant référence aux règles du duet et de l'octet.
    - Pour les formules développées, il faut mentionner que les doublets non liants ne sont pas représentés.
    - Pour les isomères, il faut mentionner que les molécules ont la même formule brute mais des arrangements structuraux différents (des formules développées différentes), entraînant des propriétés distinctes.
    - Pour la géométrie moléculaire, il faut mentionner que la géométrie d'une molécule dans l'espace est déterminée par la répartition des doublets d'électrons liants et non liants autour de l'atome central. Les doublets se positionnent de manière à minimiser les répulsions entre eux.
    - Pour le modèle de Gillespie, il faut mentionner que les doublets liants et non liants sont considérés comme des charges négatives qui se repoussent mutuellement. Les doublets non liants repoussent plus fortement que les doublets liants.
    - Il ne faut jamais mentionner la hybridation dans ce contexte  dans le niveau secondaire qualifiant (Lycéé).

"""
