from .base import BaseBrawlStarsModel
from .star_power import StarPowerModel
from typing import List
from dataclasses import field


class BrawlerModel(BaseBrawlStarsModel):
    id: int
    name: str
    star_powers: List[StarPowerModel]

    def __post_init__(self):
        super().__post_init__()
        if self.ddata.starPowers:
            self.star_powers = [
                StarPowerModel(data=d) for d in self.ddata.starPowers
            ]
        else:
            self.star_powers = []

