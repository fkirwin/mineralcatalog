import os
import json
MINERAL_DATA_SOURCE = "/assets/data/minerals.json"

cnt = {'name': 'Zunyite', 'image filename': '240px-Zunyite-199876.jpg', 'image caption': 'Sharp, pyramids of brown-red zunyite from Silver City, Tintic District, East Tintic Mountains, Juab County, Utah, USA (size: 5.5 x 5 x 3.5 cm)', 'category': 'Sorosilicates', 'formula': 'Al<sub>13</sub>Si<sub>5</sub>O<sub>20</sub>(OH,F)<sub>18</sub>Cl', 'strunz classification': '09.BJ.55', 'crystal system': 'Isometric - Hextetrahedral', 'unit cell': 'a = 13.8654 - 13.8882 Å; Z\xa0=\xa04', 'color': 'Grayish white, flesh-red; colorless in thin section', 'crystal symmetry': 'Isometric, 4 3m', 'cleavage': 'Good on {111}', 'mohs scale hardness': '7', 'luster': 'Vitreous', 'streak': 'White', 'diaphaneity': 'Transparent to translucent with inclusions', 'optical properties': 'Isotropic', 'refractive index': 'n = 1.592 - 1.600', 'crystal habit': 'Crystalline - occurs as well-formed fine sized crystals', 'specific gravity': '2.874(5) (meas.) 2.87 - 2.90 (calc.)', 'group': 'Silicates'}

from minerals.models import Mineral


Mineral.save(**cnt)