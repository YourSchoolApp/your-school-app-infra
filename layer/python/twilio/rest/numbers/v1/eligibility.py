r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class EligibilityInstance(InstanceResource):
    """
    :ivar results: The result set that contains the eligibility check response for the requested number, each result has at least the following attributes:  phone_number: The requested phone number ,hosting_account_sid: The account sid where the phone number will be hosted, date_last_checked: Datetime (ISO 8601) when the PN was last checked for eligibility, country: Phone number’s country, eligibility_status: Indicates the eligibility status of the PN (Eligible/Ineligible), eligibility_sub_status: Indicates the sub status of the eligibility , ineligibility_reason: Reason for number's ineligibility (if applicable), next_step: Suggested next step in the hosting process based on the eligibility status.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.results: Optional[List[Dict[str, object]]] = payload.get("results")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Numbers.V1.EligibilityInstance>"


class EligibilityList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the EligibilityList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/HostedNumber/Eligibility"

    def create(self, body: Union[object, object] = values.unset) -> EligibilityInstance:
        """
        Create the EligibilityInstance

        :param body:

        :returns: The created EligibilityInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return EligibilityInstance(self._version, payload)

    async def create_async(
        self, body: Union[object, object] = values.unset
    ) -> EligibilityInstance:
        """
        Asynchronously create the EligibilityInstance

        :param body:

        :returns: The created EligibilityInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return EligibilityInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.EligibilityList>"
