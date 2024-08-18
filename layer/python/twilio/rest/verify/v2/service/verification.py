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
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class VerificationInstance(InstanceResource):

    class Channel(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"
        SNA = "sna"

    class RiskCheck(object):
        ENABLE = "enable"
        DISABLE = "disable"

    class Status(object):
        CANCELED = "canceled"
        APPROVED = "approved"

    """
    :ivar sid: The unique string that we created to identify the Verification resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource.
    :ivar to: The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    :ivar channel: 
    :ivar status: The status of the verification. Can be: `pending`, `approved`, `canceled`, `max_attempts_reached`, `deleted`, `failed` or `expired`.
    :ivar valid: Use \"status\" instead. Legacy property indicating whether the verification was successful.
    :ivar lookup: Information about the phone number being verified.
    :ivar amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :ivar payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
    :ivar send_code_attempts: An array of verification attempt objects containing the channel attempted and the channel-specific transaction SID.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar sna: The set of fields used for a silent network auth (`sna`) verification. Contains a single field with the URL to be invoked to verify the phone number.
    :ivar url: The absolute URL of the Verification resource.
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
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.to: Optional[str] = payload.get("to")
        self.channel: Optional["VerificationInstance.Channel"] = payload.get("channel")
        self.status: Optional[str] = payload.get("status")
        self.valid: Optional[bool] = payload.get("valid")
        self.lookup: Optional[Dict[str, object]] = payload.get("lookup")
        self.amount: Optional[str] = payload.get("amount")
        self.payee: Optional[str] = payload.get("payee")
        self.send_code_attempts: Optional[List[Dict[str, object]]] = payload.get(
            "send_code_attempts"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.sna: Optional[Dict[str, object]] = payload.get("sna")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[VerificationContext] = None

    @property
    def _proxy(self) -> "VerificationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationContext for this VerificationInstance
        """
        if self._context is None:
            self._context = VerificationContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "VerificationInstance":
        """
        Fetch the VerificationInstance


        :returns: The fetched VerificationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "VerificationInstance":
        """
        Asynchronous coroutine to fetch the VerificationInstance


        :returns: The fetched VerificationInstance
        """
        return await self._proxy.fetch_async()

    def update(self, status: "VerificationInstance.Status") -> "VerificationInstance":
        """
        Update the VerificationInstance

        :param status:

        :returns: The updated VerificationInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "VerificationInstance.Status"
    ) -> "VerificationInstance":
        """
        Asynchronous coroutine to update the VerificationInstance

        :param status:

        :returns: The updated VerificationInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.VerificationInstance {}>".format(context)


class VerificationContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the VerificationContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to update the resource from.
        :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Verifications/{sid}".format(
            **self._solution
        )

    def fetch(self) -> VerificationInstance:
        """
        Fetch the VerificationInstance


        :returns: The fetched VerificationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> VerificationInstance:
        """
        Asynchronous coroutine to fetch the VerificationInstance


        :returns: The fetched VerificationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, status: "VerificationInstance.Status") -> VerificationInstance:
        """
        Update the VerificationInstance

        :param status:

        :returns: The updated VerificationInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status: "VerificationInstance.Status"
    ) -> VerificationInstance:
        """
        Asynchronous coroutine to update the VerificationInstance

        :param status:

        :returns: The updated VerificationInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VerificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.VerificationContext {}>".format(context)


class VerificationList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the VerificationList

        :param version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Verifications".format(**self._solution)

    def create(
        self,
        to: str,
        channel: str,
        custom_friendly_name: Union[str, object] = values.unset,
        custom_message: Union[str, object] = values.unset,
        send_digits: Union[str, object] = values.unset,
        locale: Union[str, object] = values.unset,
        custom_code: Union[str, object] = values.unset,
        amount: Union[str, object] = values.unset,
        payee: Union[str, object] = values.unset,
        rate_limits: Union[object, object] = values.unset,
        channel_configuration: Union[object, object] = values.unset,
        app_hash: Union[str, object] = values.unset,
        template_sid: Union[str, object] = values.unset,
        template_custom_substitutions: Union[str, object] = values.unset,
        device_ip: Union[str, object] = values.unset,
        risk_check: Union["VerificationInstance.RiskCheck", object] = values.unset,
        tags: Union[str, object] = values.unset,
    ) -> VerificationInstance:
        """
        Create the VerificationInstance

        :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param channel: The verification method to use. One of: [`email`](https://www.twilio.com/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.
        :param custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the verification message
        :param custom_message: The text of a custom message to use for the verification.
        :param send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
        :param locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
        :param custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
        :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
        :param channel_configuration: [`email`](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.
        :param app_hash: Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.
        :param template_sid: The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
        :param template_custom_substitutions: A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.
        :param device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.
        :param risk_check:
        :param tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length.

        :returns: The created VerificationInstance
        """

        data = values.of(
            {
                "To": to,
                "Channel": channel,
                "CustomFriendlyName": custom_friendly_name,
                "CustomMessage": custom_message,
                "SendDigits": send_digits,
                "Locale": locale,
                "CustomCode": custom_code,
                "Amount": amount,
                "Payee": payee,
                "RateLimits": serialize.object(rate_limits),
                "ChannelConfiguration": serialize.object(channel_configuration),
                "AppHash": app_hash,
                "TemplateSid": template_sid,
                "TemplateCustomSubstitutions": template_custom_substitutions,
                "DeviceIp": device_ip,
                "RiskCheck": risk_check,
                "Tags": tags,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return VerificationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        to: str,
        channel: str,
        custom_friendly_name: Union[str, object] = values.unset,
        custom_message: Union[str, object] = values.unset,
        send_digits: Union[str, object] = values.unset,
        locale: Union[str, object] = values.unset,
        custom_code: Union[str, object] = values.unset,
        amount: Union[str, object] = values.unset,
        payee: Union[str, object] = values.unset,
        rate_limits: Union[object, object] = values.unset,
        channel_configuration: Union[object, object] = values.unset,
        app_hash: Union[str, object] = values.unset,
        template_sid: Union[str, object] = values.unset,
        template_custom_substitutions: Union[str, object] = values.unset,
        device_ip: Union[str, object] = values.unset,
        risk_check: Union["VerificationInstance.RiskCheck", object] = values.unset,
        tags: Union[str, object] = values.unset,
    ) -> VerificationInstance:
        """
        Asynchronously create the VerificationInstance

        :param to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param channel: The verification method to use. One of: [`email`](https://www.twilio.com/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.
        :param custom_friendly_name: A custom user defined friendly name that overwrites the existing one in the verification message
        :param custom_message: The text of a custom message to use for the verification.
        :param send_digits: The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](https://www.twilio.com/docs/voice/twiml/number#attributes-sendDigits).
        :param locale: Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](https://www.twilio.com/docs/verify/supported-languages).
        :param custom_code: A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.
        :param amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param rate_limits: The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](https://www.twilio.com/docs/verify/api/service-rate-limits). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.
        :param channel_configuration: [`email`](https://www.twilio.com/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.
        :param app_hash: Your [App Hash](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string) to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.
        :param template_sid: The message [template](https://www.twilio.com/docs/verify/api/templates). If provided, will override the default template for the Service. SMS and Voice channels only.
        :param template_custom_substitutions: A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.
        :param device_ip: Strongly encouraged if using the auto channel. The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.
        :param risk_check:
        :param tags: A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length.

        :returns: The created VerificationInstance
        """

        data = values.of(
            {
                "To": to,
                "Channel": channel,
                "CustomFriendlyName": custom_friendly_name,
                "CustomMessage": custom_message,
                "SendDigits": send_digits,
                "Locale": locale,
                "CustomCode": custom_code,
                "Amount": amount,
                "Payee": payee,
                "RateLimits": serialize.object(rate_limits),
                "ChannelConfiguration": serialize.object(channel_configuration),
                "AppHash": app_hash,
                "TemplateSid": template_sid,
                "TemplateCustomSubstitutions": template_custom_substitutions,
                "DeviceIp": device_ip,
                "RiskCheck": risk_check,
                "Tags": tags,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return VerificationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def get(self, sid: str) -> VerificationContext:
        """
        Constructs a VerificationContext

        :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
        """
        return VerificationContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> VerificationContext:
        """
        Constructs a VerificationContext

        :param sid: The Twilio-provided string that uniquely identifies the Verification resource to update.
        """
        return VerificationContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.VerificationList>"
