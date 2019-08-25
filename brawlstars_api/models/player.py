from .base import BaseBrawlStarsModel


class PlayerModel(BaseBrawlStarsModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prop(self, prop):
        return self.data.get(prop)

    @property
    def tag(self):
        return self.clean_tag(self.ddata.tag)

    @property
    def name(self):
        return self.get_prop('name')

    @property
    def trophies(self):
        return self.get_prop('trophies')

    @property
    def highest_trophies(self):
        return self.get_prop('highestTrophies')

    @property
    def exp_level(self):
        return self.get_prop('expLevel')

    @property
    def exp_points(self):
        return self.get_prop('expPoints')

    @property
    def victories_3v3(self):
        return self.get_prop('3vs3Victories')

    @property
    def victories_solo(self):
        return self.get_prop('soloVictories')

    @property
    def victories_duo(self):
        return self.get_prop('duoVictories')

