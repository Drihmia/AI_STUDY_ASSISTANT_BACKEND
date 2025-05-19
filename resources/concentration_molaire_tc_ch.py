# -*- coding: utf-8 -*-

concentration_molaire_tc_ch = """
# Concentration molaire des espèces moléculaires dans une solution

## I- Définition d'une solution aqueuse

Une **solution** est obtenue par **dissolution** d'une espèce chimique (appelée **soluté**) dans un liquide appelé **solvant**.
- Le **solvant** est l'espèce chimique majoritaire (présente en plus grande quantité).
- Le **soluté** est l'espèce chimique minoritaire (dissoute dans le solvant).

Il existe une limite à la quantité de soluté que l'on peut dissoudre dans un volume donné de solvant à une température donnée. Cette limite est appelée la **solubilité**. Si l'on dépasse cette limite, la solution est dite **saturée**.

**Remarque :**
Si le solvant est l'eau, la solution est appelée **solution aqueuse**.

## II- Notion de concentration

### Notion de concentration massique
On appelle **concentration massique** d'un soluté (x) dans une solution, notée **Cm(x)** (ou ρ(x)), le rapport entre la masse **m(x)** de soluté dissous et le volume total **V_s** de la solution.

**Cm(x) = m(x) / V_S**

- **Cm(x)** : concentration massique (en g/L ou g·L⁻¹)
- **m(x)** : masse du soluté (en g)
- **V_S** : volume total de la solution (en L)

L'unité usuelle de la concentration massique est le **gramme par litre (g/L)**.

### Notion de concentration molaire
On appelle **concentration molaire** d'un soluté (x) apporté dans une solution, notée **C(x)** (ou simplement C), le rapport entre la quantité de matière **n(x)** de soluté dissous et le volume total **V_S** de la solution.

**C(x) = n(x) / V_S**

- **C(x)** : concentration molaire (en mol/L ou mol·L⁻¹)
- **n(x)** : quantité de matière du soluté (en mol)
- **V_S** : volume total de la solution (en L)

L'unité usuelle de concentration molaire est la **mole par litre (mol/L)**. L'unité internationale (SI) est la mole par mètre cube (mol/m³), mais elle est moins utilisée en chimie pratique.

### La relation entre concentration molaire et massique
On sait que la quantité de matière n(x) est liée à la masse m(x) et à la masse molaire M(x) par la relation : n(x) = m(x) / M(x).
En substituant n(x) dans la formule de la concentration molaire :
C(x) = n(x) / V_S = (m(x) / M(x)) / V_S = m(x) / (V_S × M(x)) = (m(x) / V_S) × (1 / M(x))
Comme Cm(x) = m(x) / V_S, on obtient la relation :

**C(x) = Cm(x) / M(x)**   ou   **Cm(x) = C(x) × M(x)**

- C(x) en mol/L
- Cm(x) en g/L
- M(x) en g/mol

## III- Dilution d'une solution aqueuse

**Diluer** une solution aqueuse, c'est ajouter de l'eau distillée (le solvant) à un volume donné de cette solution pour obtenir une nouvelle solution moins concentrée.
- La solution de départ est appelée **solution mère**.
- La solution diluée obtenue est appelée **solution fille**.

La concentration molaire C_fille de la solution fille est toujours inférieure à la concentration molaire C_mère de la solution mère (C_fille < C_mère).

**Conservation de la quantité de matière lors d'une dilution :**
Lors d'une dilution, on ajoute seulement du solvant (eau). La quantité de matière de soluté prélevée dans la solution mère se retrouve intégralement dans la solution fille. La quantité de matière de soluté est donc conservée.
**n(soluté) = n(mère) = n(fille)**

Soit :
- C_mère : concentration molaire de la solution mère
- V_mère : volume de solution mère prélevé
- C_fille : concentration molaire de la solution fille
- V_fille : volume total de la solution fille fabriquée

On a n(mère) = C_mère × V_mère et n(fille) = C_fille × V_fille.
Comme n(mère) = n(fille), on obtient la relation de dilution :

**C_mère × V_mère = C_fille × V_fille**

Cette relation permet de calculer l'une des quatre grandeurs si les trois autres sont connues.

### Protocole d'une préparation de solution par dilution

Préparer une solution fille de volume V_fille et de concentration C_fille à partir d'une solution mère de concentration C_mère. (On calcule d'abord le volume V_mère à prélever en utilisant V_mère = (C_fille × V_fille) / C_mère).

1.  **Prélever la solution mère :**
    - Verser un peu de solution mère dans un bécher propre.
    - Prélever le volume V_mère calculé de solution mère à l'aide d'une **pipette jaugée** de volume approprié (préalablement rincée avec la solution mère). Utiliser une propipette ou une poire à pipeter pour aspirer la solution jusqu'au trait de jauge supérieur de la pipette.
    *Image 1 : Une pipette jaugée est utilisée pour prélever un volume précis de solution mère (liquide bleu) contenue dans un bécher.*

2.  **Transférer dans la fiole jaugée :**
    - Verser le volume V_mère prélevé dans une **fiole jaugée** propre, de volume V_fille (le volume final souhaité de la solution fille).
    *Image 2 : Le contenu de la pipette jaugée (solution mère) est vidé dans une fiole jaugée vide.*

3.  **Ajouter de l'eau distillée et compléter :**
    - Ajouter de l'eau distillée dans la fiole jaugée jusqu'à environ la moitié ou les deux tiers.
    - Boucher la fiole et agiter doucement pour mélanger.
    - Ajouter ensuite de l'eau distillée avec une pissette, en terminant avec un compte-gouttes ou une pissette à jet fin, jusqu'à ce que le bas du ménisque du liquide coïncide exactement avec le **trait de jauge** de la fiole jaugée.
    *Image 3 : De l'eau distillée contenue dans une pissette est ajoutée dans la fiole jaugée contenant la solution mère prélevée. Le niveau monte vers le trait de jauge indiqué sur le col de la fiole.*

4.  **Homogénéiser :**
    - Boucher soigneusement la fiole jaugée.
    - Retourner la fiole plusieurs fois (environ 10 fois) en la maintenant bouchée pour **homogénéiser** parfaitement la solution fille.
    *Image 4 : La fiole jaugée, remplie jusqu'au trait et bouchée, est retournée plusieurs fois (indiqué par des flèches courbes) pour assurer un mélange homogène de la solution fille finale.*

La solution fille de concentration C_fille et de volume V_fille est prête.

# Page 1
"""
