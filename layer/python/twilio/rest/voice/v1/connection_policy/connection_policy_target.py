r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ConnectionPolicyTargetInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Target resource.
    :ivar connection_policy_sid: The SID of the Connection Policy that owns the Target.
    :ivar sid: The unique string that we created to identify the Target resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    :ivar priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
    :ivar weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
    :ivar enabled: Whether the target is enabled. The default is `true`.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        connection_policy_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.connection_policy_sid: Optional[str] = payload.get("connection_policy_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.target: Optional[str] = payload.get("target")
        self.priority: Optional[int] = deserialize.integer(payload.get("priority"))
        self.weight: Optional[int] = deserialize.integer(payload.get("weight"))
        self.enabled: Optional[bool] = payload.get("enabled")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "connection_policy_sid": connection_policy_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ConnectionPolicyTargetContext] = None

    @property
    def _proxy(self) -> "ConnectionPolicyTargetContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConnectionPolicyTargetContext for this ConnectionPolicyTargetInstance
        """
        if self._context is None:
            self._context = ConnectionPolicyTargetContext(
                self._version,
                connection_policy_sid=self._solution["connection_policy_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ConnectionPolicyTargetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ConnectionPolicyTargetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ConnectionPolicyTargetInstance":
        """
        Fetch the ConnectionPolicyTargetInstance


        :returns: The fetched ConnectionPolicyTargetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ConnectionPolicyTargetInstance":
        """
        Asynchronous coroutine to fetch the ConnectionPolicyTargetInstance


        :returns: The fetched ConnectionPolicyTargetInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        target: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> "ConnectionPolicyTargetInstance":
        """
        Update the ConnectionPolicyTargetInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            target=target,
            priority=priority,
            weight=weight,
            enabled=enabled,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        target: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> "ConnectionPolicyTargetInstance":
        """
        Asynchronous coroutine to update the ConnectionPolicyTargetInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            target=target,
            priority=priority,
            weight=weight,
            enabled=enabled,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.ConnectionPolicyTargetInstance {}>".format(context)


class ConnectionPolicyTargetContext(InstanceContext):

    def __init__(self, version: Version, connection_policy_sid: str, sid: str):
        """
        Initialize the ConnectionPolicyTargetContext

        :param version: Version that contains the resource
        :param connection_policy_sid: The SID of the Connection Policy that owns the Target.
        :param sid: The unique string that we created to identify the Target resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "connection_policy_sid": connection_policy_sid,
            "sid": sid,
        }
        self._uri = "/ConnectionPolicies/{connection_policy_sid}/Targets/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the ConnectionPolicyTargetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ConnectionPolicyTargetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ConnectionPolicyTargetInstance:
        """
        Fetch the ConnectionPolicyTargetInstance


        :returns: The fetched ConnectionPolicyTargetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ConnectionPolicyTargetInstance:
        """
        Asynchronous coroutine to fetch the ConnectionPolicyTargetInstance


        :returns: The fetched ConnectionPolicyTargetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        target: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> ConnectionPolicyTargetInstance:
        """
        Update the ConnectionPolicyTargetInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Target": target,
                "Priority": priority,
                "Weight": weight,
                "Enabled": serialize.boolean_to_string(enabled),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        target: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> ConnectionPolicyTargetInstance:
        """
        Asynchronous coroutine to update the ConnectionPolicyTargetInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled.

        :returns: The updated ConnectionPolicyTargetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Target": target,
                "Priority": priority,
                "Weight": weight,
                "Enabled": serialize.boolean_to_string(enabled),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.ConnectionPolicyTargetContext {}>".format(context)


class ConnectionPolicyTargetPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ConnectionPolicyTargetInstance:
        """
        Build an instance of ConnectionPolicyTargetInstance

        :param payload: Payload response from the API
        """
        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.ConnectionPolicyTargetPage>"


class ConnectionPolicyTargetList(ListResource):

    def __init__(self, version: Version, connection_policy_sid: str):
        """
        Initialize the ConnectionPolicyTargetList

        :param version: Version that contains the resource
        :param connection_policy_sid: The SID of the Connection Policy from which to read the Targets.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "connection_policy_sid": connection_policy_sid,
        }
        self._uri = "/ConnectionPolicies/{connection_policy_sid}/Targets".format(
            **self._solution
        )

    def create(
        self,
        target: str,
        friendly_name: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> ConnectionPolicyTargetInstance:
        """
        Create the ConnectionPolicyTargetInstance

        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled. The default is `true`.

        :returns: The created ConnectionPolicyTargetInstance
        """

        data = values.of(
            {
                "Target": target,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Weight": weight,
                "Enabled": serialize.boolean_to_string(enabled),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
        )

    async def create_async(
        self,
        target: str,
        friendly_name: Union[str, object] = values.unset,
        priority: Union[int, object] = values.unset,
        weight: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> ConnectionPolicyTargetInstance:
        """
        Asynchronously create the ConnectionPolicyTargetInstance

        :param target: The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param priority: The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
        :param weight: The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
        :param enabled: Whether the Target is enabled. The default is `true`.

        :returns: The created ConnectionPolicyTargetInstance
        """

        data = values.of(
            {
                "Target": target,
                "FriendlyName": friendly_name,
                "Priority": priority,
                "Weight": weight,
                "Enabled": serialize.boolean_to_string(enabled),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sid=self._solution["connection_policy_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ConnectionPolicyTargetInstance]:
        """
        Streams ConnectionPolicyTargetInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[ConnectionPolicyTargetInstance]:
        """
        Asynchronously streams ConnectionPolicyTargetInstance records from the API as a generator stream.
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
    ) -> List[ConnectionPolicyTargetInstance]:
        """
        Lists ConnectionPolicyTargetInstance records from the API as a list.
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
    ) -> List[ConnectionPolicyTargetInstance]:
        """
        Asynchronously lists ConnectionPolicyTargetInstance records from the API as a list.
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
    ) -> ConnectionPolicyTargetPage:
        """
        Retrieve a single page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectionPolicyTargetInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ConnectionPolicyTargetPage:
        """
        Asynchronously retrieve a single page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectionPolicyTargetInstance
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
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ConnectionPolicyTargetPage:
        """
        Retrieve a specific page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConnectionPolicyTargetInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ConnectionPolicyTargetPage:
        """
        Asynchronously retrieve a specific page of ConnectionPolicyTargetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConnectionPolicyTargetInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ConnectionPolicyTargetPage(self._version, response, self._solution)

    def get(self, sid: str) -> ConnectionPolicyTargetContext:
        """
        Constructs a ConnectionPolicyTargetContext

        :param sid: The unique string that we created to identify the Target resource to update.
        """
        return ConnectionPolicyTargetContext(
            self._version,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> ConnectionPolicyTargetContext:
        """
        Constructs a ConnectionPolicyTargetContext

        :param sid: The unique string that we created to identify the Target resource to update.
        """
        return ConnectionPolicyTargetContext(
            self._version,
            connection_policy_sid=self._solution["connection_policy_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.ConnectionPolicyTargetList>"
