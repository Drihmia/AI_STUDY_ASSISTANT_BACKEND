# -*- coding: utf-8 -*-

princie_d_inertie_tc_pc = """
# Document: Principe d'inertie - Leçon Consolidée

## I. Mise en évidence expérimentale du principe d'inertie

### 1. Expérience 1: Mouvement rectiligne uniforme

On utilise un autoporteur équipé de deux éclateurs, le premier (A) fixé sur son axe de symétrie Δ et le deuxième (M) en un point de sa périphérie.  L'autoporteur est lancé sur une table horizontale à coussin d'air, minimisant les frottements.  On enregistre les positions des points A et M pendant un mouvement de translation sans rotation.

**(Diagram Description: Diagram showing an autoporteur setup with points A and M, axis of symmetry Δ, and recording apparatus)**

**(Diagram Description:  Enregistrement des points M et A montrant des lignes droites parallèles et équidistantes, indiquant un mouvement rectiligne uniforme)**

τ = 40ms
M₀   M₁   M₂   M₃   M₄
•    •    •    •    •
A₀   A₁   A₂   A₃   A₄
:    •    •    •    •

### 2. Expérience 2: Mouvement avec rotation

On répète l'expérience, mais en lançant l'autoporteur de manière à induire une rotation en plus de la translation.  On observe l'enregistrement des points A et M.

**(Diagram Description: Enregistrement des points M et A montrant des lignes courbes pour M et une ligne droite pour A, indiquant un mouvement avec rotation autour de A)**

τ = 40ms
M₃    M₂    M₁    M₀
•     •     •     •
     A₃ A₂ A₁ A₀
          •  •  •  •

### 3. Conclusion: Le mouvement du centre d'inertie est rectiligne uniforme

- Dans les deux expériences, le mouvement du point A, situé sur l'axe de symétrie Δ, est rectiligne et uniforme.  Ceci est également vrai pour tous les points de l'axe Δ.
- Même si l'autoporteur tourne (Expérience 2), le mouvement de l'axe Δ (et donc du point A) reste rectiligne uniforme.
- Le point d'intersection des axes Δ et Δ' (lorsqu'on considère différentes orientations de l'autoporteur) définit le centre d'inertie G.

**(Diagram Description: Diagram illustrating the center of inertia G as the intersection of axes Δ and Δ')**


## II. Principe d'inertie: Système isolé et pseudo-isolé

### 1. Système isolé et pseudo-isolé

*   **Système isolé:** Un système mécaniquement isolé n'est soumis à aucune force extérieure.  En réalité, un système parfaitement isolé n'existe pas.
*   **Système pseudo-isolé:** Un système est pseudo-isolé si la somme vectorielle des forces extérieures qui s'exercent sur lui est nulle (∑ (vecteur F) = (Vecteur 0)).  Dans ce cas, les effets des forces extérieures se compensent.

**Exemples:**

*   **Système isolé (idéalisation):** Un astronaute dans l'espace intersidéral, loin de toute étoile ou planète, peut être considéré comme isolé (en négligeant les forces gravitationnelles minimes).
*   **Système pseudo-isolé (approximativement):** Un autoporteur sur une table à coussin d'air horizontale, une fois la soufflerie démarrée, est pseudo-isolé car le poids (Vecteur P) et la réaction du support (Vecteur R) se compensent: (Vecteur P) + (Vecteur R) = (Vecteur 0).

**(Diagram Description: Diagram of forces P and R in equilibrium on an autoporteur,(Vecteur P) + (Vecteur R) = (Vecteur 0))**

(Vecteur P) + (Vecteur R) = (Vecteur 0)
(Vecteur R) = - (Vecteur P)
R = P = mg

### 2. Énoncé du principe d'inertie:

Dans un référentiel galiléen, le centre d'inertie G d'un système isolé ou pseudo-isolé est :

*   **Soit au repos:** si sa vitesse initiale est nulle (vecteur VG = (Vecteur 0)).
*   **Soit en mouvement rectiligne uniforme:** si sa vitesse initiale est non nulle (vecteur VG = (Vecteur Cte)).

En résumé, en l'absence de forces extérieures ou lorsque les forces extérieures se compensent (∑(vecteur F) = (Vecteur 0)), le centre d'inertie d'un système conserve son état de mouvement (repos ou mouvement rectiligne uniforme).

**Remarques:**

*   Le principe d'inertie s'applique uniquement dans les référentiels galiléens (ou référentiels inertiels), comme le référentiel de Copernic ou, en approximation pour les durées courtes, le référentiel terrestre.
*   Seul le centre d'inertie d'un système isolé ou pseudo-isolé obéit au principe d'inertie. Les autres points du système peuvent avoir des mouvements différents (mouvement propre).

### 3. Inertie: l'inertie d'un système est la résistance qu'un corps oppose à un changement de son état de mouvement.  Cette inertie est liée à la masse du corps; plus cette dernière est grande, plus l'inertie est élevée.
## III. La relation barycentrique et le centre d'inertie

### 1. Définition du centre d'inertie pour un corps solide

Le centre d'inertie G d'un système (S) constitué de points matériels A₁, A₂, A₃, ..., A<0xE2><0x99><0x99> de masses respectives m₁, m₂, m₃, ..., m<0xE2><0x99><0x99> est défini par la relation vectorielle:

∑mᵢ * (vecteur GAᵢ) = (Vecteur 0)

Cette relation signifie que la somme des moments des masses par rapport au centre d'inertie est nulle.

**(Diagram Description: Diagram of system (S) with points A1, A2, center of inertia G, and coordinate system (O,x,y))**


En introduisant un point origine O quelconque, on peut exprimer la position du centre d'inertie G par la relation barycentrique:

vecteur OG = (∑mᵢ (vecteur OAᵢ)) / (∑mᵢ)

Où :
*   ∑mᵢ * (vecteur OAᵢ) est la somme vectorielle des produits de chaque masse mᵢ par le vecteur position (vecteur OAᵢ).
*   ∑mᵢ est la masse totale du système.

### 2. Exemples de centres d'inertie

**(Diagram Description: Four diagrams showing the center of inertia G at the geometric center for a square, circle, cylinder, and cube)**


### 3. Exercice d'application: Calcul du centre d'inertie d'un système de deux boules

Considérons un système de deux boules (S₁ et S₂) de masses respectives m₁ et m₂ = 2m₁, reliées par une liaison rigide, avec leurs centres d'inertie G₁ et G₂ distants de G₁G₂ = 90cm.  Déterminons le centre d'inertie G du système (S₁+S₂).

**(Diagram Description: Diagram of two spheres S1 and S2, their centers G1 and G2, connected by a rigid link, and the center of inertia G of the system)**


**Solution:**

En appliquant la relation barycentrique avec l'origine O confondue avec G₁, on obtient la position du centre d'inertie G par rapport à G₁:

(vecteur GG₁) = (m₂. (vecteur G₁G₂)) / (m₁ + m₂) = (2m₁.(vecteur G₁G₂)) / (3m₁) = (2/3)(vecteur G₁G₂)
Puisque les vecteurs vecteur G₁G etvecteur GG₁ sont colinéaires, on peut déterminer la distance GG₁:
GG₁ = (2/3) * G₁G₂ = (2/3) * 90cm = 60cm

Le centre d'inertie G du système (S₁+S₂) est situé à 60cm de G₁, sur le segment [G₁G₂], entre G₁ et G₂.

**(Diagram Description: Diagram illustrating the position of G relative to G1 and G2 and the distance GG1)**

---

# Document: Principe d'inertie - Effets des forces sur les mouvements (Complément)

## Effets des forces sur les mouvements

| Influence d'une force sur la vitesse d'un solide                | Influence d'une force sur la trajectoire d'un solide.           | Influence d'une force sur la trajectoire et la vitesse d'un solide             |
| :------------------------------------------------------------ | :------------------------------------------------------------ | :-------------------------------------------------------------------------------- |
| Elle peut modifier la valeur de la vitesse du système.        | Elle peut modifier la trajectoire du système                  | Elle peut modifier la trajectoire et la valeur de la vitesse du système             |
| **(Image Description: Image of a falling object illustrating gravity - Chute)** | **(Image Description: Image of a ball curving towards a magnet illustrating magnetic force - aimant)** | **(Image Description: Image of a ball hitting a barrier illustrating force changing direction and speed - Barrière)** |
| **Chute**                                                     | **aimant**                                                      | **Barrière**                                                                     |

**Remarque: Influence de la résultante des forces sur le mouvement**

| Résultante des forces exercées sur l'objet :                                                                     | Influence sur le mouvement                                                                                 |
| :------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| La somme des forces exercées sur l'objet est non nulle et est parallèle au vecteur vitesse de mouvement.       | Mouvement rectiligne (modification de la vitesse).                                                            |
| La somme des forces exercées sur l'objet est non nulle et est perpendiculaire au vecteur vitesse de mouvement. | Mouvement circulaire (modification de la direction du mouvement).                                          |

### Centre d'inertie et principe d'inertie

#### 1. Système isolé: absence de force

Un système est mécaniquement **isolé** s'il n'est soumis à **aucune force extérieure**.  Ce cas est théorique.

#### 2. Système pseudo-isolé: forces compensées

Un système est **pseudo-isolé** si les effets des forces extérieures auxquelles il est soumis se compensent (∑ (vecteur F) = (Vecteur 0)).


#### 3. Mouvement du centre d'inertie d'un solide pseudo-isolé: rectiligne uniforme

Lorsqu'on lance un solide autoporteur pseudo-isolé en rotation sur une table à coussin d'air horizontale, on observe qu'un seul point, le centre d'inertie G, se déplace en ligne droite à vitesse constante.

**(Diagram Description: Diagram of trajectory points of a rotating autoporteur, showing point A (center of inertia G) moving in a straight line while other points follow curved paths)**

A
τ=40ms
• • • • • • • • • • • ... (Trajectory points indicating straight line motion)

**Remarque:** Dans les exemples étudiés, le centre d'inertie coïncide avec le centre de gravité.  Pour un système pseudo-isolé, le mouvement du centre d'inertie G est rectiligne uniforme.

## IV. Principe d'inertie: Énoncé et référentiels

### 4. Principe d'inertie: Énoncé

Dans un référentiel galiléen, lorsqu'un solide est isolé ou pseudo-isolé (∑(vecteur F) = (Vecteur 0)), son centre d'inertie G :

*   reste immobile si sa vitesse initiale est nulle ((vecteur VG) = (Vecteur 0)).
*   est animé d'un mouvement rectiligne uniforme si sa vitesse initiale est non nulle ((vecteur VG) = (Vecteur Cte)).

Formulation mathématique:  ∑(vecteur F) = (Vecteur 0)  <=> (vecteur VG) = (Vecteur Cte)

### 5. Référentiels galiléens

Le principe d'inertie n'est valable que dans des **référentiels galiléens** (ou inertiels).  On considère comme référentiels galiléens :

*   Le référentiel de Copernic (référentiel héliocentrique).
*   Avec approximation, le référentiel terrestre (pour les expériences de courte durée).
*   Tout référentiel en translation rectiligne uniforme par rapport à un référentiel galiléen.

## V. Centre d'un système matériel: Centre de masse et relation barycentrique

### 1. Centre de masse d'un système matériel

Le centre de masse d'un système matériel est le barycentre de l'ensemble des points matériels qui le constituent.  Pour un système de points matériels pondérés Aᵢ de masses mᵢ, le centre de masse C est défini par la relation:

∑ mᵢ * (vecteur CAᵢ) = (Vecteur 0)

### 2. Relation barycentrique pour le centre de masse G

Pour un système composé de corps solides homogènes (Sᵢ) de centres de masse Gᵢ et de masses mᵢ, la position du centre de masse G du système est donnée par la relation barycentrique:

(vecteur OG) = (∑mᵢ.(vecteur OGᵢ)) / (∑mᵢ)

Où O est un point quelconque de l'espace.  Le centre de masse G coïncide avec le centre d'inertie et le centre de gravité pour les systèmes étudiés.

**Clarification importante:**

*   Ce document se concentre sur le **principe d'inertie** et non sur les lois de Newton en général. Bien que le principe d'inertie soit historiquement la première loi de Newton, le document est structuré pour présenter ce principe de manière autonome, sans référence explicite à "Newton" ou à "première loi" sauf pour le contexte historique.

--- Fin de la Leçon ---
"""

