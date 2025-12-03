import pandas as pd     # Бібліотека для роботи з табличними даними (DataFrame)
import numpy as np      # Бібліотека для роботи з числовими масивами
import plotly.graph_objects as go       # Основний модуль Plotly для створення інтерактивних графіків
from scipy.interpolate import griddata  # Функція для інтерполяції даних на регулярну сітку
import sys

ZAKARPATTYA_FILE_NAME="zakarpattya_relief.csv"

#Клас для управління даними та логікою
class ReliefVisualizer:
    def __init__(self):
        # DataFrame для зберігання даних про висоти
        self.df = pd.DataFrame()
        # Конфігурація Plotly для інтерактивності
        self.plotly_config = {
            'displayModeBar': True,
            'responsive': True
        }
        # Змінна для відстеження поточного джерела даних (для назв графіків)
        self.current_data_source = ""
    def load_data(self):
        file_name = ZAKARPATTYA_FILE_NAME
        try:
            # Читання даних з файлу
            self.df = pd.read_csv(file_name)
            self.current_data_source = f"Закарпаття ('{file_name}')"
            print(f"\nДані успішно завантажено з '{file_name}'. Кількість записів: {len(self.df)}")
            self.clean_data()
            return True
        except FileNotFoundError:
            print(f"\nПомилка. Файл '{file_name}' не знайдено")
            return False
    def clean_data(self):
        if self.df.empty:
            return
        # Уніфікація стовпців для коректної роботи. Очікуємо 6 стовпців
        expected_cols =['Name', 'Latitude', 'Longitude', 'Elevation', 'Region', 'Oblast']
        if len(self.df.columns) == len(expected_cols):
            self.df.columns = expected_cols
        elif len(self.df.columns) == 4:      # Обробка випадку, якщо є лише основні 4 стовпці
            self.df.columns =['Name', 'Latitude', 'Longitude', 'Elevation']
            self.df['Region']='N/A'
            self.df['Oblast']='N/A'
        # Перетворення числових стовпців. 'errors=coerce' перетворює нечислові значення на NaN
        for col in ['Latitude', 'Longitude', 'Elevation']:
            self.df[col]=pd.to_numeric(self.df[col], errors='coerce')
        original_len = len(self.df)
        # Видалення рядків, де відсутні координати або висота
        self.df.dropna(subset=['Latitude', 'Longitude', 'Elevation'], inplace=True)
        if len(self.df) <original_len:
            print(f"Очищення. Видалено {original_len - len(self.df)} рядків з некоректними числовими даними.")
        if self.df.empty:
            print(f"Після очищення DataFrame порожній")

    def create_3d_surface(self, df_filtered = None):
        if self.df.empty:
            print("Дані не завантажено. Виконайте опцію 1.")
            return
        # Використовуємо відфільтровані дані, якщо вони є
        df_source = df_filtered if df_filtered is not None else self.df
        if df_source.empty:
            print("Помилка. Фільтр повернув порожній результат")
            return
        print("Створення сітки та інтерполяція для 3D Surface")
        paints = df_source[['Longitude', 'Latitude']].values    # Координати X, Y
        values = df_source['Elevation'].values  # Висоти Z
        # Визначення меж сітки на основі мінімальних/максимальних координат
        x_min, x_max = df_source['Longitude'].min(), df_source['Longitude'].max()
        y_min, y_max = df_source['Latitude'].min(), df_source['Latitude'].max()
        grid_x, grid_y = np.mgrid[x_min:x_max:150j, y_min:y_max:150j]   # Створення регулярної сітки 150x150 точок для інтерполяції
        grid_z  =griddata(paints,values,(grid_x,grid_y),method='cubic') # Інтерполяція висот за допомогою методу 'cubic'
        # Створення 3D Surface Plot за допомогою Plotly
        fig =go.Figure(data=[
            go.Surface(
                z=grid_z,
                y=grid_y,
                x=grid_x,
                colorscale='Inferno_r',
                colorbar_title = 'Висота (м)',
                name = 'Рельєф'
            )
        ])
        # Налаштування макету графіку
        fig.update_layout(
            title =f'3D Поверхня Рельєфу: {self.current_data_source}',
            scene = dict(
                xaxis_title = 'Довгота (Longitude)',
                yaxis_title = 'Широта (Latitude)',
                zaxis_title = 'Висота (Elevation, м)',
                # Встановлення співвідношення сторін
                aspectratio = dict(x=1, y=1, z=0.25),
                camera = dict(
                    up=dict(x=0, y=0, z=1),
                    center=dict(x=0, y=0, z=0),
                    eye=dict(x=1.5, y=1.5, z=0.5)
                )
            ),
            height=800,
        )
        self._display_and_save_plot(fig,"3D Surface Plot")
    def create_3d_scatter(self, df_filtered = None):
        if self.df.empty:
            print("Дані не завантажено. Виконайте опцію 1.")
            return
        df_source = df_filtered if df_filtered is not None else self.df
        if df_source.empty:
            print("Помилка. Фільтр повернув порожній результат.")
            return
        # Створення 3D Scatter Plot
        fig = go.Figure(data=[
            go.Scatter3d(
                x=df_source['Longitude'],
                y=df_source['Latitude'],
                z=df_source['Elevation'],
                mode='markers',  # Відображаємо дані як маркери (точки)
                marker=dict(
                    size=8,
                    color=df_source['Elevation'],  # Колір маркерів залежить від висоти
                    colorscale='Jet',
                    opacity=0.9,
                    colorbar=dict(title='Висота (м)')
                ),
                # Налаштування тексту, який з'являється при наведенні курсору
                text=df_source['Name'] + " (" + df_source['Elevation'].astype(str) + "м, " + df_source[
                    'Region'] + ")",
                name='Вершини'
            )
        ])
        # Налаштування макету графіку
        fig.update_layout(
            title =f'3D Розсіювання Вершин: {self.current_data_source}',
            scene = dict(
                xaxis_title='Довгота (Longitude)',
                yaxis_title='Широта (Latitude)',
                zaxis_title='Висота (Elevation, м)',
                aspectratio=dict(x=1, y=1, z=0.5)
            ),
            height=800,
        )
        self._display_and_save_plot(fig, "3D Scatter Plot")
    #Функції Фільтрації та Обробки
    def filter_by_elevation(self):
        if self.df.empty:
            print("Помилка. Дані не завантажено.")
            return
        print("\nФільтр по висоті")
        try:
            #Отримання мінімальної та максимальної висоти від користувача
            min_el = float(input(f"Введіть мінімальну висоту (поточний мінімум: {self.df['Elevation'].min()} м): "))
            max_el = float(input(f"Введіть максимальну висоту (поточний максимум: {self.df['Elevation'].max()} м): "))
            if min_el >= max_el:
                print(f"Помилка. Некоректне введення: Мінімальна висота має бути меншою за максимальну.")
                return None
            # Логіка фільтрації
            filtered_df = self.df[
                (self.df['Elevation'] >= min_el) &
                (self.df['Elevation'] <= max_el)
            ]
            print(f"Фільтр застосовано. Знайдено {len(filtered_df)} вершин.")
            return filtered_df
        except ValueError:
            print(f"Помилка. Некоректне введення користувача: Введіть числові значення.")
            return None
    def filter_by_region(self):
        if self.df.empty:
            print("Помилка. Дані не завантажено.")
            return
        unique_regions = self.df['Region'].unique()
        print(f"\nФільтр по регіону")
        # Виводимо список доступних регіонів
        print("Доступні регіони:\n" + "\n".join([f"- {r}" for r in unique_regions]))
        region = input("Введіть назву регіону для фільтрації: ").strip()
        # Перевірка наявності регіону
        if region not in unique_regions and region.lower() not in [r.lower() for r in unique_regions]:
            print(f"Помилка. Некоректне введення: Такого регіону не знайдено.")
            return None
        filtered_df= self.df[self.df['Region']==region]        # Фільтруємо з урахуванням регістру
        if filtered_df.empty:
            # Якщо не знайдено
            region_match = [r for r in unique_regions if r.lower() == region.lower()]
            if region_match:
                filtered_df = self.df[self.df['Region'] == region_match[0]]
        if filtered_df.empty:
            print("Помилка. Не знайдено точок для цього регіону.")
            return None
        print(f"Фільтр застосовано. Знайдено {len(filtered_df)} вершин у регіоні '{region}'.")
        return filtered_df
    def get_top_peaks(self):
        if self.df.empty:
            print("Помилка. Дані не завантажено.")
            return
        print("\nТоп-N найвищих вершин")
        try:
            n=int(input(f"Введіть кількість вершин (N) для відображення: "))
            if n <= 0:
                print(f"Помилка. Некоректне введення: N має бути додатнім числом.")
                return
            # Сортування даних за висотою у порядку спадання та вибір N перших
            top_peaks = self.df.sort_values(by=['Elevation'], ascending=False).head(n)
            print(f"\nРезультат] Топ-{n} найвищих вершин (Джерело: {self.current_data_source}):")
            try:
                # Використання to_markdown для відображення красивої таблиці
                print(top_peaks[['Name', 'Elevation', 'Region', 'Oblast']].to_markdown(index=False))
            except ImportError:
                print(top_peaks[['Name', 'Elevation', 'Region', 'Oblast']].to_string(index=False))
        except ValueError:
            print(f"Помилка. Некоректне введення користувача: Введіть ціле число.")

    def _display_and_save_plot(self, fig, plot_type):
        # Формуємо ім'я файлу
        base_name = self.current_data_source.split(" (")[0].replace(" ", "_")
        filename = f"{base_name}_{plot_type.replace(' ', '_')}.html"

        # Збереження HTML-файлу
        fig.write_html(filename, config=self.plotly_config)
        print(f"\nГрафік '{plot_type}' збережено у файл: '{filename}'")

        # Автоматичне відкриття у браузері
        try:
            import webbrowser
            webbrowser.open(filename)
            print(f"Відкрито у браузері: {filename}")
        except Exception as e:
            print(f"Не вдалося автоматично відкрити браузер: {e}")
def main():
    app = ReliefVisualizer()
    df_filtered = None
    while True:
        print("3D Візуалізація Рельєфу: Геопросторові Дані")
        print("1. Завантажити дані: Закарпаття (з файлу zakarpattya_relief.csv)")
        print("2. Показати 3D Surface (поверхня рельєфу)")
        print("3. Показати 3D Scatter (точки вершин)")
        print("4. Фільтрувати по висоті")
        print("5. Фільтрувати по регіону")
        print("6. Топ-N найвищих вершин")
        print("7. Показати останній відфільтрований результат")
        print("9. Вийти")
        # Виведення поточного статусу програми
        if app.df.empty:
            print("Поточний статус: Дані не завантажено.")
        elif df_filtered is not None:
            print(f"Поточний статус: {app.current_data_source}. Застосовано фільтр: {len(df_filtered)} точок.")
        else:
            print(f"Поточний статус: {app.current_data_source}. Завантажено {len(app.df)} точок. Фільтр відсутній.")
        choice = input("Введіть опцію: ").strip().lower()
        if choice == '1':
            app.load_data()
            df_filtered = None
        elif choice == '2':
            app.create_3d_surface(df_filtered)
        elif choice == '3':
            app.create_3d_scatter(df_filtered)
        elif choice == '4':
            df_filtered = app.filter_by_elevation()
        elif choice == '5':
            df_filtered = app.filter_by_region()
        elif choice == '6':
            app.get_top_peaks()
        elif choice == '7':
            # Відображення відфільтрованих даних
            if df_filtered is not None and not df_filtered.empty:
                print("\nОстанній відфільтрований результат")
                try:
                    print(df_filtered.head(10).to_markdown(index=False))
                except ImportError:
                    print(df_filtered.head(10))
                    print(f"Всього {len(df_filtered)} точок.")
            else:
                print("Помилка. Фільтр не застосовано або він порожній.")
        elif choice == '9':
            print("Програму завершено.")
            sys.exit(0)
        else:
            print("Помилка. Некоректне введення. Введіть опцію (1, 2, 3, 4, 5, 6, 7, 9).")
if __name__ == '__main__':
    main()