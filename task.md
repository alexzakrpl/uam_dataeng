## Ćwiczenie

### Etap I - refaktoring

*zadanie będzie traktowane tak samo jak aktywność*

Zrób refactoring poniższego kodu:

```python
import pandas as pd

def extract(path):
  return pd.read_csv(path)

def transform(df):
  return df[["Imię"]].drop_duplicates()

def load(df, path):
  return df.to_json(path, orient="records", index=False, lines=True)


def job(input_path, output_path):
  source_data = extract(input_path)
  transformed_data = transform(source_data)
  load(transformed_data, output_path)
```

1. Utwórz klasę `CsvExtractor` z metodą `extract`. Parametry metody `extract`: `path`.
2. Utwórz klasę `Deduplicator` z metodą `transform`. Konstruktor klasy przyjmuje listę pól na bazie, których odbywa się deduplikacja. `transform` nie posiada parametrów.
3. Utwórz klasę `JsonLoader` z metodą `load`. Konstruktor przyjmuje parametry: `orient`, `index`, `lines`. Metoda `load` przyjmuje `path`.
4. Utwórz klasę `Job`. Parametry konstruktora: `input_path`, `output_path` oraz obiekty typu: `CsvExtractor`, `Deduplicator`, `JsonLoader`. Metoda `run` nie posiada parametrów, ale odpowiada za uruchomienie job'a.
5. Utwórz plik `main.py`, który tworzy instancję `Job` i uruchamia metodę `run`.

Dobrze korzystać z modułów i pakietów.

Rozwiązanie najlepiej umieścić na Github albo w ramach usługi uczelnianej.

Linki do rozwiązań proszę wysłać mi na priv na MS Teams. Najlepiej jak będą to Pull Request'y z feature branch'a do branch'a main/master - ułatwi to ew. komentowanie.

*pozostała część dla chętnych*

### Etap II - zmiana wymagań 1
1. Dodaj klasę `ParquetLoader`, która zapisuje dane w formacie parquet.
2. Utwórz plik `main_parquet.py`, który tworzy instancję `Job` i uruchamia metodę `run`.

Jak pracuje się Tobie z modularnym kodem?

### Etap III - zmiana wymagań 2
Tym razem potrzebny nam jest nowe przetwarzanie, które zlicza pracowników w poszczególnych departamentach. Postaram się wykorzystać klasy `CsvExtractor`, `ParquetLoader`, `Job`. Utwórz plik  `main_departments.py`.

Jak pracuje się Tobie z modularnym kodem?

### Etap IV

Spróbuj skorzystać z `typing`: https://realpython.com/python-type-checking/

### Etap V
W zasobach dot. tych zajęć znajdują się filmy dot. klas abstrakcyjnych, protokołów i `dependency inversion`. Zaproponuj hierarchę klas / protokoły (w zależności co wybierzesz), które najlepiej pasowałyby do naszego przypadku.

### Etap VI
Za pomocą jednego z frameworków do testów:
1. https://docs.pytest.org/en/stable/
2. https://docs.python.org/3/library/unittest.html

Stwórz klasę testową, która zawsze zwraca te wiersze nie odczytując ich z pliku. Wiersze do zwrócenia są argumentami konstruktora. Parametr `path` metody `extract` nie ma wpływu na zwrócony wynik. Utwórz przypadek testowy, który obejmuje:
1. Utworzenie instancji nowej klasy
2. Utworzenie instancji klasy `Job` bazując na nowej klasie
3. Sprawdzeniu, czy dla danych testowych zwracane są dane zgodnie z oczekiwanymi

Zakaz korzystania z mock'ów.
