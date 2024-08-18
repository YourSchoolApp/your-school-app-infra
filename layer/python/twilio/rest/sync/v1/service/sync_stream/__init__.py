r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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
from twilio.rest.sync.v1.service.sync_stream.stream_message import StreamMessageList


class SyncStreamInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the Sync Stream resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync Stream resource.
    :ivar service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with.
    :ivar url: The absolute URL of the Message Stream resource.
    :ivar links: The URLs of the Stream's nested resources.
    :ivar date_expires: The date and time in GMT when the Message Stream expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the Message Stream does not expire, this value is `null`. The Stream might not be deleted immediately after it expires.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar created_by: The identity of the Stream's creator. If the Stream is created from the client SDK, the value matches the Access Token's `identity` field. If the Stream was created from the REST API, the value is 'system'.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.date_expires: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_expires")
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.created_by: Optional[str] = payload.get("created_by")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[SyncStreamContext] = None

    @property
    def _proxy(self) -> "SyncStreamContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncStreamContext for this SyncStreamInstance
        """
        if self._context is None:
            self._context = SyncStreamContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SyncStreamInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncStreamInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SyncStreamInstance":
        """
        Fetch the SyncStreamInstance


        :returns: The fetched SyncStreamInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncStreamInstance":
        """
        Asynchronous coroutine to fetch the SyncStreamInstance


        :returns: The fetched SyncStreamInstance
        """
        return await self._proxy.fetch_async()

    def update(self, ttl: Union[int, object] = values.unset) -> "SyncStreamInstance":
        """
        Update the SyncStreamInstance

        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        """
        return self._proxy.update(
            ttl=ttl,
        )

    async def update_async(
        self, ttl: Union[int, object] = values.unset
    ) -> "SyncStreamInstance":
        """
        Asynchronous coroutine to update the SyncStreamInstance

        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        """
        return await self._proxy.update_async(
            ttl=ttl,
        )

    @property
    def stream_messages(self) -> StreamMessageList:
        """
        Access the stream_messages
        """
        return self._proxy.stream_messages

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.SyncStreamInstance {}>".format(context)


class SyncStreamContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SyncStreamContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to update.
        :param sid: The SID of the Stream resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Streams/{sid}".format(**self._solution)

        self._stream_messages: Optional[StreamMessageList] = None

    def delete(self) -> bool:
        """
        Deletes the SyncStreamInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncStreamInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SyncStreamInstance:
        """
        Fetch the SyncStreamInstance


        :returns: The fetched SyncStreamInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SyncStreamInstance:
        """
        Asynchronous coroutine to fetch the SyncStreamInstance


        :returns: The fetched SyncStreamInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, ttl: Union[int, object] = values.unset) -> SyncStreamInstance:
        """
        Update the SyncStreamInstance

        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, ttl: Union[int, object] = values.unset
    ) -> SyncStreamInstance:
        """
        Asynchronous coroutine to update the SyncStreamInstance

        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def stream_messages(self) -> StreamMessageList:
        """
        Access the stream_messages
        """
        if self._stream_messages is None:
            self._stream_messages = StreamMessageList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._stream_messages

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.SyncStreamContext {}>".format(context)


class SyncStreamPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SyncStreamInstance:
        """
        Build an instance of SyncStreamInstance

        :param payload: Payload response from the API
        """
        return SyncStreamInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.SyncStreamPage>"


class SyncStreamList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SyncStreamList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Stream resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Streams".format(**self._solution)

    def create(
        self,
        unique_name: Union[str, object] = values.unset,
        ttl: Union[int, object] = values.unset,
    ) -> SyncStreamInstance:
        """
        Create the SyncStreamInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The `unique_name` value can be used as an alternative to the `sid` in the URL path to address the resource.
        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The created SyncStreamInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "Ttl": ttl,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncStreamInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        unique_name: Union[str, object] = values.unset,
        ttl: Union[int, object] = values.unset,
    ) -> SyncStreamInstance:
        """
        Asynchronously create the SyncStreamInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The `unique_name` value can be used as an alternative to the `sid` in the URL path to address the resource.
        :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The created SyncStreamInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "Ttl": ttl,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncStreamInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SyncStreamInstance]:
        """
        Streams SyncStreamInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[SyncStreamInstance]:
        """
        Asynchronously streams SyncStreamInstance records from the API as a generator stream.
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
    ) -> List[SyncStreamInstance]:
        """
        Lists SyncStreamInstance records from the API as a list.
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
    ) -> List[SyncStreamInstance]:
        """
        Asynchronously lists SyncStreamInstance records from the API as a list.
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
    ) -> SyncStreamPage:
        """
        Retrieve a single page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncStreamInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncStreamPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SyncStreamPage:
        """
        Asynchronously retrieve a single page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncStreamInstance
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
        return SyncStreamPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SyncStreamPage:
        """
        Retrieve a specific page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncStreamInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncStreamPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SyncStreamPage:
        """
        Asynchronously retrieve a specific page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncStreamInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncStreamPage(self._version, response, self._solution)

    def get(self, sid: str) -> SyncStreamContext:
        """
        Constructs a SyncStreamContext

        :param sid: The SID of the Stream resource to update.
        """
        return SyncStreamContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> SyncStreamContext:
        """
        Constructs a SyncStreamContext

        :param sid: The SID of the Stream resource to update.
        """
        return SyncStreamContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.SyncStreamList>"