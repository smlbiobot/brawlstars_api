from dataclasses import dataclass

from ..mixins.tag import TagMixin
from ..utils import AttrDict


@dataclass
class BaseModel:
    data: dict = None


class BaseBrawlStarsModel(BaseModel, TagMixin):
    _ddata = None

    @property
    def ddata(self):
        if self._ddata is None:
            self._ddata = AttrDict(self.data)
        return self._ddata
