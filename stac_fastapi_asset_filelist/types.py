import attr
from stac_fastapi.types.search import APIRequest


@attr.s
class GetAssetFileListRequest(APIRequest):
    """Base arguments for GET  Request."""

    collection_id: str = attr.ib()
    item_id: str = attr.ib()
