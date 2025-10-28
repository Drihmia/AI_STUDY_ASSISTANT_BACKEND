# -*- coding: utf-8 -*-

transfert_energie = """
# Document: Transfert d'énergie dans un circuit électrique


**PH9:** Transfert d'énergie dans un circuit électrique

## Introduction :

Les appareils électriques reçoivent de l'énergie électrique et la transforment en d'autres formes utiles, en s'échauffant au cours du fonctionnement.

- Quels sont les différents transferts ou transmissions d'énergies qui se font au niveau des récepteurs?
- Comment se répartit l'énergie électrique dans un circuit ? et pourquoi les appareils s'échauffent-ils ?

**(Image Description: Images of various electrical appliances: toaster, washing machine, electric kettle, microwave oven.)**

## 1. Mise en évidence expérimentale du transfert d'énergie électrique :

**Activité :**

**Expérience :**
Considérons un circuit électrique comportant un générateur de courant continu, une lampe, un moteur, un interrupteur (K) et un électrolyseur qui contient une solution de soude.

**(Diagram Description: Circuit diagram showing a DC generator (+/-), a switch (K), a lamp symbol, a motor symbol (M in a circle), and an electrolyzer symbol connected in series.)**

**Observation :**
Lorsqu'on ferme l'interrupteur K on constate que:
- la lampe [s'allume] et sa température [augmente].
- le moteur [tourne] et sa température [augmente].
- l'électrolyseur est le siège de [réactions chimiques] au niveau de chaque électrode, et on constate [une augmentation] de la température de l'électrolyseur.

**Interprétation :**
Dans cette expérience on a mis en évidence les différents types de transfert d'énergie:
- le générateur : est une source d'énergie électrique.
- au niveau de la lampe il y'a une transformation de l'énergie [électrique] en énergie [lumineuse] et en énergie [thermique].
- au niveau du moteur il y'a une transformation de l'énergie [électrique] en énergie [mécanique] et en énergie [thermique].
- au niveau de l'électrolyseur il y'a une transformation de l'énergie [électrique] en énergie [chimique] et en énergie [thermique].

**Conclusion:**
Le générateur est une source d'énergie électrique, c'est lui qui fournit l'énergie électrique aux autres composants du circuit. Alors que la lampe, le moteur et l'électrolyseur sont des récepteurs qui reçoivent l'énergie électrique et la transforment en d'autres formes d'énergie (comme l'énergie mécanique, chimique, thermique, ou lumineuse...).

## 2. Énergie électrique reçue par un récepteur:

### 1. Définition d'un récepteur :

On appelle récepteur électrique tout dipôle qui reçoit l'énergie électrique et la transforme en une autre forme d'énergie.
Exemples de récepteurs : lampe, moteur, électrolyseur, conducteur ohmique ...
Dans la convention récepteur, la tension U<0xE2><0x82><0x9AB> entre ses bornes et l'intensité I du courant qui le traverse sont de sens contraires.

**(Diagram Description: Diagram showing a generic receptor between points A and B. Current I flows from A to B. Voltage UAB is shown with the arrow pointing from B to A, indicating opposite directions for I and UAB in the receptor convention.)**
   I →
A ------[récepteur]------ B
   ←----- U<0xE2><0x82><0x9AB> -----→

### 2. Puissance électrique reçue par un récepteur :

La puissance électrique (Pₑ) reçue par un récepteur AB parcouru par un courant d'intensité I et dont la tension entre ses bornes est U<0xE2><0x82><0x9AB> est donnée par la relation suivante :

Pₑ = U<0xE2><0x82><0x9AB> * I

*   Pₑ: Puissance électrique reçue (en Watt, W)
*   U<0xE2><0x82><0x9AB>: Tension aux bornes du récepteur (en Volt, V)
*   I: Intensité du courant traversant le récepteur (en Ampère, A)

## 3. Énergie électrique reçue par un récepteur :

L'énergie électrique (Wₑ) reçue par un récepteur AB pendant la durée Δt est donnée par la relation suivante :

Wₑ = Pₑ * Δt = U<0xE2><0x82><0x9AB> * I * Δt

*   Wₑ: Énergie électrique reçue (en Joule, J)
*   Pₑ: Puissance électrique reçue (en Watt, W)
*   Δt: Durée de fonctionnement (en seconde, s)

**Application 1:**
Un moteur électrique est alimenté sous une tension U<0xE2><0x82><0x9AB>= 12V et traversé par un courant d'intensité I=200 mA.
1. Calculer la puissance électrique reçue par ce moteur.
   *Pₑ = U<0xE2><0x82><0x9AB> * I = 12V * (200 * 10⁻³ A) = 2.4 W*
2. Calculer l'énergie électrique reçue par le moteur pendant 20 min de fonctionnement.
   *Δt = 20 min = 20 * 60 s = 1200 s*
   *Wₑ = Pₑ * Δt = 2.4 W * 1200 s = 2880 J*
3. Sachant que l'énergie thermique fournie par le moteur au milieu extérieur est Wₜ<0xE2><0x82><0x95> = 864 J, calculer l'énergie mécanique fournie par le moteur.
   *L'énergie reçue est transformée en énergie mécanique (utile Wu) et énergie thermique (Wₜ<0xE2><0x82><0x95>). Wₑ = Wu + Wₜ<0xE2><0x82><0x95>*
   *Wu = Wₑ - Wₜ<0xE2><0x82><0x95> = 2880 J - 864 J = 2016 J*

## 4. Effet Joule dans un conducteur - Loi de Joule :

### 1. Effet Joule :

Le passage du courant électrique dans un récepteur électrique entraîne une élévation de sa température, ce phénomène s'appelle l'**effet Joule** (il porte le nom du physicien anglais James Prescott Joule qui l'a découvert en 1840).
Les récepteurs électriques transforment intégralement ou partiellement l'énergie électrique reçue en chaleur par effet Joule.

**(Image Description: Portrait of James Prescott Joule.)**

### 2. Loi de Joule :

Les conducteurs ohmiques (appelés aussi résistances) transforment intégralement l'énergie électrique reçue en chaleur par effet Joule.
Pour un conducteur ohmique : U<0xE2><0x82><0x9AB> = R * I (Loi d'Ohm)

- La puissance électrique reçue par un conducteur ohmique (puissance dissipée par effet Joule) Pⱼ:
  Pⱼ = U<0xE2><0x82><0x9AB> * I = (R * I) * I = R * I²

- L'énergie électrique reçue par un conducteur ohmique (énergie dissipée par effet Joule) Wⱼ:
  Wⱼ = Pⱼ * Δt = R * I² * Δt

- La quantité de chaleur fournie par le conducteur ohmique au milieu extérieur (Q) est égale à l'énergie dissipée par effet Joule:
  Q = Wⱼ = R * I² * Δt

**Application 2:**
On applique aux bornes d'un conducteur ohmique de résistance R = 10 Ω une tension U<0xE2><0x82><0x9AB> = 4V.
1. Calculer l'intensité du courant I qui traverse le conducteur ohmique.
   *I = U<0xE2><0x82><0x9AB> / R = 4V / 10 Ω = 0.4 A*
2. Calculer la puissance électrique reçue par le conducteur ohmique.
   *Pₑ = Pⱼ = U<0xE2><0x82><0x9AB> * I = 4V * 0.4 A = 1.6 W*
   *(ou Pⱼ = R * I² = 10 Ω * (0.4 A)² = 10 * 0.16 = 1.6 W)*
3. Sachant que la tension U<0xE2><0x82><0x9AB> est appliquée pendant la durée Δt = 5min. Calculer l'énergie dissipée par effet joule.
   *Δt = 5 min = 5 * 60 s = 300 s*
   *Wⱼ = Pⱼ * Δt = 1.6 W * 300 s = 480 J*

## 5. Énergie électrique fournie par un générateur :

### 1. Définition d'un générateur :

Le générateur est un dipôle actif qui fournit de l'**énergie électrique** au reste du circuit.
Exemples de générateurs : pile, centrale thermique, centrale nucléaire...
Dans la convention générateur, la tension U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> et l'intensité I ont le même sens.

**(Diagram Description: Diagram showing a generator between points P and N. Current I flows from P to N. Voltage UPN is shown with the arrow pointing from P to N, indicating the same direction for I and UPN in the generator convention.)**
   I →
P ------[Générateur]------ N
   →----- U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> -----→

### 2. Puissance électrique fournie par un générateur :

La puissance électrique (Pₑ) fournie par le générateur au reste du circuit est donnée par la relation suivante :

Pₑ = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I

*   Pₑ: Puissance électrique fournie (en Watt, W)
*   U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A>: Tension aux bornes du générateur (en Volt, V)
*   I: Intensité du courant débité par le générateur (en Ampère, A)

## 6. Énergie électrique fournie par un générateur :

L'énergie électrique (Wₑ) fournie par le générateur au reste du circuit durant la durée Δt est donnée par la relation suivante :

Wₑ = Pₑ * Δt = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I * Δt

*   Wₑ: Énergie électrique fournie (en Joule, J)
*   Pₑ: Puissance électrique fournie (en Watt, W)
*   Δt: Durée de fonctionnement (en seconde, s)

**Application 3:**
Un générateur électrique fournit au circuit électrique la puissance électrique Pₑ = 300W. L'intensité du courant qui circule dans ce circuit est: I=1,2 A.
1. Calculer la tension U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> aux bornes du générateur.
   *U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = Pₑ / I = 300W / 1.2 A = 250 V*
2. Calculer l'énergie électrique transmise au reste du circuit pendant une durée de 10min.
   *Δt = 10 min = 10 * 60 s = 600 s*
   *Wₑ = Pₑ * Δt = 300W * 600 s = 180000 J = 180 kJ*

**Application 4:**
On branche un générateur avec un électrolyseur. (Voir le circuit ci-contre).
Le générateur électrique fournit au circuit électrique l'énergie électrique Wₑ = 2400 J. La durée de fonctionnement est 20min.

**(Diagram Description: Simple circuit diagram with a generator symbol connected to an electrolyzer symbol.)**

1. Calculer la puissance électrique fournie par le générateur.
   *Δt = 20 min = 20 * 60 s = 1200 s*
   *Pₑ = Wₑ / Δt = 2400 J / 1200 s = 2 W*
2. Sachant que la tension aux bornes du générateur est U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = 10V. Calculer I l'intensité du courant qui circule dans le circuit.
   *I = Pₑ / U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = 2 W / 10 V = 0.2 A*
3. En déduire la puissance électrique reçue par l'électrolyseur.
   *Dans ce circuit simple, l'électrolyseur est le seul récepteur.*
   *P<0xE1><0xB5><0x99>é<0xE1><0xB5><0x84>ᵤ<0xE1><0xB5><0x96> = P<0xE1><0xB5><0x8A> = 2 W*

--- End Document 1 ---

"""

# Document 2: Comportement global d'un circuit électrique (Pages 4-7)
comportement_global = """
# Document: Comportement global d'un circuit électrique

**PH10:** Comportement global d'un circuit électrique

## Introduction :

La batterie auto joue le rôle d'un générateur, elle sert à démarrer une voiture, ainsi qu'à alimenter en électricité les différents éléments électriques (phares, ...) et électroniques (autoradio, ...).
Comment se distribue l'énergie électrique au niveau d'un générateur et d'un récepteur ?

**(Image Description: Photo of a car engine bay with the battery visible.)**

## 1. Distribution de l'énergie reçue par un récepteur :

### 1. Loi d’Ohm pour un récepteur :

Dans son domaine de fonctionnement habituel, la tension U<0xE2><0x82><0x9AB> aux bornes d'un récepteur parcouru par un courant d'intensité I entrant par sa borne A, est donnée par :

U<0xE2><0x82><0x9AB> = E' + r' * I

*   U<0xE2><0x82><0x9AB>: Tension aux bornes du récepteur (V)
*   I: Intensité du courant (A)
*   E': Force contre-électromotrice (f.c.e.m.) du récepteur (V) (Représente l'énergie convertie en forme utile autre que thermique)
*   r': Résistance interne du récepteur (Ω)

Cette relation appelée **Loi d'Ohm pour un récepteur (actif)**.

### 2. Bilan énergétique d'un récepteur :

On a d'après la loi d'Ohm pour un récepteur : U<0xE2><0x82><0x9AB> = E' + r' * I
Multiplions les deux membres de l'équation par le terme I.Δt, on obtient :

U<0xE2><0x82><0x9AB> * I * Δt = E' * I * Δt + r' * I² * Δt

La signification de chaque terme est :
*   Wₑ = U<0xE2><0x82><0x9AB> * I * Δt : Énergie électrique reçue par le récepteur (J)
*   Wu = E' * I * Δt : Énergie utile (transformée en énergie mécanique, chimique, ...) (J)
*   Wⱼ = r' * I² * Δt : Énergie dissipée par effet Joule (chaleur) dans le récepteur (J)

Alors le bilan énergétique pour un récepteur s'écrit:

Wₑ = Wu + Wⱼ

**(Diagram Description: Energy flow diagram for a receptor. Input We (énergie électrique reçue) splits into Wu (énergie utile) and WJ (chaleur dissipée par effet Joule).)**

énergie électrique reçue (We) → [ récepteur ] → énergie utile (Wu) + chaleur dissipée par effet Joule (WJ)
                       Bilan énergétique d'un récepteur

**Remarque:** En divisant les deux membres de l'équation précédente par Δt, on obtient le bilan de puissance:

Pₑ = Pu + Pⱼ
U<0xE2><0x82><0x9AB> * I = E' * I + r' * I²

La signification de chaque terme est :
*   Pₑ = U<0xE2><0x82><0x9AB> * I : Puissance électrique reçue (W)
*   Pu = E' * I : Puissance utile (W)
*   Pⱼ = r' * I² : Puissance dissipée par effet Joule (W)

Alors le bilan de la puissance pour un récepteur s'écrit : Pₑ = Pu + Pⱼ

### 3. Rendement d'un récepteur :

Le rendement d'un récepteur (noté η) est défini comme le rapport de l'énergie utile (Wu) par l'énergie électrique reçue (Wₑ) par le récepteur :

η = Wu / Wₑ = (E' * I * Δt) / (U<0xE2><0x82><0x9AB> * I * Δt) = E' / U<0xE2><0x82><0x9AB> = E' / (E' + r' * I)

Le rendement est nombre sans unité qui s'exprime généralement en pourcentage. (0 ≤ η ≤ 1)

**Application 1:**
Un moteur électrique de résistance r'=2 Ω est parcouru par un courant I=1A lorsqu'il est alimenté sous une tension U<0xE2><0x82><0x9AB> = 12V. Déterminer :
1. la force contre-électromotrice du moteur: E'
   *U<0xE2><0x82><0x9AB> = E' + r'I => E' = U<0xE2><0x82><0x9AB> - r'I = 12V - (2 Ω * 1A) = 10V*
2. la puissance électrique absorbée par ce moteur : Pₑ
   *Pₑ = U<0xE2><0x82><0x9AB> * I = 12V * 1A = 12 W*
3. la puissance utile fournie par ce moteur: Pu
   *Pu = E' * I = 10V * 1A = 10 W*
4. La puissance dissipée dans le moteur par effet joule : Pⱼ
   *Pⱼ = r' * I² = 2 Ω * (1A)² = 2 W*
   *(Vérification: Pₑ = Pu + Pⱼ => 12W = 10W + 2W)*
5. le rendement électrique de ce moteur: η
   *η = Pu / Pₑ = 10W / 12W ≈ 0.833 soit 83.3%*
   *(ou η = E' / U<0xE2><0x82><0x9AB> = 10V / 12V ≈ 0.833)*

## 2. Distribution de l'énergie de générateur :

### 1. Loi d'Ohm pour un générateur :

La tension U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> aux bornes d'un générateur, débitant un courant d'intensité I sortant par sa borne P, est donnée par :

U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = E - r * I

*   U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A>: Tension aux bornes du générateur (V)
*   I: Intensité du courant débité (A)
*   E: Force électromotrice (f.e.m.) du générateur (V) (Représente l'énergie convertie par unité de charge)
*   r: Résistance interne du générateur (Ω)

Cette relation appelée **Loi d'Ohm pour un générateur**.

### 2. Bilan énergétique d'un générateur :

On a d'après la loi d'Ohm pour un générateur : U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = E - r * I
Multiplions les deux membres de l'équation par le terme I.Δt, on obtient :

U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I * Δt = E * I * Δt - r * I² * Δt

Réarrangeons : E * I * Δt = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I * Δt + r * I² * Δt

La signification de chaque terme est :
*   W<0xE1><0xB5><0x80> = E * I * Δt : Énergie électrique totale transformée (générée) par le générateur (J)
*   Wₑ = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I * Δt : Énergie électrique fournie au circuit extérieur (disponible) (J)
*   Wⱼ = r * I² * Δt : Énergie dissipée par effet Joule (chaleur) à l'intérieur du générateur (J)

Alors le bilan énergétique pour un générateur s'écrit:

W<0xE1><0xB5><0x80> = Wₑ + Wⱼ

**(Diagram Description: Energy flow diagram for a generator. Input WT (énergie électrique totale du générateur) splits into We (énergie électrique disponible) and WJ (chaleur dissipée par effet Joule).)**

énergie électrique totale du générateur (WT) → [ générateur ] → énergie électrique disponible (We) + chaleur dissipée par effet Joule (WJ)
                          Bilan énergétique d'un générateur

**Remarque:** En divisant les deux membres de l'équation précédente par Δt, on obtient le bilan de puissance:

P<0xE1><0xB5><0x80> = Pₑ + Pⱼ
E * I = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I + r * I²

La signification de chaque terme est :
*   P<0xE1><0xB5><0x80> = E * I : Puissance électrique totale générée (W)
*   Pₑ = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I : Puissance électrique fournie au circuit extérieur (W)
*   Pⱼ = r * I² : Puissance dissipée par effet Joule dans le générateur (W)

Alors le bilan de la puissance pour un générateur s'écrit: P<0xE1><0xB5><0x80> = Pₑ + Pⱼ

### 3. Rendement d'un générateur :

Pour un générateur électrique, le rendement η est le rapport de l'énergie électrique fournie au circuit (Wₑ) à l'énergie totale transformée par le générateur (W<0xE1><0xB5><0x80>) :

η = Wₑ / W<0xE1><0xB5><0x80> = (U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I * Δt) / (E * I * Δt) = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> / E = (E - r * I) / E = 1 - (r * I) / E

**Application 2:**
Un générateur de f.é.m. E = 13 V et de résistance interne r=1 Ω alimente un moteur électrique de force contre-électromotrice E' = 10 V et de résistance interne r'=2 Ω. Déterminer :
1. l'intensité du courant dans le circuit: I
   *Appliquant la loi de Pouillet (voir section suivante) ou la loi des mailles: U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = U<0xE2><0x82><0x9AB> => E - rI = E' + r'I => E - E' = (r + r')I*
   *I = (E - E') / (r + r') = (13V - 10V) / (1Ω + 2Ω) = 3V / 3Ω = 1 A*
2. la tension aux bornes de générateur : U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A>
   *U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = E - rI = 13V - (1Ω * 1A) = 12 V*
3. la puissance électrique fournie par le générateur : Pₑ
   *Pₑ = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> * I = 12V * 1A = 12 W*
4. la puissance totale générée par le générateur : P<0xE1><0xB5><0x80>
   *P<0xE1><0xB5><0x80> = E * I = 13V * 1A = 13 W*
5. La puissance dissipée dans le générateur par effet joule : Pⱼ
   *Pⱼ = r * I² = 1Ω * (1A)² = 1 W*
   *(Vérification: P<0xE1><0xB5><0x80> = Pₑ + Pⱼ => 13W = 12W + 1W)*
6. le rendement du générateur : η<0xE1><0xB5><0x82>
   *η<0xE1><0xB5><0x82> = Pₑ / P<0xE1><0xB5><0x80> = 12W / 13W ≈ 0.923 soit 92.3%*
   *(ou η<0xE1><0xB5><0x82> = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> / E = 12V / 13V ≈ 0.923)*

## 4. Transfert d'énergie dans un circuit électrique simple :

### 1. Loi de Pouillet :

Considérons un circuit série, constitué par un générateur (E, r), un électrolyseur (E', r') et un conducteur ohmique (R).

**(Diagram Description: Circuit diagram showing a generator (E, r) connected in series with a receptor (motor/electrolyzer E', r') and a resistor (R). Points A, B, C, P, N are marked.)**

Appliquons la loi d'addition de tension dans le circuit (loi des mailles):
U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = U<0xE1><0xB5><0x96><0xE1><0xB5><0x84> + U<0xE2><0x82><0x91><0xE2><0x82><0x85> + U<0xE1><0xB5><0x84>C

et en utilisant les différentes expressions de la loi d'Ohm aux différents dipôles, on obtient:
E - rI = E' + r'I + RI

Donc:
E - E' = (r + r' + R) I

Finalement l'intensité de courant électrique :

I = (E - E') / (r + r' + R) = (Somme des f.e.m - Somme des f.c.e.m) / (Somme des résistances)

La généralisation de cette expression conduit à la **loi de Pouillet** peut s'écrire :

I = (∑E - ∑E') / ∑R<0xE1><0xB5><0x80>ₒₜ<0xE2><0x82><0x90>ₗ<0xE2><0x82><0x91>

Exemple:
D'après la loi de Pouillet (application 2), on a :
*I = (E - E') / (r + r') = (13V - 10V) / (1Ω + 2Ω) = 1A*

### 2. Bilan énergétique de circuit :

La conservation de l'énergie (de la puissance) permet d'écrire :
Puissance totale générée = Puissance totale reçue/dissipée

Donc:
P<0xE1><0xB5><0x80>_générateur = P<0xE1><0xB5><0x99>_récepteur + Pⱼ_circuit

Alors:
E * I = (E' * I + r' * I²) + (R * I²) + (r * I²)

D'où :
E * I = E' * I + (r + r' + R) * I²

Finalement :
E = E' + (r + r' + R) * I  (On retrouve la loi des mailles)

Généralement dans circuit: Puissance fournie par générateurs = Puissance reçue par récepteurs + Puissance dissipée par effet Joule

## 5. Le rendement global d'un circuit simple :

Le rendement global (η) de circuit est défini comme le rapport de la puissance utile (Pu) par la puissance électrique totale (P<0xE1><0xB5><0x80>) du générateur :

η = Pu / P<0xE1><0xB5><0x80> = (∑E' * I) / (∑E * I) = ∑E' / ∑E

**Application 3:**
Un moteur électrique (E' = 4 V, r'= 1 Ω) est alimenté par un générateur (E = 12 V, r = 3 Ω).
1. Calculer l'intensité du courant qui circule dans le circuit : I
   *I = (E - E') / (r + r') = (12V - 4V) / (3Ω + 1Ω) = 8V / 4Ω = 2 A*
2. Calculer la puissance utile: Pu
   *Pu = E' * I = 4V * 2A = 8 W*
3. Calculer la puissance totale: P<0xE1><0xB5><0x80>
   *P<0xE1><0xB5><0x80> = E * I = 12V * 2A = 24 W*
4. Calculer le rendement du moteur : η<0xE2><0x82><0x9C>
   *U<0xE2><0x82><0x9AB> = E' + r'I = 4V + (1Ω * 2A) = 6V*
   *η<0xE2><0x82><0x9C> = E' / U<0xE2><0x82><0x9AB> = 4V / 6V ≈ 0.667 soit 66.7%*
5. Calculer le rendement du générateur : η<0xE1><0xB5><0x82>
   *U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> = E - rI = 12V - (3Ω * 2A) = 12V - 6V = 6V*
   *η<0xE1><0xB5><0x82> = U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> / E = 6V / 12V = 0.5 soit 50%*
6. Calculer le rendement global du circuit : η
   *η = Pu / P<0xE1><0xB5><0x80> = 8W / 24W ≈ 0.333 soit 33.3%*
   *(ou η = η<0xE2><0x82><0x9C> * η<0xE1><0xB5><0x82> = (E'/U<0xE2><0x82><0x9AB>) * (U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A>/E) = (E'/E) car U<0xE2><0x82><0x9AB>=U<0xE1><0xB5><0x96><0xE1><0xB5><0x8A> dans ce cas; η = 4V / 12V ≈ 0.333)*


## Exercice 1:

Un générateur de f.é.m. E = 12 V et de résistance interne r=1 Ω alimente un moteur électrique de force contre-électromotrice E' = 10 V et de résistance interne r'=2 Ω.
1. Déterminer l'intensité du courant dans le circuit.
2. Déterminer la tension aux bornes du générateur.
3. Déterminer la puissance utile fournie par le moteur.
4. Déterminer le rendement du moteur.
--- End Document 2 ---

"""
