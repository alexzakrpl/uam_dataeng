import csv
import pandas as pd
from pandas import DataFrame

class CsvExtractor():
    def __init__(self, path):
        self.path = path
    def extract(self) -> list[list]:
        with open(file=self.path, mode='r') as f:
            file_data = csv.reader(f, delimiter=',')
            data_table = []
            for row in file_data:
                data_table.append(row)
        return data_table


class Deduplicator():
    def __init__(self, data_table):
        self.data_table = data_table
    def transform(self) -> list[list]:
        add_data = self.data_table[1::]
        return self.data_table + add_data


class JsonLoader():
    def __init__(self,
                 orient: str,
                 index: bool,
                 lines: bool):
        self.orient = orient
        self.index = index
        self.lines = lines
    def load(self, df: DataFrame, path: str) -> None:
        df.to_json(
            path, 
            orient=self.orient,
            index=self.index,
            lines=self.lines
            )


class Job():
    def __init__(self,
                 input_path: str,
                 output_path: str,
                 json_loader: JsonLoader) -> None:
        self.file_path = input_path
        self.output_path = output_path
        self.json_loader = json_loader

    def run(self):
        csv_data = CsvExtractor(path=self.file_path)
        data_table = csv_data.extract()
        transformer = Deduplicator(data_table=data_table)
        transformed_data = transformer.transform()
        df = pd.DataFrame(
            data=transformed_data[1::],
            columns=transformed_data[0]
        )
        self.json_loader.load(df=df, path=self.output_path)
        
    
