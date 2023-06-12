"""Base clients."""
import abc

import attr


@attr.s  # type:ignore
class BaseAssetFileListClient(abc.ABC):
    """Defines a pattern for implementing STAC asset file list endpoint."""

    @abc.abstractmethod
    def get_asset_filelist(
        self,
        collection_id: str,
        item_id: str,
        **kwargs,
    ) -> dict:
        """item asset file list (GET).

        Called with `GET /collection/{collection_id}/items/{item_id}/asset_filelist.json`.

        Returns:
            List containing assets for given item.
        """
        ...
