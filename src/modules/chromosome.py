class Chromosome:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def get_number(self) -> int:
        return int(self.value, 2)
