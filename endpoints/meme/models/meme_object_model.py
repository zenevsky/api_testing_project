from dataclasses import dataclass, asdict, field
from typing import List, Dict

from endpoints.meme.models.meme_enumerators import Tags


@dataclass
class CreateMemePayload:
    tags: List[Tags] = field(default_factory=lambda: [Tags.lol])
    text: str = 'default'
    url: str = 'https://ya.ru/'
    info: Dict = field(default_factory=dict)

    def to_dict(self):
        data = asdict(self)

        if isinstance(self.tags, list):
            data['tags'] = [tag.value if isinstance(tag, Tags) else tag for tag in self.tags]
        return data

@dataclass
class UpdateMemePayload:
    id: int = 999
    tags: List[Tags] = field(default_factory=lambda: [Tags.lol])
    text: str = 'default'
    url: str = 'https://ya.ru/'
    info: Dict = field(default_factory=dict)

    def to_dict(self):
        data = asdict(self)

        if isinstance(self.tags, list):
            data['tags'] = [tag.value if isinstance(tag, Tags) else tag for tag in self.tags]
        return data
