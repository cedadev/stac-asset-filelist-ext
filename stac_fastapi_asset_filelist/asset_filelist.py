# encoding: utf-8
"""Asset Search Extension"""

__author__ = "Rhys Evans"
__date__ = "08 Jun 2023"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "rhys.r.evans@stfc.ac.uk"

from typing import List, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.extension import ApiExtension
from starlette.responses import JSONResponse, Response

from .client import BaseAssetFileListClient
from .types import Asset, GetAssetFileListRequest

CONFORMANCE_CLASSES = ["https://api.stacspec.org/v1.0.0-beta.2/asset-search"]


@attr.s
class AssetFileListExtension(ApiExtension):
    """Asset file list extension


    The asset file list extension adds the `/collection/{collection_id}/items/{item_id}/assets` endpoint.

    https://github.com/cedadev/stac-asset-filelist

    Attributes:
        conformance_classes (list): Defines the list of conformance classes
                                    for the extension.
    """

    client: BaseAssetFileListClient = attr.ib(default=None)
    settings: ApiSettings = attr.ib(default=None)
    conformance_classes: List[str] = attr.ib(default=CONFORMANCE_CLASSES)
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)
    asset_filelist_request_model: Type[GetAssetFileListRequest] = attr.ib(
        default=GetAssetFileListRequest
    )

    def register_get_asset_filelist(self):
        """Register asset search endpoint (GET /collection/{collection_id}/items/{item_id}/asset_filelist.json).
        Returns:
            None
        """
        self.router.add_api_route(
            name="Get Assets",
            path="/collections/{collection_id}/items/{item_id}/asset_filelist.json",
            response_model=List[Asset]
            if self.settings and self.settings.enable_response_models
            else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_asset_filelist,
                self.asset_filelist_request_model,
                self.response_class,
            ),
        )

    def register(self, app: FastAPI) -> None:
        self.register_get_asset_filelist()
        app.include_router(self.router, tags=["Asset Search Extension"])
