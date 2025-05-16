import xml.etree.ElementTree as ET
import re

# Lecture avec conservation des namespaces
tree = ET.parse('index.html')
root = tree.getroot()

# Enregistrer les namespaces à l'avance pour éviter ns0, ns1, etc.
ET.register_namespace('', 'http://www.w3.org/2000/svg')  # Namespace principal
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')  # Ajoute tous ceux que tu repères dans le fichier

# Regex pour détecter les id DepXX
pattern = re.compile(r'^Dep.._.*')

# Modifier les éléments avec id DepXX
for elem in root.iter():
    elem_id = elem.get('id')
    if elem_id and pattern.match(elem_id):
        style = elem.get('style')
        if style:
            new_style = re.sub(r'fill:[^;]+', 'fill:#fff', style)
            elem.set('style', new_style)
        else:
            elem.set('style', 'fill:#fff')

# Sauvegarde sans ns0/ns1
tree.write('index2.html', encoding='utf-8', xml_declaration=True)
