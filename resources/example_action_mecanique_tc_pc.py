# -*- coding: utf-8 -*-

example_action_mecanique_tc_pc = """
# Document: Actions Mécaniques - Consolidated Lesson

## I. Introduction aux Actions Mécaniques

### 1. Notion d'Action Mécanique

Lorsqu'un corps agit sur un autre corps, on parle d'**action mécanique**.  Chaque action mécanique est identifiée par **son effet** sur le corps qui la subit.

Une action mécanique peut:

*   Provoquer le mouvement d'un corps.
*   Arrêter le mouvement d'un corps.
*   Changer la direction du mouvement d'un corps.
*   Maintenir un corps en équilibre.

Toute action mécanique est modélisée par une **force**.

### 2. Types d'Actions Mécaniques

Il existe deux types principaux d'actions mécaniques :

*   **Actions Mécaniques de Contact:**  Nécessitent un contact physique direct entre le corps exerçant l'action (l'acteur) et le corps la subissant (le receveur).
    *   **Localisées:**  S'exercent sur une très petite surface, idéalement un point.  *Exemple: Contact d'un fil sur un corps.*
    *   **Réparties:** S'exercent sur une surface étendue. *Exemple: Contact d'une table sur un livre.*
*   **Actions Mécaniques à Distance:** S'exercent sans contact physique direct entre les corps. *Exemple: Force gravitationnelle, force magnétique.*

## II. La Force: Caractéristiques et Représentation

### 1. Définition de la Force

Une **force** est une grandeur physique vectorielle qui modélise une action mécanique.  Elle est caractérisée par quatre éléments:

*   **Point d'Application:**  L'endroit où la force s'exerce sur le corps.
*   **Direction (ou Ligne d'Action):** La droite le long de laquelle la force agit.
*   **Sens:**  L'orientation de la force le long de sa direction.
*   **Intensité (ou Valeur):**  La magnitude de la force, mesurée en Newton (N). L'intensité peut être mesurée à l'aide d'un **dynamomètre**.

### 2. Représentation d'une Force

Une force est représentée graphiquement par un **vecteur**, c'est-à-dire une flèche.

*   **Origine de la flèche:**  Correspond au point d'application de la force.
*   **Direction de la flèche:**  Indique la direction de la force.
*   **Sens de la flèche:**  Indique le sens de la force.
*   **Longueur de la flèche:**  Est proportionnelle à l'intensité de la force (une échelle est nécessaire pour la représentation).

**Exemple de Représentation:** Force (Vecteur F) exercée par un fil sur un corps (S).  Si l'intensité de la force est de 2N et que l'on choisit une échelle de 1cm pour 1N, la force sera représentée par une flèche de 2cm de long.

## III. Classification et Exemples de Forces

### 1. Forces de Contact

#### a) Tension d'un Fil (Vecteur T)

*   **Définition:** Force de contact exercée par un fil tendu sur un solide auquel il est accroché.
*   **Point d'Application:** Point d'accrochage du fil sur le solide.
*   **Direction:**  Le long du fil.
*   **Sens:**  Du point d'accrochage vers le support du fil.
*   **Intensité:**  Notée T, exprimée en Newton.

#### b) Tension d'un Ressort (Vecteur T)

*   **Définition:** Force exercée par un ressort sur un solide auquel il est accroché, lorsque le ressort est étiré ou comprimé.
*   **Point d'Application:** Point d'accrochage du ressort sur le solide.
*   **Direction:**  Selon l'axe du ressort.
*   **Sens:**  Vers la position d'équilibre du ressort.
*   **Intensité:** Notée T, exprimée en Newton.

#### c) Réaction du Plan de Contact (Vecteur R)

*   **Définition:** Force de contact répartie exercée par un support (plan) sur un solide en contact avec lui.
*   **Point d'Application:** Centre de la surface de contact.
*   **Direction:**
    *   **Sans Frottement:** Perpendiculaire au plan de contact.
    *   **Avec Frottement:**  Inclinée par rapport à la normale au plan, décomposable en:
        *   **Composante Normale (RN):** Perpendiculaire au plan.
        *   **Composante Tangentielle (RT):** Force de frottement, parallèle au plan.  (Vecteur R) = RN + RT
*   **Sens:** Du support vers le solide.
*   **Intensité:**  R = √(RN² + RT²)

### 2. Forces à Distance

*   **Force Gravitationnelle (Poids - Vecteur P):** Force d'attraction universelle exercée par la Terre sur tout corps ayant une masse.
*   **Forces Électrostatiques:** Forces entre charges électriques.
*   **Forces Magnétiques:** Forces exercées par des aimants ou des courants électriques.

## IV. Force Pressante et Pression

### 1. Force Pressante

La **force pressante** est une force de contact répartie exercée par un fluide (gaz ou liquide) sur une surface.  Elle est toujours perpendiculaire à la surface. *Exemple: Force exercée par l'air sur la paroi d'un ballon.*

**Caractéristiques:**

*   **Point d'Application:** Réparti sur la surface de contact, résultante au centre de la surface.
*   **Direction:** Perpendiculaire à la surface.
*   **Sens:** Du fluide vers le corps.
*   **Intensité:** Dépend de la pression du fluide et de la surface de contact.

### 2. Pression

La **pression (P)** est définie comme le quotient de l'intensité de la force pressante (F) par l'aire de la surface pressée (S):

**P = F / S**

*   **Unité SI de Pression:** Pascal (Pa), où 1 Pa = 1 N/m².
*   **Autres Unités:** Hectopascal (hPa), Bar (bar), Atmosphère (atm), Centimètre de Mercure (cm Hg).

**Pression Atmosphérique:**  La pression atmosphérique est la pression exercée par l'air de l'atmosphère. Elle diminue avec l'altitude et sa valeur normale au niveau de la mer est d'environ 101325 Pa (1 atm).

**Mesure de la Pression:**

*   **Manomètre:** Instrument utilisé pour mesurer la pression des gaz.
*   **Baromètre:** Instrument utilisé pour mesurer la pression atmosphérique.

## V. Forces Extérieures et Intérieures

*   **Force Extérieure:** Force exercée sur une partie du système par un élément **extérieur** au système.
*   **Force Intérieure:** Force exercée entre **deux parties appartenant au même système**.

**Exemple: Système {Corps C + Fil}**

*   La tension du fil sur le corps C devient une **force intérieure** au système {Corps C + Fil}.
*   L'action de la Terre sur le corps C (le poids) reste une **force extérieure** au système {Corps C + Fil}, car la Terre ne fait pas partie de ce système.

--- End of Consolidated Lesson ---
"""
