import matplotlib.pyplot as plt
import numpy as np
import os
import json
DATA_FILE = 'workshop_data.json'
def load_production_data(file_path):
    if not os.path.exists(file_path):
        print(f"Помилка файл даних '{file_path}' не знайдено")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Помилка некоректний формат JSON у файлі '{file_path}'")
        return None
    weekly_total = {}
    part_types = data.get("Part_Prices", {}).keys()
    for day_empty in data.get("Weekly_Production",[]):
        for part_type in part_types:
            count = day_empty.get(part_type, 0)
            weekly_total[part_type] = weekly_total.get(part_type, 0) + count
    return {k: v for k, v in weekly_total.items() if v>0}
def auto_format_labels(pct, all_values):
    absolute = int(np.round(pct/100.0*np.sum(all_values)))
    return f"{pct:.1f}%\n({absolute} шт)"
def plot_production_pie(weekly_data):
    if not weekly_data:
        print("Недостатньо даних для побудови діаграми")
        return
    sizes = list(weekly_data.values())# Значення (дані для секторів)
    labels = list(weekly_data.keys())# Підписи
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect='equal')) # aspect="equal" гарантує, що діаграма буде круглою
    wedges, text,autotext = ax.pie(
        sizes,
        autopct = lambda pct: auto_format_labels(pct, sizes),
        labels = labels, # Використовуємо назви деталей як підписи біля секторів
        startangle = 90, # Починаємо перший сектор зверху
        wedgeprops={"edgecolor": "black", "linewidth": 1,"antialiased": True} #додає простір між секторами
    )
    ax.legend(wedges, labels, title="Типи деталей", loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotext, size=12, weight="bold", color="white")# Налаштування формату тексту всередині секторів
    ax.set_title("Структура загального тижневого виробництва цеху",fontsize=16,pad=20)# Додавання заголовку діаграми
    plt.show()
def main():
    production_data = load_production_data(DATA_FILE)
    if production_data:
        plot_production_pie(production_data)
    else:
        print("Неможливо продовжити через помилки")
main()