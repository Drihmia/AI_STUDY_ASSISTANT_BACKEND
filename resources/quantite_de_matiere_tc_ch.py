# -*- coding: utf-8 -*-

quantite_de_matiere_tc_ch = """
# Outils de description d'un système

## 1- Définition : La mole.
La mole est l'unité de quantité de matière dans le Système International (SI).
**Définition :** Une mole est la quantité de matière d'un système contenant autant d'entités chimiques (atomes, molécules, ions...) qu'il y a d'atomes dans 12,0 grammes de carbone 12 (¹²C).

Ce nombre d'entités est appelé **nombre d'Avogadro** ou **constante d'Avogadro**, noté **NA**.
La valeur de la constante d'Avogadro est :
**NA ≈ 6,02 × 10²³ mol⁻¹**
(Cela signifie qu'il y a environ 6,02 × 10²³ entités par mole).

*Exemple :* Une mole d'atomes de fer contient 6,02 × 10²³ atomes de fer. Une mole de molécules d'eau contient 6,02 × 10²³ molécules d'eau.

*(Note sur le calcul dans le document original : La masse d'un atome de carbone 12 est m(¹²C) = A × mp où A=12 est le nombre de masse et mp la masse d'un nucléon. Ou plus précisément, m(¹²C) ≈ 12 u ≈ 12 × 1,66 × 10⁻²⁷ kg. Le nombre N d'atomes dans m = 12 g = 0,012 kg est N = m / m(¹²C) = 0,012 / (12 × 1,66 × 10⁻²⁷) ≈ 6,02 × 10²³ atomes. Donc NA ≈ 6,02 × 10²³ mol⁻¹).*

## 2- Quantité de matière d'un échantillon :
La quantité de matière d'une espèce chimique (x) se note **n(x)** et s'exprime en **moles (mol)**.
Le nombre d'entités chimiques (molécules, atomes ou ions) identiques présentes dans cet échantillon se note **N(x)** (c'est un nombre sans unité).
La relation entre la quantité de matière n(x) et le nombre d'entités N(x) est :

**n(x) = N(x) / NA**

Ou inversement :
**N(x) = n(x) × NA**

Où :
- n(x) : quantité de matière de l'espèce x (en mol)
- N(x) : nombre d'entités de l'espèce x
- NA : constante d'Avogadro (en mol⁻¹)

## 3- Masse molaire.

### Masse molaire atomique :
La masse molaire atomique d'un élément chimique est la masse d'une mole d'atomes de cet élément chimique.
Elle se note M et son unité est le **gramme par mole (g/mol)**.
*Remarque :* Les valeurs des masses molaires atomiques sont généralement données ou se trouvent dans le tableau périodique des éléments.
*Exemples :*
- M(H) = 1,0 g/mol (Hydrogène)
- M(C) = 12,0 g/mol (Carbone)
- M(O) = 16,0 g/mol (Oxygène)
- M(N) = 14,0 g/mol (Azote)

### Masse molaire moléculaire :
C'est la masse d'une mole de molécules de cette espèce chimique.
*Pratiquement :* La masse molaire moléculaire est égale à la somme des masses molaires atomiques de tous les atomes qui constituent la molécule.
L'unité est toujours le **g/mol**.
*Exemples :*
- Molécule d'eau (H₂O) :
  M(H₂O) = 2 × M(H) + 1 × M(O) = 2 × 1,0 + 16,0 = 18,0 g/mol
- Molécule d'éthanol (C₂H₆O) :
  M(C₂H₆O) = 2 × M(C) + 6 × M(H) + 1 × M(O) = 2 × 12,0 + 6 × 1,0 + 16,0 = 24,0 + 6,0 + 16,0 = 46,0 g/mol

## 4- Masse molaire et quantité de matière
La quantité de matière n(x) d'un échantillon d'une espèce chimique x, la masse m(x) de cet échantillon et la masse molaire M(x) de l'espèce sont liées par la relation fondamentale :

**n(x) = m(x) / M(x)**

Où :
- n(x) : quantité de matière (en mol)
- m(x) : masse de l'échantillon (doit être en grammes, g)
- M(x) : masse molaire de l'espèce x (en g/mol)

On peut aussi écrire : m(x) = n(x) × M(x)

## 5- Volume molaire des gaz.
Le volume molaire d'un gaz est le volume occupé par **une mole** de ce gaz dans des conditions de température (T) et de pression (P) données.
Il se note **Vm** et s'exprime généralement en **litre par mole (L/mol)**.

**Loi d'Avogadro-Ampère :** À une température et une pression données, tous les gaz parfaits occupent le même volume molaire. Le volume molaire d'un gaz est indépendant de la nature du gaz, il dépend uniquement de la température et de la pression.

*Valeurs courantes du volume molaire :*
- **Conditions ordinaires de température et de pression :**
  Température T = 20°C (= 293,15 K)
  Pression P = 10⁵ Pa (= 1 bar)
  Volume molaire : **Vm = 24,0 L/mol**
- **Conditions normales de température et de pression (CNTP) :**
  Température T = 0°C (= 273,15 K)
  Pression P = 10⁵ Pa (= 1 bar) (*Note : La pression normale est parfois définie comme P = 1 atm = 101325 Pa*)
  Volume molaire : **Vm ≈ 22,4 L/mol** (Cette valeur est une approximation courante, surtout si l'on se réfère à P=1 atm).

## 6- Volume molaire et quantité de matière :
La quantité de matière n(x) d'un échantillon de gaz, le volume V(x) occupé par ce gaz et le volume molaire Vm (mesurés dans les mêmes conditions de température T et de pression P) sont liés par la relation :

**n(x) = V(x) / Vm**

Où :
- n(x) : quantité de matière du gaz (en mol)
- V(x) : volume du gaz (doit être en litres, L)
- Vm : volume molaire des gaz (en L/mol)

On peut aussi écrire : V(x) = n(x) × Vm

# Page 1

## 7- La densité d d'un gaz par rapport à l'air
On définit la densité **d** d'un gaz comme le rapport de sa masse volumique (ρ) sur la masse volumique de l'air (ρ₀), prises dans les mêmes conditions de température et de pression. L'air est le gaz de référence.

**d = ρ / ρ₀**

Où :
- ρ : masse volumique du gaz étudié (par exemple en g/L)
- ρ₀ : masse volumique de l'air (dans les mêmes conditions T, P ; par exemple en g/L)
- d : densité du gaz par rapport à l'air.

*Propriétés :*
- La densité **d** est une grandeur **sans unité**.
- La densité est aussi égale au rapport de la masse d'un certain volume de gaz sur la masse du même volume d'air (les volumes étant mesurés dans les mêmes conditions T, P).

*Relation approchée avec la masse molaire :*
Considérons un volume V égal au volume molaire Vm dans certaines conditions T, P.
- La masse de ce volume Vm de gaz est sa masse molaire M (en g/mol).
- La masse du même volume Vm d'air est la masse molaire moyenne de l'air, M(air) ≈ 29 g/mol (l'air est un mélange d'environ 80% N₂ (M=28 g/mol) et 20% O₂ (M=32 g/mol)).

La masse volumique est ρ = masse / volume.
Donc ρ = M / Vm pour le gaz, et ρ₀ = M(air) / Vm pour l'air.
Le rapport des masses volumiques devient :
d = ρ / ρ₀ = (M / Vm) / (M(air) / Vm) = M / M(air)

On peut donc retenir la formule approchée suivante pour calculer rapidement la densité d d'un gaz (considéré comme parfait) par rapport à l'air :

**d ≈ M / 29**

Où :
- M est la masse molaire du gaz (en g/mol)
- 29 g/mol est la masse molaire moyenne approchée de l'air.

# Page 2
"""
