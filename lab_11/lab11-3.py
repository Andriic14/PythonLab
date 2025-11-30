from itertools import count

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
import string
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
print("="*60)
print("Аналіз тексту Alice's Adventures in Wonderland")
print("="*60)
alise_text = gutenberg.raw('carroll-alice.txt')     # Отримання тексту з Project Gutenberg
print(f"\n Загальна кількість символів у тексті: {len(alise_text)}")

tokens = word_tokenize(alise_text)  # Токенізація тексту (розбиття на слова)
print(f"Загальна кількість токенів: {len(tokens)}")
words = [word.lower() for word in tokens if word.isalpha()]     # Визначення кількості слів (без пунктуації)
print(f"Кількість слів у тексті: {len(words)}")

print("10 найбільш вживаних слів")
word_frequencies = Counter(words)
top_10_words = word_frequencies.most_common(10)
for i, (word,count) in enumerate(top_10_words,1):
    print(f"{i}.) {word} - {count} разів")
# Побудова діаграми для слів зі стоп-словами
word_list = [word for word, count in top_10_words]
count_list = [count for word, count in top_10_words]
plt.figure(figsize=(10,5))
plt.bar(word_list,count_list,color='blue',edgecolor='navy')
plt.xlabel('Слова',fontsize=10)
plt.ylabel("Частота вживання",fontsize=10)
plt.title('10 найбільш вживаних слів',fontsize=10,fontweight='bold')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.grid(True)
plt.show()
print("Обробка тексту, видалення стоп-слів та пунктуації")
stop_words = set(stopwords.words('english'))        # Отримання списку англійських стоп-слів
print(f"\nКількість стоп-слів у базі: {len(stop_words)}")
# Фільтрація слів видалення стоп-слів та пунктуації
filtered_words = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words ]
print(f"Кількість слів після видалення стоп-слів: {len(filtered_words)}")
print(f"Видалено слів: {len(words)-len(filtered_words)}")
print("10 найбільш вживаних слів без стоп-слів:")
filtered_words_frequencies = Counter(filtered_words)
top_10_filtered = filtered_words_frequencies.most_common(10)
for i,(word,count) in enumerate(top_10_filtered,1):
    print(f"{i} {word} - {count} разів")
# Побудова діаграми для слів без стоп-слів
filtered_words_list = [word for word, count in top_10_filtered]
filtered_count_list = [count for word, count in top_10_filtered]
plt.figure(figsize=(10,5))
plt.bar(filtered_words_list,filtered_count_list,color='red',edgecolor='navy')
plt.xlabel('Слова',fontsize=10)
plt.ylabel("Частота вживання",fontsize=10)
plt.title('10 найбільш вживаних слів(без стоп-слів)',fontsize=10,fontweight='bold')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.grid(axis='y',alpha = 0.3)
plt.show()
print("Порівняльна статистика")
print(f"Загальна кількість слів:{len(words)}")
print(f"Унікальних слів (з стоп-словами): {len(word_frequencies)}")
print(f"Унікальних слів (без стоп-слів): {len(filtered_words_frequencies)}")
print(f"Відсоток стоп-слів: {(len(words)-len(filtered_words))/len(words)*100:.2f}%")