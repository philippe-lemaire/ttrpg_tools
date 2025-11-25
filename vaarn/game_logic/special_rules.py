from dataclasses import dataclass


@dataclass
class SpecialRule:
    name: str
    description: str

    def __repr__(self):
        return f"<b>{self.name} –</b> {self.description}"
