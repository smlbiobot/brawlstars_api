from .base import BaseBrawlStarsModel


class PlayerModel(BaseBrawlStarsModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def tag(self):
        return self.clean_tag(self.ddata.tag)

    @property
    def name(self):
        return self.ddata.name
