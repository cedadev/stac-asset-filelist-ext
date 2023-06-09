"""Base clients."""
import abc
from typing import List, Union

import attr

from .types import Asset

NumType = Union[float, int]


@attr.s  # type:ignore
class BaseAssetFileListClient(abc.ABC):
    """Defines a pattern for implementing STAC asset file list endpoint."""

    @abc.abstractmethod
    def get_asset_filelist(
        self,
        collection_id: str,
        item_id: str,
        **kwargs,
    ) -> List[Asset]:
        """item asset file list (GET).

        Called with `GET /collection/{collection_id}/items/{item_id}/asset_filelist.json`.

        Returns:
            List containing assets for given item.
        """
        ...
