"""
Complete element data for the periodic table visualizer
"""

ELEMENTS = {
    1: {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "atomic_weight": 1.008,
        "category": "diatomic nonmetal", "group": 1, "period": 1, "block": "s",
        "state": "Gas", "melting_point": -259.16, "boiling_point": -252.879,
        "density": 0.00008988, "discoverer": "Henry Cavendish", "year": 1766,
        "electron_config": "1s1", "electronegativity": 2.20, "color": "#FFFFFF"},
    
    2: {"name": "Helium", "symbol": "He", "atomic_number": 2, "atomic_weight": 4.0026,
        "category": "noble gas", "group": 18, "period": 1, "block": "s",
        "state": "Gas", "melting_point": -272.2, "boiling_point": -268.928,
        "density": 0.0001785, "discoverer": "Pierre Janssen", "year": 1868,
        "electron_config": "1s2", "electronegativity": None, "color": "#D9FFFF"},

    3: {
        "name": "Lithium", "symbol": "Li", "atomic_number": 3, "atomic_weight": 6.94,
        "category": "alkali metal", "group": 1, "period": 2, "block": "s",
        "state": "Solid", "melting_point": 180.54, "boiling_point": 1342,
        "density": 0.534, "discoverer": "Johan August Arfwedson", "year": 1817,
        "electron_config": "[He] 2s1", "electronegativity": 0.98, "color": "#CC80FF"
    },
    4: {
        "name": "Beryllium", "symbol": "Be", "atomic_number": 4, "atomic_weight": 9.0122,
        "category": "alkaline earth metal", "group": 2, "period": 2, "block": "s",
        "state": "Solid", "melting_point": 1287, "boiling_point": 2470,
        "density": 1.85, "discoverer": "Louis-Nicolas Vauquelin", "year": 1798,
        "electron_config": "[He] 2s2", "electronegativity": 1.57, "color": "#C2FF00"
    },
    5: {
        "name": "Boron", "symbol": "B", "atomic_number": 5, "atomic_weight": 10.81,
        "category": "metalloid", "group": 13, "period": 2, "block": "p",
        "state": "Solid", "melting_point": 2075, "boiling_point": 4000,
        "density": 2.34, "discoverer": "Joseph Louis Gay-Lussac", "year": 1808,
        "electron_config": "[He] 2s2 2p1", "electronegativity": 2.04, "color": "#FFB5B5"
    },
    6: {
        "name": "Carbon", "symbol": "C", "atomic_number": 6, "atomic_weight": 12.011,
        "category": "polyatomic nonmetal", "group": 14, "period": 2, "block": "p",
        "state": "Solid", "melting_point": 3550, "boiling_point": 4827,
        "density": 2.267, "discoverer": "Ancient (Egyptians)", "year": "Ancient",
        "electron_config": "[He] 2s2 2p2", "electronegativity": 2.55, "color": "#909090"
    },
    7: {
        "name": "Nitrogen", "symbol": "N", "atomic_number": 7, "atomic_weight": 14.007,
        "category": "diatomic nonmetal", "group": 15, "period": 2, "block": "p",
        "state": "Gas", "melting_point": -210.0, "boiling_point": -195.795,
        "density": 0.0012506, "discoverer": "Daniel Rutherford", "year": 1772,
        "electron_config": "[He] 2s2 2p3", "electronegativity": 3.04, "color": "#3050F8"
    },
    8: {
        "name": "Oxygen", "symbol": "O", "atomic_number": 8, "atomic_weight": 15.999,
        "category": "diatomic nonmetal", "group": 16, "period": 2, "block": "p",
        "state": "Gas", "melting_point": -218.79, "boiling_point": -182.962,
        "density": 0.001429, "discoverer": "Carl Wilhelm Scheele", "year": 1772,
        "electron_config": "[He] 2s2 2p4", "electronegativity": 3.44, "color": "#FF0D0D"
    },
    9: {
        "name": "Fluorine", "symbol": "F", "atomic_number": 9, "atomic_weight": 18.998,
        "category": "halogen", "group": 17, "period": 2, "block": "p",
        "state": "Gas", "melting_point": -219.67, "boiling_point": -188.11,
        "density": 0.001696, "discoverer": "Henri Moissan", "year": 1886,
        "electron_config": "[He] 2s2 2p5", "electronegativity": 3.98, "color": "#90E050"
    },
    10: {
        "name": "Neon", "symbol": "Ne", "atomic_number": 10, "atomic_weight": 20.180,
        "category": "noble gas", "group": 18, "period": 2, "block": "p",
        "state": "Gas", "melting_point": -248.59, "boiling_point": -246.046,
        "density": 0.0008999, "discoverer": "William Ramsay", "year": 1898,
        "electron_config": "[He] 2s2 2p6", "electronegativity": None, "color": "#B3E3F5"
    },
    11: {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "atomic_weight": 22.990,
          "category": "alkali metal", "group": 1, "period": 3, "block": "s",
          "state": "Solid", "melting_point": 97.79, "boiling_point": 883,
          "density": 0.968, "discoverer": "Humphry Davy", "year": 1807,
          "electron_config": "[Ne] 3s1", "electronegativity": 0.93, "color": "#7878F8"},    

    12: {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "atomic_weight": 24.305,
          "category": "alkaline earth metal", "group": 2, "period": 3, "block": "s",        
            "state": "Solid", "melting_point": 650, "boiling_point": 1090,  
            "density": 1.738, "discoverer": "Joseph Black", "year": 1755,
            "electron_config": "[Ne] 3s2", "electronegativity": 1.31, "color": "#F8D030"},
    13: {"name": "Aluminum", "symbol": "Al", "atomic_number": 13, "atomic_weight": 26.982,
            "category": "post-transition metal", "group": 13, "period": 3, "block": "p",
            "state": "Solid", "melting_point": 660.32, "boiling_point": 2519,
            "density": 2.70, "discoverer": "Hans Christian Ørsted", "year": 1825,
            "electron_config": "[Ne] 3s2 3p1", "electronegativity": 1.61, "color": "#BFC2C7"},
    14: {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "atomic_weight": 28.085,
            "category": "metalloid", "group": 14, "period": 3, "block": "p",
            "state": "Solid", "melting_point": 1414, "boiling_point": 2900,
            "density": 2.329, "discoverer": "Jöns Jacob Berzelius", "year": 1824,
            "electron_config": "[Ne] 3s2 3p2", "electronegativity": 1.90, "color": "#F0C8A0"},  
            
    15: {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "atomic_weight": 30.974,
            "category": "polyatomic nonmetal", "group": 15, "period": 3, "block": "p",
            "state": "Solid", "melting_point": 44.15, "boiling_point": 280.5,
            "density": 1.82, "discoverer": "Hennig Brand", "year": 1669,
            "electron_config": "[Ne] 3s2 3p3", "electronegativity": 2.19, "color": "#FF8000"},
    
    16: {
        "name": "Sulfur", "symbol": "S", "atomic_number": 16, "atomic_weight": 32.06,
        "category": "polyatomic nonmetal", "group": 16, "period": 3, "block": "p",
        "state": "Solid", "melting_point": 115.21, "boiling_point": 444.61,
        "density": 2.07, "discoverer": "Ancient (China/India)", "year": "Ancient",
        "electron_config": "[Ne] 3s2 3p4", "electronegativity": 2.58, "color": "#FFFF30"
    },
    17: {
        "name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "atomic_weight": 35.45,
        "category": "diatomic nonmetal", "group": 17, "period": 3, "block": "p",
        "state": "Gas", "melting_point": -101.5, "boiling_point": -34.04,
        "density": 0.003214, "discoverer": "Carl Wilhelm Scheele", "year": 1774,
        "electron_config": "[Ne] 3s2 3p5", "electronegativity": 3.16, "color": "#1FF01F"
    },

    # Noble Gas (18)
    18: {
        "name": "Argon", "symbol": "Ar", "atomic_number": 18, "atomic_weight": 39.948,
        "category": "noble gas", "group": 18, "period": 3, "block": "p",
        "state": "Gas", "melting_point": -189.34, "boiling_point": -185.85,
        "density": 0.0017837, "discoverer": "Lord Rayleigh", "year": 1894,
        "electron_config": "[Ne] 3s2 3p6", "electronegativity": None, "color": "#80D1E3"
    },

    # Alkali & Alkaline Earth (19-20)
    19: {
        "name": "Potassium", "symbol": "K", "atomic_number": 19, "atomic_weight": 39.098,
        "category": "alkali metal", "group": 1, "period": 4, "block": "s",
        "state": "Solid", "melting_point": 63.5, "boiling_point": 759,
        "density": 0.89, "discoverer": "Humphry Davy", "year": 1807,
        "electron_config": "[Ar] 4s1", "electronegativity": 0.82, "color": "#8F40D4"
    },
    20: {
        "name": "Calcium", "symbol": "Ca", "atomic_number": 20, "atomic_weight": 40.078,
        "category": "alkaline earth metal", "group": 2, "period": 4, "block": "s",
        "state": "Solid", "melting_point": 842, "boiling_point": 1484,
        "density": 1.55, "discoverer": "Humphry Davy", "year": 1808,
        "electron_config": "[Ar] 4s2", "electronegativity": 1.00, "color": "#3DFF00"
    },

    # Transition Metals (21-30)
    21: {
        "name": "Scandium", "symbol": "Sc", "atomic_number": 21, "atomic_weight": 44.956,
        "category": "transition metal", "group": 3, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1541, "boiling_point": 2836,
        "density": 2.99, "discoverer": "Lars Fredrik Nilson", "year": 1879,
        "electron_config": "[Ar] 3d1 4s2", "electronegativity": 1.36, "color": "#E6E6E6"
    },
    22: {
        "name": "Titanium", "symbol": "Ti", "atomic_number": 22, "atomic_weight": 47.867,
        "category": "transition metal", "group": 4, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1668, "boiling_point": 3287,
        "density": 4.54, "discoverer": "William Gregor", "year": 1791,
        "electron_config": "[Ar] 3d2 4s2", "electronegativity": 1.54, "color": "#BFC2C7"
    },
    23: {
        "name": "Vanadium", "symbol": "V", "atomic_number": 23, "atomic_weight": 50.942,
        "category": "transition metal", "group": 5, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1910, "boiling_point": 3407,
        "density": 6.11, "discoverer": "Andrés Manuel del Río", "year": 1801,
        "electron_config": "[Ar] 3d3 4s2", "electronegativity": 1.63, "color": "#A6A6AB"
    },
    24: {
        "name": "Chromium", "symbol": "Cr", "atomic_number": 24, "atomic_weight": 51.996,
        "category": "transition metal", "group": 6, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1907, "boiling_point": 2671,
        "density": 7.15, "discoverer": "Louis Nicolas Vauquelin", "year": 1797,
        "electron_config": "[Ar] 3d5 4s1", "electronegativity": 1.66, "color": "#8A99C7"
    },
    25: {
        "name": "Manganese", "symbol": "Mn", "atomic_number": 25, "atomic_weight": 54.938,
        "category": "transition metal", "group": 7, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1246, "boiling_point": 2061,
        "density": 7.44, "discoverer": "Johan Gottlieb Gahn", "year": 1774,
        "electron_config": "[Ar] 3d5 4s2", "electronegativity": 1.55, "color": "#9C7AC7"
    },
    26: {
        "name": "Iron", "symbol": "Fe", "atomic_number": 26, "atomic_weight": 55.845,
        "category": "transition metal", "group": 8, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1538, "boiling_point": 2862,
        "density": 7.87, "discoverer": "Ancient (5000 BCE)", "year": "Ancient",
        "electron_config": "[Ar] 3d6 4s2", "electronegativity": 1.83, "color": "#E06633"
    },
    27: {
        "name": "Cobalt", "symbol": "Co", "atomic_number": 27, "atomic_weight": 58.933,
        "category": "transition metal", "group": 9, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1495, "boiling_point": 2927,
        "density": 8.90, "discoverer": "Georg Brandt", "year": 1735,
        "electron_config": "[Ar] 3d7 4s2", "electronegativity": 1.88, "color": "#F090A0"
    },
    28: {
        "name": "Nickel", "symbol": "Ni", "atomic_number": 28, "atomic_weight": 58.693,
        "category": "transition metal", "group": 10, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1455, "boiling_point": 2913,
        "density": 8.91, "discoverer": "Axel Fredrik Cronstedt", "year": 1751,
        "electron_config": "[Ar] 3d8 4s2", "electronegativity": 1.91, "color": "#50D050"
    },
    29: {
        "name": "Copper", "symbol": "Cu", "atomic_number": 29, "atomic_weight": 63.546,
        "category": "transition metal", "group": 11, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 1085, "boiling_point": 2562,
        "density": 8.96, "discoverer": "Ancient (9000 BCE)", "year": "Ancient",
        "electron_config": "[Ar] 3d10 4s1", "electronegativity": 1.90, "color": "#C88033"
    },
    30: {
        "name": "Zinc", "symbol": "Zn", "atomic_number": 30, "atomic_weight": 65.38,
        "category": "transition metal", "group": 12, "period": 4, "block": "d",
        "state": "Solid", "melting_point": 419.53, "boiling_point": 907,
        "density": 7.13, "discoverer": "Andreas Sigismund Marggraf", "year": 1746,
        "electron_config": "[Ar] 3d10 4s2", "electronegativity": 1.65, "color": "#7D80B0"
    },

    # Post-Transition Metals & Metalloids (31-34)
    31: {
        "name": "Gallium", "symbol": "Ga", "atomic_number": 31, "atomic_weight": 69.723,
        "category": "post-transition metal", "group": 13, "period": 4, "block": "p",
        "state": "Solid", "melting_point": 29.76, "boiling_point": 2204,
        "density": 5.91, "discoverer": "Paul-Émile Lecoq de Boisbaudran", "year": 1875,
        "electron_config": "[Ar] 3d10 4s2 4p1", "electronegativity": 1.81, "color": "#C28F8F"
    },
    32: {
        "name": "Germanium", "symbol": "Ge", "atomic_number": 32, "atomic_weight": 72.630,
        "category": "metalloid", "group": 14, "period": 4, "block": "p",
        "state": "Solid", "melting_point": 938.25, "boiling_point": 2833,
        "density": 5.32, "discoverer": "Clemens Winkler", "year": 1886,
        "electron_config": "[Ar] 3d10 4s2 4p2", "electronegativity": 2.01, "color": "#668F8F"
    },
    33: {
        "name": "Arsenic", "symbol": "As", "atomic_number": 33, "atomic_weight": 74.922,
        "category": "metalloid", "group": 15, "period": 4, "block": "p",
        "state": "Solid", "melting_point": 817, "boiling_point": 614,
        "density": 5.73, "discoverer": "Albertus Magnus", "year": 1250,
        "electron_config": "[Ar] 3d10 4s2 4p3", "electronegativity": 2.18, "color": "#BD80E3"
    },
    34: {
        "name": "Selenium", "symbol": "Se", "atomic_number": 34, "atomic_weight": 78.971,
        "category": "polyatomic nonmetal", "group": 16, "period": 4, "block": "p",
        "state": "Solid", "melting_point": 221, "boiling_point": 685,
        "density": 4.81, "discoverer": "Jöns Jacob Berzelius", "year": 1817,
        "electron_config": "[Ar] 3d10 4s2 4p4", "electronegativity": 2.55, "color": "#FFA100"
    },

    # Halogen & Noble Gas (35-36)
    35: {
        "name": "Bromine", "symbol": "Br", "atomic_number": 35, "atomic_weight": 79.904,
        "category": "diatomic nonmetal", "group": 17, "period": 4, "block": "p",
        "state": "Liquid", "melting_point": -7.2, "boiling_point": 58.8,
        "density": 3.12, "discoverer": "Antoine Jérôme Balard", "year": 1826,
        "electron_config": "[Ar] 3d10 4s2 4p5", "electronegativity": 2.96, "color": "#A62929"
    },
    36: {
        "name": "Krypton", "symbol": "Kr", "atomic_number": 36, "atomic_weight": 83.798,
        "category": "noble gas", "group": 18, "period": 4, "block": "p",
        "state": "Gas", "melting_point": -157.37, "boiling_point": -153.22,
        "density": 0.003733, "discoverer": "William Ramsay", "year": 1898,
        "electron_config": "[Ar] 3d10 4s2 4p6", "electronegativity": 3.00, "color": "#5CB8D1"
    },

    # Alkali & Alkaline Earth (37-38)
    37: {
        "name": "Rubidium", "symbol": "Rb", "atomic_number": 37, "atomic_weight": 85.468,
        "category": "alkali metal", "group": 1, "period": 5, "block": "s",
        "state": "Solid", "melting_point": 39.31, "boiling_point": 688,
        "density": 1.53, "discoverer": "Robert Bunsen", "year": 1861,
        "electron_config": "[Kr] 5s1", "electronegativity": 0.82, "color": "#702EB0"
    },
    38: {
        "name": "Strontium", "symbol": "Sr", "atomic_number": 38, "atomic_weight": 87.62,
        "category": "alkaline earth metal", "group": 2, "period": 5, "block": "s",
        "state": "Solid", "melting_point": 777, "boiling_point": 1382,
        "density": 2.64, "discoverer": "William Cruickshank", "year": 1787,
        "electron_config": "[Kr] 5s2", "electronegativity": 0.95, "color": "#00FF00"
    },

    # Transition Metals (39-48)
    39: {
        "name": "Yttrium", "symbol": "Y", "atomic_number": 39, "atomic_weight": 88.906,
        "category": "transition metal", "group": 3, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 1526, "boiling_point": 3345,
        "density": 4.47, "discoverer": "Johan Gadolin", "year": 1794,
        "electron_config": "[Kr] 4d1 5s2", "electronegativity": 1.22, "color": "#94FFFF"
    },
    40: {
        "name": "Zirconium", "symbol": "Zr", "atomic_number": 40, "atomic_weight": 91.224,
        "category": "transition metal", "group": 4, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 1855, "boiling_point": 4409,
        "density": 6.52, "discoverer": "Martin Heinrich Klaproth", "year": 1789,
        "electron_config": "[Kr] 4d2 5s2", "electronegativity": 1.33, "color": "#94E0E0"
    },
    41: {
        "name": "Niobium", "symbol": "Nb", "atomic_number": 41, "atomic_weight": 92.906,
        "category": "transition metal", "group": 5, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 2477, "boiling_point": 4744,
        "density": 8.57, "discoverer": "Charles Hatchett", "year": 1801,
        "electron_config": "[Kr] 4d4 5s1", "electronegativity": 1.6, "color": "#73C2C9"
    },
    42: {
        "name": "Molybdenum", "symbol": "Mo", "atomic_number": 42, "atomic_weight": 95.95,
        "category": "transition metal", "group": 6, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 2623, "boiling_point": 4639,
        "density": 10.22, "discoverer": "Carl Wilhelm Scheele", "year": 1778,
        "electron_config": "[Kr] 4d5 5s1", "electronegativity": 2.16, "color": "#54B5B5"
    },
    43: {
        "name": "Technetium", "symbol": "Tc", "atomic_number": 43, "atomic_weight": 98,
        "category": "transition metal", "group": 7, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 2157, "boiling_point": 4265,
        "density": 11.50, "discoverer": "Emilio Segrè", "year": 1937,
        "electron_config": "[Kr] 4d5 5s2", "electronegativity": 1.9, "color": "#3B9E9E"
    },
    44: {
        "name": "Ruthenium", "symbol": "Ru", "atomic_number": 44, "atomic_weight": 101.07,
        "category": "transition metal", "group": 8, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 2334, "boiling_point": 4150,
        "density": 12.45, "discoverer": "Karl Ernst Claus", "year": 1844,
        "electron_config": "[Kr] 4d7 5s1", "electronegativity": 2.2, "color": "#248F8F"
    },
    45: {
        "name": "Rhodium", "symbol": "Rh", "atomic_number": 45, "atomic_weight": 102.91,
        "category": "transition metal", "group": 9, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 1964, "boiling_point": 3695,
        "density": 12.41, "discoverer": "William Hyde Wollaston", "year": 1803,
        "electron_config": "[Kr] 4d8 5s1", "electronegativity": 2.28, "color": "#0A7D8C"
    },
    46: {
        "name": "Palladium", "symbol": "Pd", "atomic_number": 46, "atomic_weight": 106.42,
        "category": "transition metal", "group": 10, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 1554.9, "boiling_point": 2963,
        "density": 12.02, "discoverer": "William Hyde Wollaston", "year": 1803,
        "electron_config": "[Kr] 4d10", "electronegativity": 2.20, "color": "#6985A8"
    },
    47: {
        "name": "Silver", "symbol": "Ag", "atomic_number": 47, "atomic_weight": 107.87,
        "category": "transition metal", "group": 11, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 961.78, "boiling_point": 2162,
        "density": 10.49, "discoverer": "Ancient (3000 BCE)", "year": "Ancient",
        "electron_config": "[Kr] 4d10 5s1", "electronegativity": 1.93, "color": "#C0C0C0"
    },
    48: {
        "name": "Cadmium", "symbol": "Cd", "atomic_number": 48, "atomic_weight": 112.41,
        "category": "transition metal", "group": 12, "period": 5, "block": "d",
        "state": "Solid", "melting_point": 321.07, "boiling_point": 767,
        "density": 8.65, "discoverer": "Karl Samuel Leberecht Hermann", "year": 1817,
        "electron_config": "[Kr] 4d10 5s2", "electronegativity": 1.69, "color": "#FFD98F"
    },

    # Post-Transition Metals & Metalloids (49-50)
    49: {
        "name": "Indium", "symbol": "In", "atomic_number": 49, "atomic_weight": 114.82,
        "category": "post-transition metal", "group": 13, "period": 5, "block": "p",
        "state": "Solid", "melting_point": 156.60, "boiling_point": 2072,
        "density": 7.31, "discoverer": "Ferdinand Reich", "year": 1863,
        "electron_config": "[Kr] 4d10 5s2 5p1", "electronegativity": 1.78, "color": "#A67573"
    },
    50: {
        "name": "Tin", "symbol": "Sn", "atomic_number": 50, "atomic_weight": 118.71,
        "category": "post-transition metal", "group": 14, "period": 5, "block": "p",
        "state": "Solid", "melting_point": 231.93, "boiling_point": 2602,
        "density": 7.31, "discoverer": "Ancient (3500 BCE)", "year": "Ancient",
        "electron_config": "[Kr] 4d10 5s2 5p2", "electronegativity": 1.96, "color": "#668080"
    },
    51: {
        "name": "Antimony", "symbol": "Sb", "atomic_number": 51, "atomic_weight": 121.76,
        "category": "metalloid", "group": 15, "period": 5, "block": "p",
        "state": "Solid", "melting_point": 630.63, "boiling_point": 1587,
        "density": 6.697, "discoverer": "Ancient (3000 BCE)", "year": "Ancient",
        "electron_config": "[Kr] 4d10 5s2 5p3", "electronegativity": 2.05, "color": "#9E63B5"
    },
    
    52: {
        "name": "Tellurium", "symbol": "Te", "atomic_number": 52, "atomic_weight": 127.60,
        "category": "metalloid", "group": 16, "period": 5, "block": "p",
        "state": "Solid", "melting_point": 449.51, "boiling_point": 988,
        "density": 6.24, "discoverer": "Franz-Joseph Müller von Reichenstein", "year": 1782,
        "electron_config": "[Kr] 4d10 5s2 5p4", "electronegativity": 2.1, "color": "#D47A00"
    },
    53: {
        "name": "Iodine", "symbol": "I", "atomic_number": 53, "atomic_weight": 126.90,
        "category": "diatomic nonmetal", "group": 17, "period": 5, "block": "p",
        "state": "Solid", "melting_point": 113.7, "boiling_point": 184.3,
        "density": 4.93, "discoverer": "Bernard Courtois", "year": 1811,
        "electron_config": "[Kr] 4d10 5s2 5p5", "electronegativity": 2.66, "color": "#940094"
    },
    54: {
        "name": "Xenon", "symbol": "Xe", "atomic_number": 54, "atomic_weight": 131.29,
        "category": "noble gas", "group": 18, "period": 5, "block": "p",
        "state": "Gas", "melting_point": -111.75, "boiling_point": -108.12,
        "density": 0.005887, "discoverer": "William Ramsay", "year": 1898,
        "electron_config": "[Kr] 4d10 5s2 5p6", "electronegativity": 2.6, "color": "#429EB0"
    },
    55: {
        "name": "Cesium", "symbol": "Cs", "atomic_number": 55, "atomic_weight": 132.91,
        "category": "alkali metal", "group": 1, "period": 6, "block": "s",
        "state": "Solid", "melting_point": 28.44, "boiling_point": 671,
        "density": 1.93, "discoverer": "Robert Bunsen", "year": 1860,
        "electron_config": "[Xe] 6s1", "electronegativity": 0.79, "color": "#57178F"
    },
    56: {
        "name": "Barium", "symbol": "Ba", "atomic_number": 56, "atomic_weight": 137.33,
        "category": "alkaline earth metal", "group": 2, "period": 6, "block": "s",
        "state": "Solid", "melting_point": 727, "boiling_point": 1870,
        "density": 3.51, "discoverer": "Carl Wilhelm Scheele", "year": 1772,
        "electron_config": "[Xe] 6s2", "electronegativity": 0.89, "color": "#00C900"
    },

    # Lanthanides (57-71)
    57: {
        "name": "Lanthanum", "symbol": "La", "atomic_number": 57, "atomic_weight": 138.91,
        "category": "lanthanide", "group": 3, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 920, "boiling_point": 3464,
        "density": 6.15, "discoverer": "Carl Gustaf Mosander", "year": 1839,
        "electron_config": "[Xe] 5d1 6s2", "electronegativity": 1.1, "color": "#70D4FF"
    },
    58: {
        "name": "Cerium", "symbol": "Ce", "atomic_number": 58, "atomic_weight": 140.12,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 795, "boiling_point": 3443,
        "density": 6.77, "discoverer": "Martin Heinrich Klaproth", "year": 1803,
        "electron_config": "[Xe] 4f1 5d1 6s2", "electronegativity": 1.12, "color": "#FFFFC7"
    },
    59: {
        "name": "Praseodymium", "symbol": "Pr", "atomic_number": 59, "atomic_weight": 140.91,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 935, "boiling_point": 3520,
        "density": 6.77, "discoverer": "Carl Auer von Welsbach", "year": 1885,
        "electron_config": "[Xe] 4f3 6s2", "electronegativity": 1.13, "color": "#D9FFC7"
    },
    60: {
        "name": "Neodymium", "symbol": "Nd", "atomic_number": 60, "atomic_weight": 144.24,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1024, "boiling_point": 3074,
        "density": 7.01, "discoverer": "Carl Auer von Welsbach", "year": 1885,
        "electron_config": "[Xe] 4f4 6s2", "electronegativity": 1.14, "color": "#C7FFC7"
    },
    61: {
        "name": "Promethium", "symbol": "Pm", "atomic_number": 61, "atomic_weight": 145,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1042, "boiling_point": 3000,
        "density": 7.26, "discoverer": "Jacob A. Marinsky", "year": 1945,
        "electron_config": "[Xe] 4f5 6s2", "electronegativity": 1.13, "color": "#A3FFC7"
    },
    62: {
        "name": "Samarium", "symbol": "Sm", "atomic_number": 62, "atomic_weight": 150.36,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1072, "boiling_point": 1900,
        "density": 7.52, "discoverer": "Lecoq de Boisbaudran", "year": 1879,
        "electron_config": "[Xe] 4f6 6s2", "electronegativity": 1.17, "color": "#8FFFC7"
    },
    63: {
        "name": "Europium", "symbol": "Eu", "atomic_number": 63, "atomic_weight": 151.96,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 822, "boiling_point": 1529,
        "density": 5.24, "discoverer": "Eugène-Anatole Demarçay", "year": 1901,
        "electron_config": "[Xe] 4f7 6s2", "electronegativity": 1.2, "color": "#61FFC7"
    },
    64: {
        "name": "Gadolinium", "symbol": "Gd", "atomic_number": 64, "atomic_weight": 157.25,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1312, "boiling_point": 3273,
        "density": 7.90, "discoverer": "Jean Charles Galissard de Marignac", "year": 1880,
        "electron_config": "[Xe] 4f7 5d1 6s2", "electronegativity": 1.2, "color": "#45FFC7"
    },
    65: {
        "name": "Terbium", "symbol": "Tb", "atomic_number": 65, "atomic_weight": 158.93,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1356, "boiling_point": 3230,
        "density": 8.23, "discoverer": "Carl Gustaf Mosander", "year": 1843,
        "electron_config": "[Xe] 4f9 6s2", "electronegativity": 1.2, "color": "#30FFC7"
    },
    66: {
        "name": "Dysprosium", "symbol": "Dy", "atomic_number": 66, "atomic_weight": 162.50,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1407, "boiling_point": 2567,
        "density": 8.55, "discoverer": "Lecoq de Boisbaudran", "year": 1886,
        "electron_config": "[Xe] 4f10 6s2", "electronegativity": 1.22, "color": "#1FFFC7"
    },
    67: {
        "name": "Holmium", "symbol": "Ho", "atomic_number": 67, "atomic_weight": 164.93,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1461, "boiling_point": 2720,
        "density": 8.80, "discoverer": "Marc Delafontaine", "year": 1878,
        "electron_config": "[Xe] 4f11 6s2", "electronegativity": 1.23, "color": "#00FF9C"
    },
    68: {
        "name": "Erbium", "symbol": "Er", "atomic_number": 68, "atomic_weight": 167.26,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1529, "boiling_point": 2868,
        "density": 9.07, "discoverer": "Carl Gustaf Mosander", "year": 1843,
        "electron_config": "[Xe] 4f12 6s2", "electronegativity": 1.24, "color": "#00E675"
    },
    69: {
        "name": "Thulium", "symbol": "Tm", "atomic_number": 69, "atomic_weight": 168.93,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 1545, "boiling_point": 1950,
        "density": 9.32, "discoverer": "Per Teodor Cleve", "year": 1879,
        "electron_config": "[Xe] 4f13 6s2", "electronegativity": 1.25, "color": "#00D452"
    },
    70: {
        "name": "Ytterbium", "symbol": "Yb", "atomic_number": 70, "atomic_weight": 173.05,
        "category": "lanthanide", "group": None, "period": 6, "block": "f",
        "state": "Solid", "melting_point": 819, "boiling_point": 1196,
        "density": 6.90, "discoverer": "Jean Charles Galissard de Marignac", "year": 1878,
        "electron_config": "[Xe] 4f14 6s2", "electronegativity": 1.1, "color": "#00BF38"
    },
    71: {
        "name": "Lutetium", "symbol": "Lu", "atomic_number": 71, "atomic_weight": 174.97,
        "category": "lanthanide", "group": 3, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 1663, "boiling_point": 3402,
        "density": 9.84, "discoverer": "Georges Urbain", "year": 1907,
        "electron_config": "[Xe] 4f14 5d1 6s2", "electronegativity": 1.27, "color": "#00AB24"
    },

    # Transition Metals (72-80)
    72: {
        "name": "Hafnium", "symbol": "Hf", "atomic_number": 72, "atomic_weight": 178.49,
        "category": "transition metal", "group": 4, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 2233, "boiling_point": 4603,
        "density": 13.31, "discoverer": "Dirk Coster", "year": 1923,
        "electron_config": "[Xe] 4f14 5d2 6s2", "electronegativity": 1.3, "color": "#4DC2FF"
    },

    73: {
        "name": "Tantalum", "symbol": "Ta", "atomic_number": 73, "atomic_weight": 180.95,
        "category": "transition metal", "group": 5, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 3017, "boiling_point": 5458,
        "density": 16.65, "discoverer": "Anders Gustaf Ekeberg", "year": 1802,
        "electron_config": "[Xe] 4f14 5d3 6s2", "electronegativity": 1.5, "color": "#4DA6FF"
    },
    74: {
        "name": "Tungsten", "symbol": "W", "atomic_number": 74, "atomic_weight": 183.84,
        "category": "transition metal", "group": 6, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 3422, "boiling_point": 5555,
        "density": 19.25, "discoverer": "Juan José and Fausto Elhuyar", "year": 1783,
        "electron_config": "[Xe] 4f14 5d4 6s2", "electronegativity": 2.36, "color": "#2194D6"
    },
    75: {
        "name": "Rhenium", "symbol": "Re", "atomic_number": 75, "atomic_weight": 186.21,
        "category": "transition metal", "group": 7, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 3186, "boiling_point": 5596,
        "density": 21.02, "discoverer": "Walter Noddack, Ida Tacke, Otto Berg", "year": 1925,
        "electron_config": "[Xe] 4f14 5d5 6s2", "electronegativity": 1.9, "color": "#267DAB"
    },
    76: {
        "name": "Osmium", "symbol": "Os", "atomic_number": 76, "atomic_weight": 190.23,
        "category": "transition metal", "group": 8, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 3033, "boiling_point": 5012,
        "density": 22.59, "discoverer": "Smithson Tennant", "year": 1803,
        "electron_config": "[Xe] 4f14 5d6 6s2", "electronegativity": 2.2, "color": "#266696"
    },
    77: {
        "name": "Iridium", "symbol": "Ir", "atomic_number": 77, "atomic_weight": 192.22,
        "category": "transition metal", "group": 9, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 2446, "boiling_point": 4428,
        "density": 22.56, "discoverer": "Smithson Tennant", "year": 1803,
        "electron_config": "[Xe] 4f14 5d7 6s2", "electronegativity": 2.2, "color": "#175487"
    },
    78: {
        "name": "Platinum", "symbol": "Pt", "atomic_number": 78, "atomic_weight": 195.08,
        "category": "transition metal", "group": 10, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 1768, "boiling_point": 3825,
        "density": 21.45, "discoverer": "Antonio de Ulloa", "year": 1735,
        "electron_config": "[Xe] 4f14 5d9 6s1", "electronegativity": 2.28, "color": "#D0D0E0"
    },
    79: {
        "name": "Gold", "symbol": "Au", "atomic_number": 79, "atomic_weight": 196.97,
        "category": "transition metal", "group": 11, "period": 6, "block": "d",
        "state": "Solid", "melting_point": 1064, "boiling_point": 2856,
        "density": 19.32, "discoverer": "Known since ancient times", "year": "Ancient",
        "electron_config": "[Xe] 4f14 5d10 6s1", "electronegativity": 2.54, "color": "#FFD123"
    },
    80: {
        "name": "Mercury", "symbol": "Hg", "atomic_number": 80, "atomic_weight": 200.59,
        "category": "transition metal", "group": 12, "period": 6, "block": "d",
        "state": "Liquid", "melting_point": -38.83, "boiling_point": 356.73,
        "density": 13.534, "discoverer": "Known since ancient times", "year": "Ancient",
        "electron_config": "[Xe] 4f14 5d10 6s2", "electronegativity": 2.0, "color": "#B8B8D0"
    },
    81: {
        "name": "Thallium", "symbol": "Tl", "atomic_number": 81, "atomic_weight": 204.38,
        "category": "post-transition metal", "group": 13, "period": 6, "block": "p",
        "state": "Solid", "melting_point": 304, "boiling_point": 1473,
        "density": 11.85, "discoverer": "William Crookes", "year": 1861,
        "electron_config": "[Xe] 4f14 5d10 6s2 6p1", "electronegativity": 1.62, "color": "#A6544D"
    },
    82: {
        "name": "Lead", "symbol": "Pb", "atomic_number": 82, "atomic_weight": 207.2,
        "category": "post-transition metal", "group": 14, "period": 6, "block": "p",
        "state": "Solid", "melting_point": 327.46, "boiling_point": 1749,
        "density": 11.34, "discoverer": "Known since ancient times", "year": "Ancient",
        "electron_config": "[Xe] 4f14 5d10 6s2 6p2", "electronegativity": 2.33, "color": "#575961"
    },
    83: {
        "name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "atomic_weight": 208.98,
        "category": "post-transition metal", "group": 15, "period": 6, "block": "p",
        "state": "Solid", "melting_point": 271.5, "boiling_point": 1564,
        "density": 9.78, "discoverer": "Claude François Geoffroy", "year": 1753,
        "electron_config": "[Xe] 4f14 5d10 6s2 6p3", "electronegativity": 2.02, "color": "#9E4FB5"
    },
    84: {
        "name": "Polonium", "symbol": "Po", "atomic_number": 84, "atomic_weight": 209,
        "category": "metalloid", "group": 16, "period": 6, "block": "p",
        "state": "Solid", "melting_point": 254, "boiling_point": 962,
        "density": 9.196, "discoverer": "Marie Curie", "year": 1898,
        "electron_config": "[Xe] 4f14 5d10 6s2 6p4", "electronegativity": 2.0, "color": "#AB5C00"
    },
    85: {
        "name": "Astatine", "symbol": "At", "atomic_number": 85, "atomic_weight": 210,
        "category": "halogen", "group": 17, "period": 6, "block": "p",
        "state": "Solid", "melting_point": 302, "boiling_point": 337,
        "density": 7, "discoverer": "Dale R. Corson, Kenneth Ross MacKenzie, Emilio Segrè", "year": 1940,
        "electron_config": "[Xe] 4f14 5d10 6s2 6p5", "electronegativity": 2.2, "color": "#754F45"
    },
    86: {
        "name": "Radon", "symbol": "Rn", "atomic_number": 86, "atomic_weight": 222,
        "category": "noble gas", "group": 18, "period": 6, "block": "p",
        "state": "Gas", "melting_point": -71, "boiling_point": -61.7,
        "density": 0.00973, "discoverer": "Friedrich Ernst Dorn", "year": 1900,
        "electron_config": "[Xe] 4f14 5d10 6s2 6p6", "electronegativity": 2.2, "color": "#428296"
    },
    87: {
        "name": "Francium", "symbol": "Fr", "atomic_number": 87, "atomic_weight": 223,
        "category": "alkali metal", "group": 1, "period": 7, "block": "s",
        "state": "Solid", "melting_point": 27, "boiling_point": 677,
        "density": 1.87, "discoverer": "Marguerite Perey", "year": 1939,
        "electron_config": "[Rn] 7s1", "electronegativity": 0.7, "color": "#420066"
    },
    88: {
        "name": "Radium", "symbol": "Ra", "atomic_number": 88, "atomic_weight": 226,
        "category": "alkaline earth metal", "group": 2, "period": 7, "block": "s",
        "state": "Solid", "melting_point": 700, "boiling_point": 1737,
        "density": 5.5, "discoverer": "Marie Curie, Pierre Curie", "year": 1898,
        "electron_config": "[Rn] 7s2", "electronegativity": 0.9, "color": "#007D00"
    },
    89: {
            "name": "Actinium", "symbol": "Ac", "atomic_number": 89, "atomic_weight": 227,
            "category": "actinide", "group": 3, "period": 7, "block": "f",
            "state": "Solid", "melting_point": 1050, "boiling_point": 3200,
            "density": 10.07, "discoverer": "André-Louis Debierne", "year": 1899,
            "electron_config": "[Rn] 6d1 7s2", "electronegativity": 1.1, "color": "#70ABFA"
        },
    90: {
        "name": "Thorium", "symbol": "Th", "atomic_number": 90, "atomic_weight": 232.04,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1750, "boiling_point": 4788,
        "density": 11.72, "discoverer": "Jöns Jakob Berzelius", "year": 1828,
        "electron_config": "[Rn] 6d2 7s2", "electronegativity": 1.3, "color": "#00BAFF"
    },
    91: {
        "name": "Protactinium", "symbol": "Pa", "atomic_number": 91, "atomic_weight": 231.04,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1568, "boiling_point": 4027,
        "density": 15.37, "discoverer": "William Crookes, Kasimir Fajans, Otto Hahn", "year": 1913,
        "electron_config": "[Rn] 5f2 6d1 7s2", "electronegativity": 1.5, "color": "#00A1FF"
    },
    92: {
        "name": "Uranium", "symbol": "U", "atomic_number": 92, "atomic_weight": 238.03,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1132, "boiling_point": 4131,
        "density": 19.05, "discoverer": "Martin Heinrich Klaproth", "year": 1789,
        "electron_config": "[Rn] 5f3 6d1 7s2", "electronegativity": 1.38, "color": "#008FFF"
    },
    93: {
        "name": "Neptunium", "symbol": "Np", "atomic_number": 93, "atomic_weight": 237,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 644, "boiling_point": 3902,
        "density": 20.45, "discoverer": "Edwin McMillan, Philip H. Abelson", "year": 1940,
        "electron_config": "[Rn] 5f4 6d1 7s2", "electronegativity": 1.36, "color": "#0080FF"
    },
    94: {
        "name": "Plutonium", "symbol": "Pu", "atomic_number": 94, "atomic_weight": 244,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 639.4, "boiling_point": 3228,
        "density": 19.84, "discoverer": "Glenn T. Seaborg, Arthur Wahl, Joseph W. Kennedy, Edwin McMillan", "year": 1940,
        "electron_config": "[Rn] 5f6 7s2", "electronegativity": 1.28, "color": "#006BFF"
    },
    95: {
        "name": "Americium", "symbol": "Am", "atomic_number": 95, "atomic_weight": 243,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1176, "boiling_point": 2011,
        "density": 13.69, "discoverer": "Glenn T. Seaborg, Ralph A. James, Leon O. Morgan, Albert Ghiorso", "year": 1944,
        "electron_config": "[Rn] 5f7 7s2", "electronegativity": 1.13, "color": "#545CF2"
    },
    96: {
        "name": "Curium", "symbol": "Cm", "atomic_number": 96, "atomic_weight": 247,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1340, "boiling_point": 3110,
        "density": 13.51, "discoverer": "Glenn T. Seaborg, Ralph A. James, Albert Ghiorso", "year": 1944,
        "electron_config": "[Rn] 5f7 6d1 7s2", "electronegativity": 1.28, "color": "#785CE3"
    },
    97: {
        "name": "Berkelium", "symbol": "Bk", "atomic_number": 97, "atomic_weight": 247,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 986, "boiling_point": 2627,
        "density": 14.78, "discoverer": "Glenn T. Seaborg, Stanley G. Thompson, Albert Ghiorso", "year": 1949,
        "electron_config": "[Rn] 5f9 7s2", "electronegativity": 1.3, "color": "#8A4FE3"
    },
    98: {
        "name": "Californium", "symbol": "Cf", "atomic_number": 98, "atomic_weight": 251,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 900, "boiling_point": 1470,
        "density": 15.1, "discoverer": "Glenn T. Seaborg, Stanley G. Thompson, Kenneth Street Jr., Albert Ghiorso", "year": 1950,
        "electron_config": "[Rn] 5f10 7s2", "electronegativity": 1.3, "color": "#A136D4"
    },
    99: {
        "name": "Einsteinium", "symbol": "Es", "atomic_number": 99, "atomic_weight": 252,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 860, "boiling_point": 996,
        "density": 8.84, "discoverer": "Albert Ghiorso et al.", "year": 1952,
        "electron_config": "[Rn] 5f11 7s2", "electronegativity": 1.3, "color": "#B31FD4"
    },
    100: {
        "name": "Fermium", "symbol": "Fm", "atomic_number": 100, "atomic_weight": 257,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 1527, "boiling_point": None,
        "density": None, "discoverer": "Albert Ghiorso et al.", "year": 1952,
        "electron_config": "[Rn] 5f12 7s2", "electronegativity": 1.3, "color": "#B31FBA"
    },
    # Actinides (101-103), Transactinides (104-117)
    101: {
        "name": "Mendelevium", "symbol": "Md", "atomic_number": 101, "atomic_weight": 258,
        "category": "actinide","group": None, "period": 7, "block": "f","state": 
        "Solid", "melting_point": 827, "boiling_point": None,
        "density": None, "discoverer": "Albert Ghiorso, Glenn T. Seaborg et al.", "year": 1955,
        "electron_config": "[Rn] 5f13 7s2", "electronegativity": 1.3, "color": "#B30DA2"
    },
    102: {
        "name": "Nobelium", "symbol": "No", "atomic_number": 102, "atomic_weight": 259,
        "category": "actinide", "group": None, "period": 7, "block": "f",
        "state": "Solid", "melting_point": 827, "boiling_point": None,
        "density": None, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 1966,
        "electron_config": "[Rn] 5f14 7s2", "electronegativity": 1.3, "color": "#BD0096"
    },
    103: {
        "name": "Lawrencium", "symbol": "Lr", "atomic_number": 103, "atomic_weight": 262,
        "category": "actinide", "group": 3, "period": 7, "block": "d",
        "state": "Solid", "melting_point": 1627, "boiling_point": None,
        "density": None, "discoverer": "Albert Ghiorso, Torbjørn Sikkeland et al.", "year": 1961,
        "electron_config": "[Rn] 5f14 7s2 7p1", "electronegativity": 1.3, "color": "#C70066"
    },
    104: {
        "name": "Rutherfordium", "symbol": "Rf", "atomic_number": 104, "atomic_weight": 267,
        "category": "transition metal", "group": 4, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": 2100, "boiling_point": 5500,
        "density": 23.2, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 1964,
        "electron_config": "[Rn] 5f14 6d2 7s2", "electronegativity": None, "color": "#CC0059"
    },
    105: {
        "name": "Dubnium", "symbol": "Db", "atomic_number": 105, "atomic_weight": 268,
        "category": "transition metal", "group": 5, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 29.3, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 1967,
        "electron_config": "[Rn] 5f14 6d3 7s2", "electronegativity": None, "color": "#D1004F"
    },
    106: {
        "name": "Seaborgium", "symbol": "Sg", "atomic_number": 106, "atomic_weight": 269,
        "category": "transition metal", "group": 6, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 35.0, "discoverer": "Lawrence Berkeley National Laboratory", "year": 1974,
        "electron_config": "[Rn] 5f14 6d4 7s2", "electronegativity": None, "color": "#D90045"
    },
    107: {
        "name": "Bohrium", "symbol": "Bh", "atomic_number": 107, "atomic_weight": 270,
        "category": "transition metal", "group": 7, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 37.1, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1981,
        "electron_config": "[Rn] 5f14 6d5 7s2", "electronegativity": None, "color": "#E00038"
    },
    108: {
        "name": "Hassium", "symbol": "Hs", "atomic_number": 108, "atomic_weight": 269,
        "category": "transition metal", "group": 8, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 40.7, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1984,
        "electron_config": "[Rn] 5f14 6d6 7s2", "electronegativity": None, "color": "#E6002E"
    },
    109: {
        "name": "Meitnerium", "symbol": "Mt", "atomic_number": 109, "atomic_weight": 278,
        "category": "transition metal (predicted)", "group": 9, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 37.4, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1982,
        "electron_config": "[Rn] 5f14 6d7 7s2", "electronegativity": None, "color": "#EB0026"
    },
    110: {
        "name": "Darmstadtium", "symbol": "Ds", "atomic_number": 110, "atomic_weight": 281,
        "category": "transition metal (predicted)", "group": 10, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 34.8, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1994,
        "electron_config": "[Rn] 5f14 6d9 7s1", "electronegativity": None, "color": "#FF0000"
    },
    111: {
        "name": "Roentgenium", "symbol": "Rg", "atomic_number": 111, "atomic_weight": 282,
        "category": "transition metal (predicted)", "group": 11, "period": 7, "block": "d",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 28.7, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1994,
        "electron_config": "[Rn] 5f14 6d10 7s1", "electronegativity": None, "color": "#FF5B00"
    },
    112: {
        "name": "Copernicium", "symbol": "Cn", "atomic_number": 112, "atomic_weight": 285,
        "category": "transition metal (predicted)", "group": 12, "period": 7, "block": "d",
        "state": "Gas (predicted)", "melting_point": None, "boiling_point": None,
        "density": 23.7, "discoverer": "Gesellschaft für Schwerionenforschung (GSI)", "year": 1996,
        "electron_config": "[Rn] 5f14 6d10 7s2", "electronegativity": None, "color": "#FF8F00"
    },
    113: {
        "name": "Nihonium", "symbol": "Nh", "atomic_number": 113, "atomic_weight": 286,
        "category": "post-transition metal (predicted)", "group": 13, "period": 7, "block": "p",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 16, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 2003,
        "electron_config": "[Rn] 5f14 6d10 7s2 7p1", "electronegativity": None, "color": "#FFB300"
    },
    114: {
        "name": "Flerovium", "symbol": "Fl", "atomic_number": 114, "atomic_weight": 289,
        "category": "post-transition metal (predicted)", "group": 14, "period": 7, "block": "p",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 14, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 1998,
        "electron_config": "[Rn] 5f14 6d10 7s2 7p2", "electronegativity": None, "color": "#FFD300"
    },
    115: {
        "name": "Moscovium", "symbol": "Mc", "atomic_number": 115, "atomic_weight": 290,
        "category": "post-transition metal (predicted)", "group": 15, "period": 7, "block": "p",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 13.5, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 2003,
        "electron_config": "[Rn] 5f14 6d10 7s2 7p3", "electronegativity": None, "color": "#FFE500"
    },
    116: {
        "name": "Livermorium", "symbol": "Lv", "atomic_number": 116, "atomic_weight": 293,
        "category": "post-transition metal (predicted)", "group": 16, "period": 7, "block": "p",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 12.9, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 2000,
        "electron_config": "[Rn] 5f14 6d10 7s2 7p4", "electronegativity": None, "color": "#FFF200"
    },
    
    117: {
        "name": "Tennessine", "symbol": "Ts", "atomic_number": 117, "atomic_weight": 294,
        "category": "halogen (predicted)", "group": 17, "period": 7, "block": "p",
        "state": "Solid (predicted)", "melting_point": None, "boiling_point": None,
        "density": 7.2, "discoverer": "Joint Institute for Nuclear Research (JINR)", "year": 2010,
        "electron_config": "[Rn] 5f14 6d10 7s2 7p5", "electronegativity": None, "color": "#FFFF00"
    },
    118: {"name": "Oganesson", "symbol": "Og", "atomic_number": 118, "atomic_weight": 294,
            "category": "unknown", "group": 18, "period": 7, "block": "p",
            "state": "Unknown", "melting_point": None, "boiling_point": None,
            "density": None, "discoverer": "Joint Institute for Nuclear Research", "year": 2006,
            "electron_config": "[Rn] 5f14 6d10 7s2 7p6", "electronegativity": None, "color": "#E8E8E8"
    }
}

CATEGORY_COLORS = {
    "alkali metal": "#FF6666",
    "alkaline earth metal": "#FFDEAD",
    "transition metal": "#FFC0C0",
    "post-transition metal": "#CCCCCC",
    "metalloid": "#CCCC99",
    "diatomic nonmetal": "#A1FFC3",
    "polyatomic nonmetal": "#E2FFC3",
    "noble gas": "#C0FFFF",
    "halogen": "#FFFF99",
    "lanthanide": "#FFBFFF",
    "actinide": "#FF99CC",
    "unknown": "#E8E8E8",
    "liquid": "#ADD8E6",  # Not a category, but sometimes used
    "solid": "#D3D3D3",   # Not a category, but sometimes used
    "gas": "#FFFACD",     # Not a category, but sometimes used
}

def get_element(atomic_number):
    """Return element data by atomic number."""
    return ELEMENTS.get(atomic_number)

def get_all_elements():
    """Return all elements as a list of dictionaries."""
    return list(ELEMENTS.values())

def get_elements_by_period(period):
    """Return elements in a specific period."""
    return [elem for elem in ELEMENTS.values() if elem["period"] == period]

def get_elements_by_group(group):
    """Return elements in a specific group."""
    return [elem for elem in ELEMENTS.values() if elem["group"] == group]

def get_category_color(category):
    """Return the color associated with an element category."""
    return CATEGORY_COLORS.get(category.lower(), "#FFFFFF")
