r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class VerificationCheckInstance(InstanceResource):

    class Channel(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"
        SNA = "sna"

    """
    :ivar sid: The unique string that we created to identify the VerificationCheck resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the VerificationCheck resource.
    :ivar to: The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :ivar channel: 
    :ivar status: The status of the verification. Can be: `pending`, `approved`, `canceled`, `max_attempts_reached`, `deleted`, `failed` or `expired`.
    :ivar valid: Use \"status\" instead. Legacy property indicating whether the verification was successful.
    :ivar amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :ivar payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was last updated.
    :ivar sna_attempts_error_codes: List of error codes as a result of attempting a verification using the `sna` channel. The error codes are chronologically ordered, from the first attempt to the latest attempt. This will be an empty list if no errors occured or `null` if the last channel used wasn't `sna`.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], service_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.to: Optional[str] = payload.get("to")
        self.channel: Optional["VerificationCheckInstance.Channel"] = payload.get(
            "channel"
        )
        self.status: Optional[str] = payload.get("status")
        self.valid: Optional[bool] = payload.get("valid")
        self.amount: Optional[str] = payload.get("amount")
        self.payee: Optional[str] = payload.get("payee")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.sna_attempts_error_codes: Optional[List[Dict[str, object]]] = payload.get(
            "sna_attempts_error_codes"
        )

        self._solution = {
            "service_sid": service_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.VerificationCheckInstance {}>".format(context)


class VerificationCheckList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the VerificationCheckList

        :param version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/VerificationCheck".format(**self._solution)

    def create(
        self,
        code: Union[str, object] = values.unset,
        to: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        amount: Union[str, object] = values.unset,
        payee: Union[str, object] = values.unset,
    ) -> VerificationCheckInstance:
        """
        Create the VerificationCheckInstance

        :param code: The 4-10 character string being verified.
        :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
        :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

        :returns: The created VerificationCheckInstance
        """

        data = values.of(
            {
                "Code": code,
                "To": to,
                "VerificationSid": verification_sid,
                "Amount": amount,
                "Payee": payee,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return VerificationCheckInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        code: Union[str, object] = values.unset,
        to: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        amount: Union[str, object] = values.unset,
        payee: Union[str, object] = values.unset,
    ) -> VerificationCheckInstance:
        """
        Asynchronously create the VerificationCheckInstance

        :param code: The 4-10 character string being verified.
        :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
        :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

        :returns: The created VerificationCheckInstance
        """

        data = values.of(
            {
                "Code": code,
                "To": to,
                "VerificationSid": verification_sid,
                "Amount": amount,
                "Payee": payee,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return VerificationCheckInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.VerificationCheckList>"