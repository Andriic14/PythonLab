from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

DATA_FILE = "API_NY.GDP.csv"
COUNTRIES_FOR_LINE_CHART = ["Ukraine","Italy"]
indicator_name = "ВВП на душу населення"
def load_gdp_data_all(file_path):
    final_data = defaultdict(dict)
    all_countries_found = set()
    if not os.path.exists(file_path):
        print(f"Помилка: Файл даних '{file_path}' не знайдено")
        return final_data, all_countries_found
    SKIP_ROWS = 5
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
        if len(rows) <= SKIP_ROWS:
            print("Помилка: Файл CSV занадто короткий")
            return final_data, all_countries_found
        header = rows[SKIP_ROWS - 1]
        years = [int(year) for year in header[4:] if year.strip().isdigit()]
        for row in rows[SKIP_ROWS:]:
            country_name = row[0].strip()
            if not country_name:
                continue  # Пропускаємо порожні назви країн
            has_valid_data = False
            for i, year in enumerate(years):
                val_str = row[4 + i].strip()
                try:
                    value = float(val_str) if val_str else np.nan
                except ValueError:
                    value = np.nan

                if not np.isnan(value):
                    final_data[year][country_name] = value
                    has_valid_data = True
            if has_valid_data:
                all_countries_found.add(country_name)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return defaultdict(dict), set()
    return final_data, all_countries_found

def process_data_for_plotting(gdp_data, countries):
    if not gdp_data:
        return {'Year':[]}
    years = sorted([year for year, data in gdp_data.items() if any(c in data for c in countries)])#Фільтруємо роки, для яких є дані хоча б для однієї з країн
    plot_data = {'Year':years}
    for country in countries:
        plot_data[country] = [gdp_data.get(year,{}).get(country,np.nan) for year in years]
    return plot_data
def plot_line_chart(plot_data, indicator_name):
    countries_to_plot = [key for key in plot_data if key != 'Year']
    plt.figure(figsize=(14, 7))
    # Побудова графіків для кожної країни
    for country in countries_to_plot:
        # Видаляємо NaN значення для коректного відображення
        valid_years = [plot_data['Year'][i] for i, val in enumerate(plot_data[country]) if not np.isnan(val)]
        valid_values = [val for val in plot_data[country] if not np.isnan(val)]
        plt.plot(valid_years, valid_values,
                label=country,
                marker='o',
                linestyle='-',
                linewidth=2,
                alpha=0.8)
    # Налаштування осей та заголовка
    plt.title(f"Динаміка показника: {indicator_name}", fontsize=18, pad=15)
    plt.xlabel('Рік',fontsize=12,color='darkblue')
    plt.ylabel('Значення показника (USD)',fontsize=12,color='darkblue')
    # Додавання легенди та сітки
    plt.legend(title = 'Країна', loc='upper left')
    plt.grid(True,linestyle='--',alpha=0.5)
    if plot_data['Year']:   # Форматування осі X: відображати лише цілі роки
        step = max(1, len(plot_data['Year']) // 15)
        plt.xticks(plot_data['Year'][::step], rotation=45)
    plt.tight_layout()
    plt.show()
def plot_bar_chart(gdp_data, country_name,indicator_name):
    if country_name not in gdp_data or not gdp_data.get('Year'):
        return
    years = gdp_data['Year']
    values = gdp_data[country_name]
    valid_data = [(years[i],values[i],)for i in range (len(years)) if not np.isnan (values[i])]
    bar_years = [item[0] for item in valid_data]
    bar_values = [item[1]for item in valid_data]
    plt.figure(figsize = (12,6))
    # Побудова діаграми
    bars = plt.bar(bar_years, bar_values,color = 'green',alpha = 0.7, width = 0.8)
    #Налаштування заголовка та осей
    plt.title(f"Значення показника для {country_name}: {indicator_name}", fontsize=18, pad=15)
    plt.xlabel('Рік', fontsize=12, color='darkblue')
    plt.ylabel('Значення показника (USD)', fontsize=12, color='darkblue')
    #Додавання значень над стовпцями
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height+ height*0.01,
                 f'{height / 1000 :.1f}K',
                 ha='center', va='bottom',
                 fontsize=9, rotation=45)
    # Налаштування міток по осі X
    plt.xticks(bar_years, rotation=45)
    plt.grid(axis='y',linestyle='--',alpha=0.5)
    plt.tight_layout()
    plt.show()
def main():
    #Завантаження та обробка даних
    gdp_data_all, available_countries_all = load_gdp_data_all(DATA_FILE)
    if not gdp_data_all:
        print("Не вдалося завантажити дані. Завершення програми.")
        return
    # дані для Ukraine та Italy для лінійного графіка
    countries_for_line_chart_present = [c for c in COUNTRIES_FOR_LINE_CHART if c in available_countries_all]
    plot_data_specific = process_data_for_plotting(gdp_data_all, countries_for_line_chart_present)
    if len(countries_for_line_chart_present)>=2: #Перевірка наявності даних для лінійного графіка
        print(f"Будується лінійний графік для {', '.join(countries_for_line_chart_present)}")
        plot_line_chart(plot_data_specific, indicator_name)
    else:
        print(f"Немає даних для всіх необхідних країн ({', '.join(COUNTRIES_FOR_LINE_CHART)}) для лінійного графіка.")
    while True:
        count = len(available_countries_all)# available_countries_all містить УСІ країни з файлу
        choice = input(f"\nВведіть назву країни для побудови стовпчастої діаграми (доступно {count} країн, наприклад, 'Ukraine' або 'Albania'): ").strip()
        if choice in available_countries_all:
            print(f"Будується стовпчаста діаграма для {choice}")
            # Готуємо дані для обраної користувачем країни
            plot_data_single = process_data_for_plotting(gdp_data_all, [choice])
            plot_bar_chart(plot_data_single,choice,indicator_name)
            break
        elif choice.lower() == 'вихід' or choice.lower() == 'exit':
            print("Вихід з програми.")
            break
        else:
            print(f"Помилка: Країна '{choice}' не знайдена у файлі або для неї немає даних. Спробуйте ще раз або введіть 'вихід'")
main()