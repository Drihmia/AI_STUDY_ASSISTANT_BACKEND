# -*- coding: utf-8 -*-
equilibre_rotation_tc_pc = """
# lecons : Équilibre d'un solide en rotation autour d'un axe fixe

## I. Effet d'une force sur la rotation d'un solide

**(Diagram Description: Diagram illustrating a door rotating around a fixed axis. Forces \(\vec{F_1}\), \(\vec{F_2}\), and \(\vec{F_3}\) are applied. \(\vec{F_1}\) is parallel to the axis, \(\vec{F_2}\) intersects the axis, and \(\vec{F_3}\) is perpendicular to the axis, causing rotation.)**


*   Si on exerce sur une porte ouverte une force \(\vec{F_1}\) parallèle à l'axe de rotation, celle-ci ne tourne pas.
*   Si on exerce sur cette porte une force \(\vec{F_2}\) dont la droite d'action coupe l'axe, elle ne tourne pas non plus.
*   Une force \(\vec{F_3}\) perpendiculaire à la porte (n´est pas sécante à l'axe de rotation) provoque une rotation. L'efficacité de la rotation dépend de l'intensité de la force et de la position de la droite d'action par rapport à l'axe de rotation.

## II. Moment d'une force par rapport à un axe

### 1. Définition du moment d'une force

Le **moment d'une force par rapport à un axe** traduit son efficacité à produire un effet de rotation du solide autour de cet axe.

L'intensité du moment par rapport à un axe d'une force \(\vec{F}\) orthogonale à cet axe est le produit de l'intensité \(F\) de cette force par la distance \(d\) séparant la droite d'action de la force et l'axe :

\( M_{\Delta}(\vec{F}) = F \cdot d \)

**(Diagram Description: Two diagrams illustrating the calculation of the moment. Left: Force \(\vec{F}\) is perpendicular to distance \(d\) from axis \(\Delta\). Right: Force \(\vec{F}\) is at an angle \(\alpha\), only the perpendicular component matters for the moment.)**


*Application 1: Voir Exercice 1 Page 91*

### 2. Moment: grandeur algébrique

Afin de distinguer les deux possibilités de sens de rotation, nous évaluerons algébriquement le moment d'une force par rapport à l'axe par l'une des expressions suivantes (convention de signe selon le sens positif choisi):

**(Diagram Description: Two diagrams showing the convention for positive and negative moment based on the direction of rotation induced by force \(\vec{F}\) relative to the chosen positive direction around axis \(\Delta\).)**

| Lorsque \(\vec{F}\) tend à faire tourner le solide dans le sens positif choisi | Lorsque \(\vec{F}\) tend à faire tourner le solide dans le sens contraire au sens positif choisi |
| :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------- |
| **(Diagram showing positive rotation)**                                    | **(Diagram showing negative rotation)**                                                        |
| \( M_{\Delta}(\vec{F}) = +F \cdot d \)                                     | \( M_{\Delta}(\vec{F}) = -F \cdot d \)                                                         |

## III. Théorème des moments

Lorsqu'un solide, mobile autour d'un axe fixe \(\Delta\), est en équilibre, la somme algébrique des moments, par rapport à cet axe, de toutes les forces extérieures appliquées à ce solide est nulle:

\( \sum M_{\Delta}(\vec{F_i}) = 0 \)

**REMARQUE**

**Conditions générales d'équilibre**

Lorsqu'un solide est en équilibre, deux conditions doivent être satisfaites:

1.  **Immobilité du centre de gravité G:** \( \sum \vec{F_i} = \vec{0} \)
2.  **Absence de rotation autour de l'axe:** \( \sum M_{\Delta}(\vec{F_i}) = 0 \)

*Application 2: Voir Exercice F Page 95*

## IV. Couples de forces

### 1. Définition d'un couple de forces

Un **couple de forces** est un système de deux forces parallèles, de sens contraires, de même intensité et n'ayant pas la même droite support (lignes d'action différentes).

**(Diagram Description: Diagrams illustrating examples of couples: (a) rotating a wheel, (b) turning a screwdriver.)**

(a) Rotating forces: couples (\(\vec{F}\), \(-\vec{F}\))
(b) Applying torque with two opposing forces (\(\vec{F}\), \(-\vec{F}\))

### 2. Moment d'un couple de forces : \( M_{\Delta}(C) \)

Le moment d'un couple de force ne dépend pas de la position de l'axe de rotation mais seulement de la distance entre les deux lignes d'action.

\( M_{\Delta}(C) = M_{\Delta}(\vec{F_1}) + M_{\Delta}(\vec{F_2}) = F_1 \cdot d_1 + F_2 \cdot d_2 \)

avec
\( F_1 = F_2 = F \)
\( d_1 + d_2 = d \)

\( d \) est la distance séparant les deux droites d'action.

\( M_{\Delta}(C) = F \cdot d \)

**(Diagram Description: Diagram illustrating a couple of forces \(\vec{F_1}\) and \(\vec{F_2}\), parallel and opposite, separated by distance \(d = d_1 + d_2\).)**

*Application 3: Voir Exercice 3 Page 94*

En général, le moment d'un couple de force est : \( M_{\Delta}(C) = \pm F \cdot d \)

*Application 4: Voir Exercice 5 Page 94*

## V. Couple de torsion

Un **pendule de torsion** est un solide suspendu à un fil vertical, le centre de masse étant sur l'axe du fil, l'autre extrémité du fil étant maintenue fixe dans un support.

Quand le solide tourne autour de l'axe du fil, celui-ci réagit à la torsion en exerçant des forces de rappel équivalentes à un couple dont le moment par rapport à l'axe est proportionnel à l'angle de torsion \(\theta\) en (rad):

\( M_{\Delta}(C) = -C \cdot \theta \)

**(Diagram Description: Diagram showing a torsion pendulum setup with a suspended bar, angle of torsion \(\theta\), and coordinate axes x, y, z.)**


La constante \( C \), dite **constante de torsion**, dépend de la longueur et du diamètre du fil (supposé cylindrique) et de la nature du matériau constituant le fil (en N.m/rad).

*Application 5: Voir Exercice 8 Page 94*

IMPORTANT NOTES:
    - Si le sense de rotation n'est pas précisé, on vérifier avec l'élève si cette information dans la figure de l'exercice donné, sinon on définit un sens positif de rotation pour un exercice donné.
--- End Document ---
"""
