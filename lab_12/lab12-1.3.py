import polars as pl

# Створення DataFrame
df_polars = pl.DataFrame({
    'employee': ['Anna', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'department': ['IT', 'Sales', 'IT', 'HR', 'Sales'],
    'salary': [75000, 65000, 80000, 70000, 68000],
    'experience': [5, 3, 7, 4, 2]
})

# Ланцюгові операції (method chaining)
result = (
    df_polars
    .filter(pl.col('salary') > 65000)
    .with_columns([
        (pl.col('salary') * 1.1).alias('new_salary'),
        (pl.col('salary') / pl.col('experience')).alias('salary_per_year')
    ])
    .sort('salary_per_year', descending=True)
)

print("Оброблені дані співробітників:")
print(result)

# Групування з множинною агрегацією
dept_stats = df_polars.group_by('department').agg([
    pl.col('salary').mean().alias('avg_salary'),
    pl.col('salary').max().alias('max_salary'),
    pl.len().alias('employees')
])

print("\nСтатистика по відділах:")
print(dept_stats)

# Lazy evaluation для оптимізації складних запитів
lazy_query = (
    df_polars.lazy()
    .filter(pl.col('experience') > 2)
    .select(['employee', 'department', 'salary'])
    .group_by('department')
    .agg(pl.col('salary').mean())
)

# Виконання запиту
result_lazy = lazy_query.collect()
print("\nРезультат lazy запиту:")
print(result_lazy)