from dataclasses import dataclass, asdict


@dataclass
class AuthorizePayload:
    name: str = 'default'

    def to_dict(self):
        return asdict(self)
