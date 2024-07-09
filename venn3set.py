import itertools
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
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

# Генерируем все возможные комбинации (2^8 = 256 комбинаций)
combinations = list(itertools.product([0, 1], repeat=7))

# Идентификаторы областей
region_ids = ('100', '010', '110', '001', '101', '011', '111')

for i, combo in enumerate(combinations):
    plt.figure(figsize=(10, 10))

    # Создаем диаграмму Венна
    v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A', 'B', 'C'))

    # Генерируем уникальный цвет для каждой комбинации
    hue = i / 128
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
            #v.get_patch_by_id('100').set(visible=False, label=None)
          # ('100', '010', '110', '001', '101', '011', '111')
            v.get_label_by_id('100').set_text("")
            v.get_label_by_id('010').set_text("")
            v.get_label_by_id('110').set_text("")
            v.get_label_by_id('001').set_text("")
            v.get_label_by_id('101').set_text("")
            v.get_label_by_id('011').set_text("")
            v.get_label_by_id('111').set_text("")
    # Добавляем заголовок
    plt.title(f'{i+1} = {combo}', fontname='Roboto')

    # Сохраняем диаграмму
    plt.savefig(f'venn_diagrams/venn_diagram_{i+1:03d}.png')
    plt.close()

print("All 128 Venn diagrams have been generated and saved.")
