import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    # Читаем содержимое файла, переводим в нижний регистр
                    content = f.read().lower()
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation))
                    # Разбиваем по пробелам
                    words = content.split()
                    all_words[file_name] = words
            except Exception as e:
                print(f"Ошибка при чтении файла {file_name}: {e}")
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()  # Игнорируем регистр
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1  # +1 для позиции от 1
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        word = word.lower()  # Игнорируем регистр
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results

# Пример использования:
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Печатает все слова
    print(finder.find('TEXT'))      # Печатает позицию слова 'TEXT'
    print(finder.count('teXT'))     # Печатает количество слова 'teXT'