r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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
from twilio.rest.api.v2010.account.queue.member import MemberList


class QueueInstance(InstanceResource):
    """
    :ivar date_updated: The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar current_size: The number of calls currently in the queue.
    :ivar friendly_name: A string that you assigned to describe this resource.
    :ivar uri: The URI of this resource, relative to `https://api.twilio.com`.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Queue resource.
    :ivar average_wait_time:  The average wait time in seconds of the members in this queue. This is calculated at the time of the request.
    :ivar sid: The unique string that that we created to identify this Queue resource.
    :ivar date_created: The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar max_size:  The maximum number of calls that can be in the queue. The default is 1000 and the maximum is 5000.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.current_size: Optional[int] = deserialize.integer(
            payload.get("current_size")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.uri: Optional[str] = payload.get("uri")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.average_wait_time: Optional[int] = deserialize.integer(
            payload.get("average_wait_time")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.max_size: Optional[int] = deserialize.integer(payload.get("max_size"))

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[QueueContext] = None

    @property
    def _proxy(self) -> "QueueContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: QueueContext for this QueueInstance
        """
        if self._context is None:
            self._context = QueueContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the QueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the QueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "QueueInstance":
        """
        Fetch the QueueInstance


        :returns: The fetched QueueInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "QueueInstance":
        """
        Asynchronous coroutine to fetch the QueueInstance


        :returns: The fetched QueueInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        max_size: Union[int, object] = values.unset,
    ) -> "QueueInstance":
        """
        Update the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The updated QueueInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            max_size=max_size,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        max_size: Union[int, object] = values.unset,
    ) -> "QueueInstance":
        """
        Asynchronous coroutine to update the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The updated QueueInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            max_size=max_size,
        )

    @property
    def members(self) -> MemberList:
        """
        Access the members
        """
        return self._proxy.members

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.QueueInstance {}>".format(context)


class QueueContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the QueueContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Queues/{sid}.json".format(**self._solution)

        self._members: Optional[MemberList] = None

    def delete(self) -> bool:
        """
        Deletes the QueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the QueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> QueueInstance:
        """
        Fetch the QueueInstance


        :returns: The fetched QueueInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> QueueInstance:
        """
        Asynchronous coroutine to fetch the QueueInstance


        :returns: The fetched QueueInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        max_size: Union[int, object] = values.unset,
    ) -> QueueInstance:
        """
        Update the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The updated QueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "MaxSize": max_size,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        max_size: Union[int, object] = values.unset,
    ) -> QueueInstance:
        """
        Asynchronous coroutine to update the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The updated QueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "MaxSize": max_size,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def members(self) -> MemberList:
        """
        Access the members
        """
        if self._members is None:
            self._members = MemberList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._members

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.QueueContext {}>".format(context)


class QueuePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> QueueInstance:
        """
        Build an instance of QueueInstance

        :param payload: Payload response from the API
        """
        return QueueInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.QueuePage>"


class QueueList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the QueueList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Queues.json".format(**self._solution)

    def create(
        self, friendly_name: str, max_size: Union[int, object] = values.unset
    ) -> QueueInstance:
        """
        Create the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The created QueueInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "MaxSize": max_size,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return QueueInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self, friendly_name: str, max_size: Union[int, object] = values.unset
    ) -> QueueInstance:
        """
        Asynchronously create the QueueInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

        :returns: The created QueueInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "MaxSize": max_size,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return QueueInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[QueueInstance]:
        """
        Streams QueueInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[QueueInstance]:
        """
        Asynchronously streams QueueInstance records from the API as a generator stream.
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
    ) -> List[QueueInstance]:
        """
        Lists QueueInstance records from the API as a list.
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
    ) -> List[QueueInstance]:
        """
        Asynchronously lists QueueInstance records from the API as a list.
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
    ) -> QueuePage:
        """
        Retrieve a single page of QueueInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of QueueInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return QueuePage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> QueuePage:
        """
        Asynchronously retrieve a single page of QueueInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of QueueInstance
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
        return QueuePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> QueuePage:
        """
        Retrieve a specific page of QueueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of QueueInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return QueuePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> QueuePage:
        """
        Asynchronously retrieve a specific page of QueueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of QueueInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return QueuePage(self._version, response, self._solution)

    def get(self, sid: str) -> QueueContext:
        """
        Constructs a QueueContext

        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
        """
        return QueueContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> QueueContext:
        """
        Constructs a QueueContext

        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
        """
        return QueueContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.QueueList>"