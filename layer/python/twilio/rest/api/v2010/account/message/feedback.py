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
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class FeedbackInstance(InstanceResource):

    class Outcome(object):
        CONFIRMED = "confirmed"
        UNCONFIRMED = "unconfirmed"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with this MessageFeedback resource.
    :ivar message_sid: The SID of the Message resource associated with this MessageFeedback resource.
    :ivar outcome: 
    :ivar date_created: The date and time in GMT when this MessageFeedback resource was created, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when this MessageFeedback resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        message_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.message_sid: Optional[str] = payload.get("message_sid")
        self.outcome: Optional["FeedbackInstance.Outcome"] = payload.get("outcome")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "message_sid": message_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.FeedbackInstance {}>".format(context)


class FeedbackList(ListResource):

    def __init__(self, version: Version, account_sid: str, message_sid: str):
        """
        Initialize the FeedbackList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback.
        :param message_sid: The SID of the Message resource for which to create MessageFeedback.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "message_sid": message_sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Messages/{message_sid}/Feedback.json".format(
                **self._solution
            )
        )

    def create(
        self, outcome: Union["FeedbackInstance.Outcome", object] = values.unset
    ) -> FeedbackInstance:
        """
        Create the FeedbackInstance

        :param outcome:

        :returns: The created FeedbackInstance
        """

        data = values.of(
            {
                "Outcome": outcome,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
        )

    async def create_async(
        self, outcome: Union["FeedbackInstance.Outcome", object] = values.unset
    ) -> FeedbackInstance:
        """
        Asynchronously create the FeedbackInstance

        :param outcome:

        :returns: The created FeedbackInstance
        """

        data = values.of(
            {
                "Outcome": outcome,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.FeedbackList>"