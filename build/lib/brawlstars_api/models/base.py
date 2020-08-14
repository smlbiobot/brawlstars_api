from dataclasses import dataclass

from ..mixins.tag import TagMixin
from ..utils import AttrDict


@dataclass
class BaseModel:
    data: dict = None

    _ddata: AttrDict = None

    def __post_init__(self):
        self._ddata = AttrDict(self.data)

    @property
    def ddata(self):
        return self._ddata


class BaseBrawlStarsModel(BaseModel, TagMixin):
    pass
