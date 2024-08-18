r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ApprovalCreateInstance(InstanceResource):
    """
    :ivar name:
    :ivar category:
    :ivar content_type:
    :ivar status:
    :ivar rejection_reason:
    :ivar allow_category_change:
    """

    def __init__(self, version: Version, payload: Dict[str, Any], content_sid: str):
        super().__init__(version)

        self.name: Optional[str] = payload.get("name")
        self.category: Optional[str] = payload.get("category")
        self.content_type: Optional[str] = payload.get("content_type")
        self.status: Optional[str] = payload.get("status")
        self.rejection_reason: Optional[str] = payload.get("rejection_reason")
        self.allow_category_change: Optional[bool] = payload.get(
            "allow_category_change"
        )

        self._solution = {
            "content_sid": content_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ApprovalCreateInstance {}>".format(context)


class ApprovalCreateList(ListResource):

    class ContentApprovalRequest(object):
        """
        :ivar name: Name of the template.
        :ivar category: A WhatsApp recognized template category.
        """

        def __init__(self, payload: Dict[str, Any], content_sid: str):

            self.name: Optional[str] = payload.get("name")
            self.category: Optional[str] = payload.get("category")

        def to_dict(self):
            return {
                "name": self.name,
                "category": self.category,
            }

    def __init__(self, version: Version, content_sid: str):
        """
        Initialize the ApprovalCreateList

        :param version: Version that contains the resource
        :param content_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "content_sid": content_sid,
        }
        self._uri = "/Content/{content_sid}/ApprovalRequests/whatsapp".format(
            **self._solution
        )

    def create(
        self, content_approval_request: ContentApprovalRequest
    ) -> ApprovalCreateInstance:
        """
        Create the ApprovalCreateInstance

        :param content_approval_request:

        :returns: The created ApprovalCreateInstance
        """
        data = content_approval_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ApprovalCreateInstance(
            self._version, payload, content_sid=self._solution["content_sid"]
        )

    async def create_async(
        self, content_approval_request: ContentApprovalRequest
    ) -> ApprovalCreateInstance:
        """
        Asynchronously create the ApprovalCreateInstance

        :param content_approval_request:

        :returns: The created ApprovalCreateInstance
        """
        data = content_approval_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ApprovalCreateInstance(
            self._version, payload, content_sid=self._solution["content_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ApprovalCreateList>"