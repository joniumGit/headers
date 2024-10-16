"""HTTP Headers as str

see: https://www.iana.org/assignments/http-fields/http-fields.xhtml
"""

A_IM = "A-IM"
"""A-IM []

[RFC 3229: Delta encoding in HTTP]
"""

ACCEPT = "Accept"
"""Accept []

[RFC9110, Section 12.5.1: HTTP Semantics]
"""

ACCEPT_ADDITIONS = "Accept-Additions"
"""Accept-Additions []

[RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)]
"""

ACCEPT_CH = "Accept-CH"
"""Accept-CH [List]

[RFC 8942, Section 3.1: HTTP Client Hints]
"""

ACCEPT_CHARSET = "Accept-Charset"
"""Accept-Charset []

[RFC9110, Section 12.5.2: HTTP Semantics]
"""

ACCEPT_DATETIME = "Accept-Datetime"
"""Accept-Datetime []

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

ACCEPT_ENCODING = "Accept-Encoding"
"""Accept-Encoding []

[RFC9110, Section 12.5.3: HTTP Semantics]
"""

ACCEPT_FEATURES = "Accept-Features"
"""Accept-Features []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

ACCEPT_LANGUAGE = "Accept-Language"
"""Accept-Language []

[RFC9110, Section 12.5.4: HTTP Semantics]
"""

ACCEPT_PATCH = "Accept-Patch"
"""Accept-Patch []

[RFC 5789: PATCH Method for HTTP]
"""

ACCEPT_POST = "Accept-Post"
"""Accept-Post []

[Linked Data Platform 1.0]
"""

ACCEPT_RANGES = "Accept-Ranges"
"""Accept-Ranges []

[RFC9110, Section 14.3: HTTP Semantics]
"""

ACCEPT_SIGNATURE = "Accept-Signature"
"""Accept-Signature []

[RFC 9421, Section 5.1: HTTP Message Signatures]
"""

ACCESS_CONTROL = "Access-Control"
"""Access-Control []

[Access Control for Cross-site Requests]
"""

ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
"""Access-Control-Allow-Credentials []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
"""Access-Control-Allow-Headers []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
"""Access-Control-Allow-Methods []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
"""Access-Control-Allow-Origin []

[Fetch]
"""

ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
"""Access-Control-Expose-Headers []

[Fetch]
"""

ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
"""Access-Control-Max-Age []

[Fetch]
"""

ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers"
"""Access-Control-Request-Headers []

[Fetch]
"""

ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method"
"""Access-Control-Request-Method []

[Fetch]
"""

AGE = "Age"
"""Age []

[RFC9111, Section 5.1: HTTP Caching]
"""

ALLOW = "Allow"
"""Allow []

[RFC9110, Section 10.2.1: HTTP Semantics]
"""

ALPN = "ALPN"
"""ALPN []

[RFC 7639, Section 2: The ALPN HTTP Header Field]
"""

ALT_SVC = "Alt-Svc"
"""Alt-Svc []

[RFC 7838: HTTP Alternative Services]
"""

ALT_USED = "Alt-Used"
"""Alt-Used []

[RFC 7838: HTTP Alternative Services]
"""

ALTERNATES = "Alternates"
"""Alternates []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

AMP_CACHE_TRANSFORM = "AMP-Cache-Transform"
"""AMP-Cache-Transform []

[AMP-Cache-Transform HTTP request header]
"""

APPLY_TO_REDIRECT_REF = "Apply-To-Redirect-Ref"
"""Apply-To-Redirect-Ref []

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

AUTHENTICATION_CONTROL = "Authentication-Control"
"""Authentication-Control []

[RFC 8053, Section 4: HTTP Authentication Extensions for Interactive Clients]
"""

AUTHENTICATION_INFO = "Authentication-Info"
"""Authentication-Info []

[RFC9110, Section 11.6.3: HTTP Semantics]
"""

AUTHORIZATION = "Authorization"
"""Authorization []

[RFC9110, Section 11.6.2: HTTP Semantics]
"""

AVAILABLE_DICTIONARY = "Available-Dictionary"
"""Available-Dictionary []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.2: Compression Dictionary Transport]
"""

C_EXT = "C-Ext"
"""C-Ext []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_MAN = "C-Man"
"""C-Man []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_OPT = "C-Opt"
"""C-Opt []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_PEP = "C-PEP"
"""C-PEP []

[PEP - an Extension Mechanism for HTTP]

[Status change of HTTP experiments to Historic]
"""

C_PEP_INFO = "C-PEP-Info"
"""C-PEP-Info []

[PEP - an Extension Mechanism for HTTP]

[Status change of HTTP experiments to Historic]
"""

CACHE_CONTROL = "Cache-Control"
"""Cache-Control []

[RFC9111, Section 5.2]
"""

CACHE_STATUS = "Cache-Status"
"""Cache-Status [List]

[RFC9211: The Cache-Status HTTP Response Header Field]
"""

CAL_MANAGED_ID = "Cal-Managed-ID"
"""Cal-Managed-ID []

[RFC 8607, Section 5.1: Calendaring Extensions to WebDAV (CalDAV): Managed Attachments]
"""

CALDAV_TIMEZONES = "CalDAV-Timezones"
"""CalDAV-Timezones []

[RFC 7809, Section 7.1: Calendaring Extensions to WebDAV (CalDAV): Time Zones by Reference]
"""

CAPSULE_PROTOCOL = "Capsule-Protocol"
"""Capsule-Protocol []

[RFC9297]
"""

CDN_CACHE_CONTROL = "CDN-Cache-Control"
"""CDN-Cache-Control [Dictionary]

[RFC9213: Targeted HTTP Cache Control]

Cache directives targeted at content delivery networks
"""

CDN_LOOP = "CDN-Loop"
"""CDN-Loop []

[RFC 8586: Loop Detection in Content Delivery Networks (CDNs)]
"""

CERT_NOT_AFTER = "Cert-Not-After"
"""Cert-Not-After []

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CERT_NOT_BEFORE = "Cert-Not-Before"
"""Cert-Not-Before []

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CLEAR_SITE_DATA = "Clear-Site-Data"
"""Clear-Site-Data []

[Clear Site Data]
"""

CLIENT_CERT = "Client-Cert"
"""Client-Cert [Item]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLIENT_CERT_CHAIN = "Client-Cert-Chain"
"""Client-Cert-Chain [List]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLOSE = "Close"
"""Close []

[RFC9112, Section 9.6: HTTP/1.1]

(reserved)
"""

CMCD_OBJECT = "CMCD-Object"
"""CMCD-Object []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_REQUEST = "CMCD-Request"
"""CMCD-Request []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_SESSION = "CMCD-Session"
"""CMCD-Session []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_STATUS = "CMCD-Status"
"""CMCD-Status []

[CTA][CTA-5004 Common Media Client Data]
"""

CMSD_DYNAMIC = "CMSD-Dynamic"
"""CMSD-Dynamic []

[CTA][CTA-5006 Common Media Server Data (CMSD)]
"""

CMSD_STATIC = "CMSD-Static"
"""CMSD-Static []

[CTA][CTA-5006 Common Media Server Data (CMSD)]
"""

CONCEALED_AUTH_EXPORT = "Concealed-Auth-Export"
"""Concealed-Auth-Export [Item]

[RFC-ietf-httpbis-unprompted-auth-12: The Concealed HTTP Authentication Scheme]
"""

CONFIGURATION_CONTEXT = "Configuration-Context"
"""Configuration-Context []

[OSLC Configuration Management Version 1.0. Part 3: Configuration Specification]
"""

CONNECTION = "Connection"
"""Connection []

[RFC9110, Section 7.6.1: HTTP Semantics]
"""

CONTENT_BASE = "Content-Base"
"""Content-Base []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]

Obsoleted by [RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1]
"""

CONTENT_DIGEST = "Content-Digest"
"""Content-Digest []

[RFC 9530, Section 2: Digest Fields]
"""

CONTENT_DISPOSITION = "Content-Disposition"
"""Content-Disposition []

[RFC 6266: Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP)]
"""

CONTENT_ENCODING = "Content-Encoding"
"""Content-Encoding []

[RFC9110, Section 8.4: HTTP Semantics]
"""

CONTENT_ID = "Content-ID"
"""Content-ID []

[The HTTP Distribution and Replication Protocol]
"""

CONTENT_LANGUAGE = "Content-Language"
"""Content-Language []

[RFC9110, Section 8.5: HTTP Semantics]
"""

CONTENT_LENGTH = "Content-Length"
"""Content-Length []

[RFC9110, Section 8.6: HTTP Semantics]
"""

CONTENT_LOCATION = "Content-Location"
"""Content-Location []

[RFC9110, Section 8.7: HTTP Semantics]
"""

CONTENT_MD5 = "Content-MD5"
"""Content-MD5 []

[RFC 2616, Section 14.15: Hypertext Transfer Protocol -- HTTP/1.1]

Obsoleted by [RFC 7231, Appendix B: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content]
"""

CONTENT_RANGE = "Content-Range"
"""Content-Range []

[RFC9110, Section 14.4: HTTP Semantics]
"""

CONTENT_SCRIPT_TYPE = "Content-Script-Type"
"""Content-Script-Type []

[HTML 4.01 Specification]
"""

CONTENT_SECURITY_POLICY = "Content-Security-Policy"
"""Content-Security-Policy []

[Content Security Policy Level 3]
"""

CONTENT_SECURITY_POLICY_REPORT_ONLY = "Content-Security-Policy-Report-Only"
"""Content-Security-Policy-Report-Only []

[Content Security Policy Level 3]
"""

CONTENT_STYLE_TYPE = "Content-Style-Type"
"""Content-Style-Type []

[HTML 4.01 Specification]
"""

CONTENT_TYPE = "Content-Type"
"""Content-Type []

[RFC9110, Section 8.3: HTTP Semantics]
"""

CONTENT_VERSION = "Content-Version"
"""Content-Version []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

COOKIE = "Cookie"
"""Cookie []

[RFC 6265: HTTP State Management Mechanism]
"""

COOKIE2 = "Cookie2"
"""Cookie2 []

[RFC 2965: HTTP State Management Mechanism]

Obsoleted by [RFC 6265: HTTP State Management Mechanism]
"""

CROSS_ORIGIN_EMBEDDER_POLICY = "Cross-Origin-Embedder-Policy"
"""Cross-Origin-Embedder-Policy [Item]

[HTML]
"""

CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY = "Cross-Origin-Embedder-Policy-Report-Only"
"""Cross-Origin-Embedder-Policy-Report-Only [Item]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY = "Cross-Origin-Opener-Policy"
"""Cross-Origin-Opener-Policy [Item]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY_REPORT_ONLY = "Cross-Origin-Opener-Policy-Report-Only"
"""Cross-Origin-Opener-Policy-Report-Only [Item]

[HTML]
"""

CROSS_ORIGIN_RESOURCE_POLICY = "Cross-Origin-Resource-Policy"
"""Cross-Origin-Resource-Policy []

[Fetch]
"""

CTA_COMMON_ACCESS_TOKEN = "CTA-Common-Access-Token"
"""CTA-Common-Access-Token []

[CTA][Chris_Lemmons]
"""

DASL = "DASL"
"""DASL []

[RFC 5323: Web Distributed Authoring and Versioning (WebDAV) SEARCH]
"""

DATE = "Date"
"""Date []

[RFC9110, Section 6.6.1: HTTP Semantics]
"""

DAV = "DAV"
"""DAV []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DEFAULT_STYLE = "Default-Style"
"""Default-Style []

[HTML 4.01 Specification]
"""

DELTA_BASE = "Delta-Base"
"""Delta-Base []

[RFC 3229: Delta encoding in HTTP]
"""

DEPRECATION = "Deprecation"
"""Deprecation [Item]

[RFC-ietf-httpapi-deprecation-header-09, Section 2: The Deprecation HTTP Response Header Field]
"""

DEPTH = "Depth"
"""Depth []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DERIVED_FROM = "Derived-From"
"""Derived-From []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

DESTINATION = "Destination"
"""Destination []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DIFFERENTIAL_ID = "Differential-ID"
"""Differential-ID []

[The HTTP Distribution and Replication Protocol]
"""

DICTIONARY_ID = "Dictionary-ID"
"""Dictionary-ID []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.3: Compression Dictionary Transport]
"""

DIGEST = "Digest"
"""Digest []

[RFC 3230: Instance Digests in HTTP]

Obsoleted by [RFC 9530, Section 1.3: Digest Fields]
"""

DPOP = "DPoP"
"""DPoP []

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

DPOP_NONCE = "DPoP-Nonce"
"""DPoP-Nonce []

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

EARLY_DATA = "Early-Data"
"""Early-Data []

[RFC 8470: Using Early Data in HTTP]
"""

EDIINT_FEATURES = "EDIINT-Features"
"""EDIINT-Features []

[RFC 6017: Electronic Data Interchange - Internet Integration (EDIINT) Features Header Field]
"""

ETAG = "ETag"
"""ETag []

[RFC9110, Section 8.8.3: HTTP Semantics]
"""

EXPECT = "Expect"
"""Expect []

[RFC9110, Section 10.1.1: HTTP Semantics]
"""

EXPECT_CT = "Expect-CT"
"""Expect-CT []

[RFC9163: Expect-CT Extension for HTTP]

Obsoleted by [IESG]        [HTTPBIS]
"""

EXPIRES = "Expires"
"""Expires []

[RFC9111, Section 5.3: HTTP Caching]
"""

EXT = "Ext"
"""Ext []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

FORWARDED = "Forwarded"
"""Forwarded []

[RFC 7239: Forwarded HTTP Extension]
"""

FROM = "From"
"""From []

[RFC9110, Section 10.1.2: HTTP Semantics]
"""

GETPROFILE = "GetProfile"
"""GetProfile []

[Implementation of OPS Over HTTP]
"""

HOBAREG = "Hobareg"
"""Hobareg []

[RFC 7486, Section 6.1.1: HTTP Origin-Bound Authentication (HOBA)]
"""

HOST = "Host"
"""Host []

[RFC9110, Section 7.2: HTTP Semantics]
"""

HTTP2_SETTINGS = "HTTP2-Settings"
"""HTTP2-Settings []

[RFC 7540, Section 3.2.1: Hypertext Transfer Protocol Version 2 (HTTP/2)]

Obsolete; see Section 11.1 of [RFC9113]
"""

IF = "If"
"""If []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

IF_MATCH = "If-Match"
"""If-Match []

[RFC9110, Section 13.1.1: HTTP Semantics]
"""

IF_MODIFIED_SINCE = "If-Modified-Since"
"""If-Modified-Since []

[RFC9110, Section 13.1.3: HTTP Semantics]
"""

IF_NONE_MATCH = "If-None-Match"
"""If-None-Match []

[RFC9110, Section 13.1.2: HTTP Semantics]
"""

IF_RANGE = "If-Range"
"""If-Range []

[RFC9110, Section 13.1.5: HTTP Semantics]
"""

IF_SCHEDULE_TAG_MATCH = "If-Schedule-Tag-Match"
"""If-Schedule-Tag-Match []

[ RFC 6338: Scheduling Extensions to CalDAV]
"""

IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
"""If-Unmodified-Since []

[RFC9110, Section 13.1.4: HTTP Semantics]
"""

IM = "IM"
"""IM []

[RFC 3229: Delta encoding in HTTP]
"""

INCLUDE_REFERRED_TOKEN_BINDING_ID = "Include-Referred-Token-Binding-ID"
"""Include-Referred-Token-Binding-ID []

[RFC 8473: Token Binding over HTTP]
"""

ISOLATION = "Isolation"
"""Isolation []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

KEEP_ALIVE = "Keep-Alive"
"""Keep-Alive []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

LABEL = "Label"
"""Label []

[RFC 3253: Versioning Extensions to WebDAV: (Web Distributed Authoring and Versioning)]
"""

LAST_EVENT_ID = "Last-Event-ID"
"""Last-Event-ID []

[HTML]
"""

LAST_MODIFIED = "Last-Modified"
"""Last-Modified []

[RFC9110, Section 8.8.2: HTTP Semantics]
"""

LINK = "Link"
"""Link []

[RFC 8288: Web Linking]
"""

LINK_TEMPLATE = "Link-Template"
"""Link-Template []

[RFC 9652: The Link-Template HTTP Header Field]
"""

LOCATION = "Location"
"""Location []

[RFC9110, Section 10.2.2: HTTP Semantics]
"""

LOCK_TOKEN = "Lock-Token"
"""Lock-Token []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

MAN = "Man"
"""Man []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

MAX_FORWARDS = "Max-Forwards"
"""Max-Forwards []

[RFC9110, Section 7.6.2: HTTP Semantics]
"""

MEMENTO_DATETIME = "Memento-Datetime"
"""Memento-Datetime []

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

METER = "Meter"
"""Meter []

[RFC 2227: Simple Hit-Metering and Usage-Limiting for HTTP]
"""

METHOD_CHECK = "Method-Check"
"""Method-Check []

[Access Control for Cross-site Requests]
"""

METHOD_CHECK_EXPIRES = "Method-Check-Expires"
"""Method-Check-Expires []

[Access Control for Cross-site Requests]
"""

MIME_VERSION = "MIME-Version"
"""MIME-Version []

[RFC9112, Appendix B.1: HTTP/1.1]
"""

NEGOTIATE = "Negotiate"
"""Negotiate []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

NEL = "NEL"
"""NEL []

[Network Error Logging]
"""

ODATA_ENTITYID = "OData-EntityId"
"""OData-EntityId []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_ISOLATION = "OData-Isolation"
"""OData-Isolation []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_MAXVERSION = "OData-MaxVersion"
"""OData-MaxVersion []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_VERSION = "OData-Version"
"""OData-Version []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

OPT = "Opt"
"""Opt []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

OPTIONAL_WWW_AUTHENTICATE = "Optional-WWW-Authenticate"
"""Optional-WWW-Authenticate []

[RFC 8053, Section 3: HTTP Authentication Extensions for Interactive Clients]
"""

ORDERING_TYPE = "Ordering-Type"
"""Ordering-Type []

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

ORIGIN = "Origin"
"""Origin []

[RFC 6454: The Web Origin Concept]
"""

ORIGIN_AGENT_CLUSTER = "Origin-Agent-Cluster"
"""Origin-Agent-Cluster [Item]

[HTML]
"""

OSCORE = "OSCORE"
"""OSCORE []

[RFC 8613, Section 11.1: Object Security for Constrained RESTful Environments (OSCORE)]
"""

OSLC_CORE_VERSION = "OSLC-Core-Version"
"""OSLC-Core-Version []

[OASIS Project Specification 01][OASIS][Chet_Ensign]
"""

OVERWRITE = "Overwrite"
"""Overwrite []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

P3P = "P3P"
"""P3P []

[The Platform for Privacy Preferences 1.0 (P3P1.0) Specification]
"""

PEP = "PEP"
"""PEP []

[PEP - an Extension Mechanism for HTTP]
"""

PEP_INFO = "PEP-Info"
"""PEP-Info []

[PEP - an Extension Mechanism for HTTP]
"""

PERMISSIONS_POLICY = "Permissions-Policy"
"""Permissions-Policy []

[Permissions Policy]
"""

PICS_LABEL = "PICS-Label"
"""PICS-Label []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PING_FROM = "Ping-From"
"""Ping-From []

[HTML]
"""

PING_TO = "Ping-To"
"""Ping-To []

[HTML]
"""

POSITION = "Position"
"""Position []

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

PRAGMA = "Pragma"
"""Pragma []

[RFC9111, Section 5.4: HTTP Caching]
"""

PREFER = "Prefer"
"""Prefer []

[RFC 7240: Prefer Header for HTTP]
"""

PREFERENCE_APPLIED = "Preference-Applied"
"""Preference-Applied []

[RFC 7240: Prefer Header for HTTP]
"""

PRIORITY = "Priority"
"""Priority [Dictionary]

[RFC9218: Extensible Prioritization Scheme for HTTP]
"""

PROFILEOBJECT = "ProfileObject"
"""ProfileObject []

[Implementation of OPS Over HTTP]
"""

PROTOCOL = "Protocol"
"""Protocol []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROTOCOL_INFO = "Protocol-Info"
"""Protocol-Info []

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_QUERY = "Protocol-Query"
"""Protocol-Query []

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_REQUEST = "Protocol-Request"
"""Protocol-Request []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROXY_AUTHENTICATE = "Proxy-Authenticate"
"""Proxy-Authenticate []

[RFC9110, Section 11.7.1: HTTP Semantics]
"""

PROXY_AUTHENTICATION_INFO = "Proxy-Authentication-Info"
"""Proxy-Authentication-Info []

[RFC9110, Section 11.7.3: HTTP Semantics]
"""

PROXY_AUTHORIZATION = "Proxy-Authorization"
"""Proxy-Authorization []

[RFC9110, Section 11.7.2: HTTP Semantics]
"""

PROXY_FEATURES = "Proxy-Features"
"""Proxy-Features []

[Notification for Proxy Caches]
"""

PROXY_INSTRUCTION = "Proxy-Instruction"
"""Proxy-Instruction []

[Notification for Proxy Caches]
"""

PROXY_STATUS = "Proxy-Status"
"""Proxy-Status [List]

[RFC9209: The Proxy-Status HTTP Response Header Field]
"""

PUBLIC = "Public"
"""Public []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

PUBLIC_KEY_PINS = "Public-Key-Pins"
"""Public-Key-Pins []

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

PUBLIC_KEY_PINS_REPORT_ONLY = "Public-Key-Pins-Report-Only"
"""Public-Key-Pins-Report-Only []

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

RANGE = "Range"
"""Range []

[RFC9110, Section 14.2: HTTP Semantics]
"""

REDIRECT_REF = "Redirect-Ref"
"""Redirect-Ref []

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

REFERER = "Referer"
"""Referer []

[RFC9110, Section 10.1.3: HTTP Semantics]
"""

REFERER_ROOT = "Referer-Root"
"""Referer-Root []

[Access Control for Cross-site Requests]
"""

REFERRER_POLICY = "Referrer-Policy"
"""Referrer-Policy []

[Referrer Policy]

The header name does not share the HTTP Referer header's misspelling.
"""

REFRESH = "Refresh"
"""Refresh []

[HTML]
"""

REPEATABILITY_CLIENT_ID = "Repeatability-Client-ID"
"""Repeatability-Client-ID []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_FIRST_SENT = "Repeatability-First-Sent"
"""Repeatability-First-Sent []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_REQUEST_ID = "Repeatability-Request-ID"
"""Repeatability-Request-ID []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_RESULT = "Repeatability-Result"
"""Repeatability-Result []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPLAY_NONCE = "Replay-Nonce"
"""Replay-Nonce []

[RFC 8555, Section 6.5.1: Automatic Certificate Management Environment (ACME)]
"""

REPORTING_ENDPOINTS = "Reporting-Endpoints"
"""Reporting-Endpoints []

[Reporting API]
"""

REPR_DIGEST = "Repr-Digest"
"""Repr-Digest []

[RFC 9530, Section 3: Digest Fields]
"""

RETRY_AFTER = "Retry-After"
"""Retry-After []

[RFC9110, Section 10.2.3: HTTP Semantics]
"""

SAFE = "Safe"
"""Safe []

[RFC 2310: The Safe Response Header Field]

[Status change of HTTP experiments to Historic]
"""

SCHEDULE_REPLY = "Schedule-Reply"
"""Schedule-Reply []

[RFC 6638: Scheduling Extensions to CalDAV]
"""

SCHEDULE_TAG = "Schedule-Tag"
"""Schedule-Tag []

[RFC 6338: Scheduling Extensions to CalDAV]
"""

SEC_GPC = "Sec-GPC"
"""Sec-GPC []

[Global Privacy Control (GPC)]
"""

SEC_PURPOSE = "Sec-Purpose"
"""Sec-Purpose []

[Fetch]

Intended to replace the (not registered) Purpose and x-moz headers.
"""

SEC_TOKEN_BINDING = "Sec-Token-Binding"
"""Sec-Token-Binding []

[RFC 8473: Token Binding over HTTP]
"""

SEC_WEBSOCKET_ACCEPT = "Sec-WebSocket-Accept"
"""Sec-WebSocket-Accept []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_EXTENSIONS = "Sec-WebSocket-Extensions"
"""Sec-WebSocket-Extensions []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_KEY = "Sec-WebSocket-Key"
"""Sec-WebSocket-Key []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_PROTOCOL = "Sec-WebSocket-Protocol"
"""Sec-WebSocket-Protocol []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_VERSION = "Sec-WebSocket-Version"
"""Sec-WebSocket-Version []

[RFC 6455: The WebSocket Protocol]
"""

SECURITY_SCHEME = "Security-Scheme"
"""Security-Scheme []

[RFC 2660: The Secure HyperText Transfer Protocol]

[Status change of HTTP experiments to Historic]
"""

SERVER = "Server"
"""Server []

[RFC9110, Section 10.2.4: HTTP Semantics]
"""

SERVER_TIMING = "Server-Timing"
"""Server-Timing []

[Server Timing]
"""

SET_COOKIE = "Set-Cookie"
"""Set-Cookie []

[RFC 6265: HTTP State Management Mechanism]
"""

SET_COOKIE2 = "Set-Cookie2"
"""Set-Cookie2 []

[RFC 2965: HTTP State Management Mechanism]

Obsoleted by [RFC 6265: HTTP State Management Mechanism]
"""

SETPROFILE = "SetProfile"
"""SetProfile []

[Implementation of OPS Over HTTP]
"""

SIGNATURE = "Signature"
"""Signature []

[RFC 9421, Section 4.2: HTTP Message Signatures]
"""

SIGNATURE_INPUT = "Signature-Input"
"""Signature-Input []

[RFC 9421, Section 4.1: HTTP Message Signatures]
"""

SLUG = "SLUG"
"""SLUG []

[RFC 5023: The Atom Publishing Protocol]
"""

SOAPACTION = "SoapAction"
"""SoapAction []

[Simple Object Access Protocol (SOAP) 1.1]
"""

STATUS_URI = "Status-URI"
"""Status-URI []

[RFC 2518: HTTP Extensions for Distributed Authoring -- WEBDAV]
"""

STRICT_TRANSPORT_SECURITY = "Strict-Transport-Security"
"""Strict-Transport-Security []

[RFC 6797: HTTP Strict Transport Security (HSTS)]
"""

SUNSET = "Sunset"
"""Sunset []

[RFC 8594: The Sunset HTTP Header Field]
"""

SURROGATE_CAPABILITY = "Surrogate-Capability"
"""Surrogate-Capability []

[Edge Architecture Specification]
"""

SURROGATE_CONTROL = "Surrogate-Control"
"""Surrogate-Control []

[Edge Architecture Specification]
"""

TCN = "TCN"
"""TCN []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

TE = "TE"
"""TE []

[RFC9110, Section 10.1.4: HTTP Semantics]
"""

TIMEOUT = "Timeout"
"""Timeout []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

TIMING_ALLOW_ORIGIN = "Timing-Allow-Origin"
"""Timing-Allow-Origin []

[Resource Timing Level 1]
"""

TOPIC = "Topic"
"""Topic []

[RFC 8030, Section 5.4: Generic Event Delivery Using HTTP Push]
"""

TRACEPARENT = "Traceparent"
"""Traceparent []

[Trace Context]
"""

TRACESTATE = "Tracestate"
"""Tracestate []

[Trace Context]
"""

TRAILER = "Trailer"
"""Trailer []

[RFC9110, Section 6.6.2: HTTP Semantics]
"""

TRANSFER_ENCODING = "Transfer-Encoding"
"""Transfer-Encoding []

[RFC9112, Section 6.1: HTTP Semantics]
"""

TTL = "TTL"
"""TTL []

[RFC 8030, Section 5.2: Generic Event Delivery Using HTTP Push]
"""

UPGRADE = "Upgrade"
"""Upgrade []

[RFC9110, Section 7.8: HTTP Semantics]
"""

URGENCY = "Urgency"
"""Urgency []

[RFC 8030, Section 5.3: Generic Event Delivery Using HTTP Push]
"""

URI = "URI"
"""URI []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

USE_AS_DICTIONARY = "Use-As-Dictionary"
"""Use-As-Dictionary []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.1: Compression Dictionary Transport]
"""

USER_AGENT = "User-Agent"
"""User-Agent []

[RFC9110, Section 10.1.5: HTTP Semantics]
"""

VARIANT_VARY = "Variant-Vary"
"""Variant-Vary []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

VARY = "Vary"
"""Vary []

[RFC9110, Section 12.5.5: HTTP Semantics]
"""

VIA = "Via"
"""Via []

[RFC9110, Section 7.6.3: HTTP Semantics]
"""

WANT_CONTENT_DIGEST = "Want-Content-Digest"
"""Want-Content-Digest []

[RFC 9530, Section 4: Digest Fields]
"""

WANT_DIGEST = "Want-Digest"
"""Want-Digest []

[RFC 3230: Instance Digests in HTTP]

Obsoleted by [RFC 9530, Section 1.3: Digest Fields]
"""

WANT_REPR_DIGEST = "Want-Repr-Digest"
"""Want-Repr-Digest []

[RFC 9530, Section 4: Digest Fields]
"""

WARNING = "Warning"
"""Warning []

[RFC9111, Section 5.5: HTTP Caching]
"""

WWW_AUTHENTICATE = "WWW-Authenticate"
"""WWW-Authenticate []

[RFC9110, Section 11.6.1: HTTP Semantics]
"""

X_CONTENT_TYPE_OPTIONS = "X-Content-Type-Options"
"""X-Content-Type-Options []

[Fetch]
"""

X_FRAME_OPTIONS = "X-Frame-Options"
"""X-Frame-Options []

[HTML]
"""

STAR = "*"
"""* []

[RFC9110, Section 12.5.5: HTTP Semantics]

(reserved)
"""
