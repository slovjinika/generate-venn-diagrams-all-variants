import itertools
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import os
import colorsys
from matplotlib import font_manager

# Добавляем шрифт Roboto
font_path = "RobotoMono-Regular.ttf"  # Замените на актуальный путь к файлу Roboto.ttf
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Roboto'

# Создаем директорию для сохранения диаграмм
if not os.path.exists('venn_diagrams'):
    os.makedirs('venn_diagrams')

# Генерируем все возможные комбинации (2^4 = 16 комбинаций)
combinations = list(itertools.product([0, 1], repeat=3))

# Идентификаторы областей
region_ids = ('10', '01', '11')

for i, combo in enumerate(combinations):
    plt.figure(figsize=(10, 10))

    # Создаем диаграмму Венна
    v = venn2(subsets=(1, 1, 1), set_labels=('A', 'B'))

    # Генерируем уникальный цвет для каждой комбинации8
    hue = i / 8
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color = (r, g, b)

    # Устанавливаем цвета для каждой области и добавляем серую обводку
    for j, region_id in enumerate(region_ids):
        if v.get_patch_by_id(region_id):
            if combo[j]:
                v.get_patch_by_id(region_id).set_color(color)
            else:
                v.get_patch_by_id(region_id).set_color('white')
            v.get_patch_by_id(region_id).set_edgecolor('gray')
            v.get_patch_by_id(region_id).set_linewidth(1)
            v.get_label_by_id('10').set_text("")
            v.get_label_by_id('01').set_text("")
            v.get_label_by_id('11').set_text("")

    # Добавляем заголовок
    plt.title(f'{i+1} = {combo}', fontname='Roboto')

    # Сохраняем диаграмму
    plt.savefig(f'venn_diagrams/venn_diagram_{i+1:03d}.png')
    plt.close()

print("All 16 Venn diagrams have been generated and saved.")
