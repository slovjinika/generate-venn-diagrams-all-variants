# Уменьшаем размер изображений до 360p
for file in venn_diagrams/*.png; do
    magick convert "$file" -resize 500x500 "$file"
done

# Создаем GIF-анимацию
convert venn_diagrams/*.png -delay 100 -loop 0 01.gif 
