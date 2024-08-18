r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Intelligence
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class OperatorTypeInstance(InstanceResource):

    class Availability(object):
        INTERNAL = "internal"
        BETA = "beta"
        PUBLIC = "public"
        RETIRED = "retired"

    class OutputType(object):
        TEXT_CLASSIFICATION = "text-classification"
        TEXT_EXTRACTION = "text-extraction"
        TEXT_EXTRACTION_NORMALIZED = "text-extraction-normalized"
        TEXT_GENERATION = "text-generation"

    class Provider(object):
        TWILIO = "twilio"
        AMAZON = "amazon"
        OPENAI = "openai"

    """
    :ivar name: A unique name that references an Operator's Operator Type.
    :ivar sid: A 34 character string that uniquely identifies this Operator Type.
    :ivar friendly_name: A human-readable name of this resource, up to 64 characters.
    :ivar description: A human-readable description of this resource, longer than the friendly name.
    :ivar docs_link: Additional documentation for the Operator Type.
    :ivar output_type: 
    :ivar supported_languages: List of languages this Operator Type supports.
    :ivar provider: 
    :ivar availability: 
    :ivar configurable: Operators can be created from configurable Operator Types.
    :ivar config_schema: JSON Schema for configuring an Operator with this Operator Type. Following https://json-schema.org/
    :ivar date_created: The date that this Operator Type was created, given in ISO 8601 format.
    :ivar date_updated: The date that this Operator Type was updated, given in ISO 8601 format.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.name: Optional[str] = payload.get("name")
        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.docs_link: Optional[str] = payload.get("docs_link")
        self.output_type: Optional["OperatorTypeInstance.OutputType"] = payload.get(
            "output_type"
        )
        self.supported_languages: Optional[List[str]] = payload.get(
            "supported_languages"
        )
        self.provider: Optional["OperatorTypeInstance.Provider"] = payload.get(
            "provider"
        )
        self.availability: Optional["OperatorTypeInstance.Availability"] = payload.get(
            "availability"
        )
        self.configurable: Optional[bool] = payload.get("configurable")
        self.config_schema: Optional[Dict[str, object]] = payload.get("config_schema")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[OperatorTypeContext] = None

    @property
    def _proxy(self) -> "OperatorTypeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OperatorTypeContext for this OperatorTypeInstance
        """
        if self._context is None:
            self._context = OperatorTypeContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "OperatorTypeInstance":
        """
        Fetch the OperatorTypeInstance


        :returns: The fetched OperatorTypeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "OperatorTypeInstance":
        """
        Asynchronous coroutine to fetch the OperatorTypeInstance


        :returns: The fetched OperatorTypeInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.OperatorTypeInstance {}>".format(context)


class OperatorTypeContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the OperatorTypeContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Operator Type.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/OperatorTypes/{sid}".format(**self._solution)

    def fetch(self) -> OperatorTypeInstance:
        """
        Fetch the OperatorTypeInstance


        :returns: The fetched OperatorTypeInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return OperatorTypeInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> OperatorTypeInstance:
        """
        Asynchronous coroutine to fetch the OperatorTypeInstance


        :returns: The fetched OperatorTypeInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return OperatorTypeInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.OperatorTypeContext {}>".format(context)


class OperatorTypePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> OperatorTypeInstance:
        """
        Build an instance of OperatorTypeInstance

        :param payload: Payload response from the API
        """
        return OperatorTypeInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.OperatorTypePage>"


class OperatorTypeList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the OperatorTypeList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/OperatorTypes"

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[OperatorTypeInstance]:
        """
        Streams OperatorTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[OperatorTypeInstance]:
        """
        Asynchronously streams OperatorTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OperatorTypeInstance]:
        """
        Lists OperatorTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OperatorTypeInstance]:
        """
        Asynchronously lists OperatorTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OperatorTypePage:
        """
        Retrieve a single page of OperatorTypeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OperatorTypeInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return OperatorTypePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OperatorTypePage:
        """
        Asynchronously retrieve a single page of OperatorTypeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OperatorTypeInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return OperatorTypePage(self._version, response)

    def get_page(self, target_url: str) -> OperatorTypePage:
        """
        Retrieve a specific page of OperatorTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OperatorTypeInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return OperatorTypePage(self._version, response)

    async def get_page_async(self, target_url: str) -> OperatorTypePage:
        """
        Asynchronously retrieve a specific page of OperatorTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OperatorTypeInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return OperatorTypePage(self._version, response)

    def get(self, sid: str) -> OperatorTypeContext:
        """
        Constructs a OperatorTypeContext

        :param sid: A 34 character string that uniquely identifies this Operator Type.
        """
        return OperatorTypeContext(self._version, sid=sid)

    def __call__(self, sid: str) -> OperatorTypeContext:
        """
        Constructs a OperatorTypeContext

        :param sid: A 34 character string that uniquely identifies this Operator Type.
        """
        return OperatorTypeContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.OperatorTypeList>"
