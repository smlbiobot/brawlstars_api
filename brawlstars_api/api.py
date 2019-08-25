import aiohttp

from .mixins.tag import TagMixin
from .models.player import PlayerModel


class BrawlStarsAPIError(Exception):
    pass


class BaseAPI(object):
    pass


class BrawlStarsAPI(BaseAPI, TagMixin):
    def __init__(self, token=None):
        self._token = token
        self._test = "Hi there"
        self._session = None
        self._headers = None

    async def setup(self):
        """Run this before other tasks"""
        self._session = aiohttp.ClientSession()

    async def shutdown(self):
        if self._session is not None:
            await self._session.close()

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def test(self):
        return self._test

    @property
    def headers(self):
        if self._headers is None:
            self._headers = dict(
                Authorization=f"Bearer {self.token}"
            )
        return self._headers

    def make_url(self, path):
        base = "https://api.brawlstars.com"
        return f"{base}{path}"

    async def fetch(self, url):
        async with self._session.get(url, headers=self.headers) as resp:
            try:
                r = await resp.json()
            except:
                return None
            else:
                return r

    async def get_player(self, player_tag) -> PlayerModel:
        player_tag = self.clean_tag(player_tag)
        path = f"/v1/players/%23{player_tag}"
        url = self.make_url(path)
        r = await self.fetch(url)
        return PlayerModel(r)
