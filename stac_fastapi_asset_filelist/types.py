from typing import Dict, Optional, Union

import attr
from stac_fastapi.types.search import APIRequest
from typing_extensions import TypedDict

NumType = Union[float, int]


class Asset(TypedDict, total=False):

    href: str
    role: Optional[str]


@attr.s
class GetAssetFileListRequest(APIRequest):
    """Base arguments for GET  Request."""

    collection_id: str = attr.ib()
    item_id: str = attr.ib()
