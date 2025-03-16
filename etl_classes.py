class CsvExtractor():
    def extract(extract, path):
        pass


class Deduplicator():
    def transform(data: list[list]) -> list[list]:
        pass


class JsonLoader():
    def __init__(self, orient, index, lines):
        pass

    def load(path):
        pass


class Job():
    def __init__(
        self,
        input_path: str,
        output_path: str,
        extractor: CsvExtractor,
        dedubl: Deduplicator,
        json_loader: JsonLoader
        ):
        def run(self):
            pass
