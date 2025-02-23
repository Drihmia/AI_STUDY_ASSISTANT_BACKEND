equilibre_2_forces_tc_pc = """
# Document: Tension d'un ressort – Poussée d'Archimède

## I. Équilibre d'un corps solide sous l'action de deux forces

### 1. Expérience:

Réalisation de l'équilibre d'une plaque solide de poids P=0,1N à l'aide de deux dynamomètres D₁ et D₂.

**(Diagram Description: Diagram showing a solid plate suspended by two dynamometers D1 and D2. D1 and D2 read 7N each. Arrow F1 from D1 and F2 from D2 pointing upwards, and arrow P (weight) pointing downwards. Calculation F/P = 7N/0.1N = 70, F >> P)**

Les deux dynamomètres indiquent la même intensité F₁=F₂=7N.
Le poids de la plaque est négligeable devant l'intensité des deux forces, donc **la** plaque est en équilibre sous l'action de deux forces (Vecteur F₁) et (Vecteur F₂).

Ces deux forces (Vecteur F₁) et (Vecteur F₂) ont même ligne d'action, même intensité et des sens opposés.

### 2. Condition d'équilibre d'un corps sous l'action de deux forces:

    + Lorsqu'un corps est en équilibre sous l'action de deux forces: (Vecteur F₁) et (Vecteur F₂).
        - La somme vectorielle de ces deux forces est nulle. C-à-d: (Vecteur F₁) + (Vecteur F₂) = (Vecteur 0)
        - Elles ont la même ligne d'action.

la somme vectorielle de ces deux forces est nulle signifie que ces deux forces ont la même intensité et sens opposés et la même direction. Elle ne signifie pas que ces deux forces ont la même ligne d'action.

les deux forces ayant la même ligne d'action, signifie qu'elles ont la même direction. Mais si ces deux forces ont la même direction, elles n'ont pas forcément la même ligne d'action.

## II. Tension d'un ressort:

### 1. Équilibre d'un corps suspendu à l'extrémité d'un ressort:

**Système étudié:** {le corps solide S}

**Bilan des forces:**

*   (Vecteur P): poids du corps S.
*   (Vecteur T): tension du ressort.

**(Diagram Description: Diagram showing a solid S suspended by a spring. Arrows P (weight) pointing downwards and T (tension) pointing upwards. Lengths l0, l, and Δl are indicated)**

Le corps S est en équilibre  =>  (Vecteur P) + (Vecteur T) = (Vecteur 0) donc ces deux forces ont même intensité T = P = m.g.

On appelle allongement du ressort Δl, la différence entre sa longueur finale l et sa longueur initiale l₀:

Δl = |l - l₀|

### 2. Relation, entre la tension et l'allongement du ressort:

On suspend successivement différentes **masses** marquées à un ressort de longueur initiale l₀ = 10cm et on mesure sa longueur finale pour chaque équilibre. Puis on trace la courbe qui représente la variation de T en fonction de l'allongement Δl.

On prend l'intensité de pesanteur  g = 10N/kg

**(Table Description: Table of results with columns m(g), l(cm), Δl(cm), T(N) and data rows for different mass values)**

**(Graph Description: Graph T(N) vs Δl(cm) with a straight line passing through origin. Points A and B are marked on the line)**

**Tableau des résultats:**

| m(g)  | 40   | 30   | 20   | 10   | 0    |
|-------|------|------|------|------|------|
| l(cm) | 14   | 13   | 12   | 11   | 10   |
| Δl(cm)| 4    | 3    | 2    | 1    | 0    |
| T(N)  | 0.4  | 0.3  | 0.2  | 0.1  | 0    |

T = P = m.g

d'après le graphe on constate que la relation entre la tension et l'allongement du ressort est linéaire. Donc la tension d'un ressort est proportionnelle à son allongement et le coefficient de proportionnalité  est la constante de raideur k du ressort.

on écrit la relation entre la tension et l'allongement du ressort: T = k.Δl
d'où:
    + T : tension du ressort en (N)
    + k : constante de raideur du ressort en (N/m), elle dépend de la nature du ressort.
    + Δl : allongement du ressort en (m)
Dans le cas de compression, on a: Δl = |l - l₀| = l₀ - l car l₀ > l .
Dans le cas de dilatation, on a: Δl = |l - l₀| = l - l₀ car l₀ < l .


## III. Poussée d'Archimède:

### 1. Définition:

Tout corps immergé (partiellement ou totalement) dans un fluide (gaz ou liquide) subit de la part de ce fluide une force de contact répartie appelée **poussée d'Archimède**.

### 2. Expérimentale de la mise en évidence de la poussée d'Archimède:

On suspend un corps solide à un dynamomètre, on mesure son poids dans l'air puis dans l'eau.

**(Diagram Description: Three diagrams side-by-side. Leftmost: Dynamometer reading P=0.6N in air, middle: diagram showing initial volume V=211mL, rightmost: Dynamometer reading T=0.4N when immersed in water, water level at V'=232mL. Arrows P (weight), T (tension), and Fa (Archimedes' thrust) are shown. Calculation Fa = P - T = 0.6N - 0.4N = 0.2N)**

**Air Measurement:**
P = 0,6N
T = 0,6N
(Vecteur P) + (Vecteur T) = (Vecteur 0)

**Water Immersion:**
P = 0,6N
T = 0,4N
V = 211mL
V' = 232mL
(Vecteur T) + (Vecteur P) + (Vecteur Fa) = (Vecteur 0)
(Vecteur Fa) = (Vecteur P) - (Vecteur T) => Fa = P - T = 0,6 - 0,4 = 0,2N

### 3. Interprétations:

Malgré qu'il s'agit du même corps, le dynamomètre n'indique pas la même intensité dans les deux cas, car l'eau exerce sur le corps une force qui s'appelle: **poussée d'Archimède** dont les caractéristiques sont:

*   **Point d'application:** centre de gravité du liquide déplacé. (centre de poussée)
*   **Droite d'action:** verticale
*   **Sens:** vers le haut.
*   **Intensité:** poids du liquide déplacé.

**Expression de l'intensité de la poussée d'Archimède:**

Fₐ = ρ<0xE2><0x82><0x99>liquide * V<0xE2><0x82><0x99>déplacé * g

*   ρ<0xE2><0x82><0x99>liquide: étant la masse volumique du liquide en kg/m³
*   V<0xE2><0x82><0x99>déplacé: étant le volume du liquide déplacé en (m³).
*   g: intensité de pesanteur en (N/kg).

### 4. Exploitation des résultats de l'expérience:

Dans l'expérience précédente l'intensité de la poussée d'Archimède mesurée à l'aide du dynamomètre est: Fₐ=0,2N, et le volume du liquide déplacé :

V<0xE2><0x82><0x99>déplacé = V' - V = 232 - 211 = 21mL = 0,021 L = 0,021 * 10⁻³ m³

On a l'intensité de pesanteur : g=9,8N/kg.
La masse volumique de l'eau: ρ<0xE2><0x82><0x99>eau = 10³ kg/m³

Le poids du liquide déplacé est:

P<0xE2><0x82><0x99>liquide déplacé = m<0xE2><0x82><0x99>liquide déplacé * g = ρ<0xE2><0x82><0x99>liquide * V<0xE2><0x82><0x99>déplacé * g = 10³ kg/m³ * 0,021 * 10⁻³ m³ * 9,8N/kg⁻¹ ≈ 0,2N

Donc par comparaison avec les résultats précédents on a: l'intensité de la poussée d'Archimède est égale au poids du liquide déplacé.

**Remarque:** cette relation se généralise pour tous les fluides (gaz ou liquide).

### 5. Conclusion

Tout corps immergé (partiellement ou totalement) dans un fluide, subit de la part de ce fluide une force (Vecteur Fₐ) appelée **poussée d'Archimède** (force de contact répartie).

**Caractéristiques de la poussée d'Archimède:**

*   **Point d'application:** centre de gravité du liquide déplacé. (Il est important de ne pas confondre entre le centre de gravité du corps immergé et le centre de gravité du liquide déplacé).
*   **Droite d'action:** verticale
*   **Sens:** vers le haut.
*   **Intensité:** Fₐ = ρ<0xE2><0x82><0x99>fluide * V<0xE2><0x82><0x99>fluide * g

Important:
    + L'intensité de la poussée d'Archimède est égale au poids du fluide déplacé.
    + Jamais introduire la notion de trois forces en équilibre dans cette leçon. le cas d'un corps immergé dans un fluide est un cas particulier de deux forces en équilibre. On considère que la force de possée d'Archimède  et la tension du ressort sont colinéaires et de même sens. C-à-d que la force de poussée d'Archimède est une force de tension s'oppesant au poids du corps immergé. on peut facilement guidèe l'élève que vecteur T + vecteur Fa = - vecteur P => en intensité:  T + Fa = P

    + Intensité de pesanteur g = 9.8 N/kg

     + Jamais montionner la loi de Hooke dans cette leçon. on peut juste dire que la relation entre la tension et l'allongement du ressort est linéaire.

     + On n'utilise pas la projection des forces dans cette leçon. cela est réservé pour les cas de trois forces non parallèles.

--- End Document ---
"""

