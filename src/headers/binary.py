"""HTTP Headers as bytes

see: https://www.iana.org/assignments/http-fields/http-fields.xhtml
"""

A_IM = b"A-IM"
"""A-IM []

[RFC 3229: Delta encoding in HTTP]
"""

ACCEPT = b"Accept"
"""Accept []

[RFC9110, Section 12.5.1: HTTP Semantics]
"""

ACCEPT_ADDITIONS = b"Accept-Additions"
"""Accept-Additions []

[RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)]
"""

ACCEPT_CH = b"Accept-CH"
"""Accept-CH [List]

[RFC 8942, Section 3.1: HTTP Client Hints]
"""

ACCEPT_CHARSET = b"Accept-Charset"
"""Accept-Charset []

[RFC9110, Section 12.5.2: HTTP Semantics]
"""

ACCEPT_DATETIME = b"Accept-Datetime"
"""Accept-Datetime []

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

ACCEPT_ENCODING = b"Accept-Encoding"
"""Accept-Encoding []

[RFC9110, Section 12.5.3: HTTP Semantics]
"""

ACCEPT_FEATURES = b"Accept-Features"
"""Accept-Features []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

ACCEPT_LANGUAGE = b"Accept-Language"
"""Accept-Language []

[RFC9110, Section 12.5.4: HTTP Semantics]
"""

ACCEPT_PATCH = b"Accept-Patch"
"""Accept-Patch []

[RFC 5789: PATCH Method for HTTP]
"""

ACCEPT_POST = b"Accept-Post"
"""Accept-Post []

[Linked Data Platform 1.0]
"""

ACCEPT_RANGES = b"Accept-Ranges"
"""Accept-Ranges []

[RFC9110, Section 14.3: HTTP Semantics]
"""

ACCEPT_SIGNATURE = b"Accept-Signature"
"""Accept-Signature []

[RFC 9421, Section 5.1: HTTP Message Signatures]
"""

ACCESS_CONTROL = b"Access-Control"
"""Access-Control []

[Access Control for Cross-site Requests]
"""

ACCESS_CONTROL_ALLOW_CREDENTIALS = b"Access-Control-Allow-Credentials"
"""Access-Control-Allow-Credentials []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_HEADERS = b"Access-Control-Allow-Headers"
"""Access-Control-Allow-Headers []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_METHODS = b"Access-Control-Allow-Methods"
"""Access-Control-Allow-Methods []

[Fetch]
"""

ACCESS_CONTROL_ALLOW_ORIGIN = b"Access-Control-Allow-Origin"
"""Access-Control-Allow-Origin []

[Fetch]
"""

ACCESS_CONTROL_EXPOSE_HEADERS = b"Access-Control-Expose-Headers"
"""Access-Control-Expose-Headers []

[Fetch]
"""

ACCESS_CONTROL_MAX_AGE = b"Access-Control-Max-Age"
"""Access-Control-Max-Age []

[Fetch]
"""

ACCESS_CONTROL_REQUEST_HEADERS = b"Access-Control-Request-Headers"
"""Access-Control-Request-Headers []

[Fetch]
"""

ACCESS_CONTROL_REQUEST_METHOD = b"Access-Control-Request-Method"
"""Access-Control-Request-Method []

[Fetch]
"""

AGE = b"Age"
"""Age []

[RFC9111, Section 5.1: HTTP Caching]
"""

ALLOW = b"Allow"
"""Allow []

[RFC9110, Section 10.2.1: HTTP Semantics]
"""

ALPN = b"ALPN"
"""ALPN []

[RFC 7639, Section 2: The ALPN HTTP Header Field]
"""

ALT_SVC = b"Alt-Svc"
"""Alt-Svc []

[RFC 7838: HTTP Alternative Services]
"""

ALT_USED = b"Alt-Used"
"""Alt-Used []

[RFC 7838: HTTP Alternative Services]
"""

ALTERNATES = b"Alternates"
"""Alternates []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

AMP_CACHE_TRANSFORM = b"AMP-Cache-Transform"
"""AMP-Cache-Transform []

[AMP-Cache-Transform HTTP request header]
"""

APPLY_TO_REDIRECT_REF = b"Apply-To-Redirect-Ref"
"""Apply-To-Redirect-Ref []

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

AUTHENTICATION_CONTROL = b"Authentication-Control"
"""Authentication-Control []

[RFC 8053, Section 4: HTTP Authentication Extensions for Interactive Clients]
"""

AUTHENTICATION_INFO = b"Authentication-Info"
"""Authentication-Info []

[RFC9110, Section 11.6.3: HTTP Semantics]
"""

AUTHORIZATION = b"Authorization"
"""Authorization []

[RFC9110, Section 11.6.2: HTTP Semantics]
"""

AVAILABLE_DICTIONARY = b"Available-Dictionary"
"""Available-Dictionary []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.2: Compression Dictionary Transport]
"""

C_EXT = b"C-Ext"
"""C-Ext []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_MAN = b"C-Man"
"""C-Man []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_OPT = b"C-Opt"
"""C-Opt []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

C_PEP = b"C-PEP"
"""C-PEP []

[PEP - an Extension Mechanism for HTTP]

[Status change of HTTP experiments to Historic]
"""

C_PEP_INFO = b"C-PEP-Info"
"""C-PEP-Info []

[PEP - an Extension Mechanism for HTTP]

[Status change of HTTP experiments to Historic]
"""

CACHE_CONTROL = b"Cache-Control"
"""Cache-Control []

[RFC9111, Section 5.2]
"""

CACHE_STATUS = b"Cache-Status"
"""Cache-Status [List]

[RFC9211: The Cache-Status HTTP Response Header Field]
"""

CAL_MANAGED_ID = b"Cal-Managed-ID"
"""Cal-Managed-ID []

[RFC 8607, Section 5.1: Calendaring Extensions to WebDAV (CalDAV): Managed Attachments]
"""

CALDAV_TIMEZONES = b"CalDAV-Timezones"
"""CalDAV-Timezones []

[RFC 7809, Section 7.1: Calendaring Extensions to WebDAV (CalDAV): Time Zones by Reference]
"""

CAPSULE_PROTOCOL = b"Capsule-Protocol"
"""Capsule-Protocol []

[RFC9297]
"""

CDN_CACHE_CONTROL = b"CDN-Cache-Control"
"""CDN-Cache-Control [Dictionary]

[RFC9213: Targeted HTTP Cache Control]

Cache directives targeted at content delivery networks
"""

CDN_LOOP = b"CDN-Loop"
"""CDN-Loop []

[RFC 8586: Loop Detection in Content Delivery Networks (CDNs)]
"""

CERT_NOT_AFTER = b"Cert-Not-After"
"""Cert-Not-After []

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CERT_NOT_BEFORE = b"Cert-Not-Before"
"""Cert-Not-Before []

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CLEAR_SITE_DATA = b"Clear-Site-Data"
"""Clear-Site-Data []

[Clear Site Data]
"""

CLIENT_CERT = b"Client-Cert"
"""Client-Cert [Item]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLIENT_CERT_CHAIN = b"Client-Cert-Chain"
"""Client-Cert-Chain [List]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLOSE = b"Close"
"""Close []

[RFC9112, Section 9.6: HTTP/1.1]

(reserved)
"""

CMCD_OBJECT = b"CMCD-Object"
"""CMCD-Object []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_REQUEST = b"CMCD-Request"
"""CMCD-Request []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_SESSION = b"CMCD-Session"
"""CMCD-Session []

[CTA][CTA-5004 Common Media Client Data]
"""

CMCD_STATUS = b"CMCD-Status"
"""CMCD-Status []

[CTA][CTA-5004 Common Media Client Data]
"""

CMSD_DYNAMIC = b"CMSD-Dynamic"
"""CMSD-Dynamic []

[CTA][CTA-5006 Common Media Server Data (CMSD)]
"""

CMSD_STATIC = b"CMSD-Static"
"""CMSD-Static []

[CTA][CTA-5006 Common Media Server Data (CMSD)]
"""

CONCEALED_AUTH_EXPORT = b"Concealed-Auth-Export"
"""Concealed-Auth-Export [Item]

[RFC-ietf-httpbis-unprompted-auth-12: The Concealed HTTP Authentication Scheme]
"""

CONFIGURATION_CONTEXT = b"Configuration-Context"
"""Configuration-Context []

[OSLC Configuration Management Version 1.0. Part 3: Configuration Specification]
"""

CONNECTION = b"Connection"
"""Connection []

[RFC9110, Section 7.6.1: HTTP Semantics]
"""

CONTENT_BASE = b"Content-Base"
"""Content-Base []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]

Obsoleted by [RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1]
"""

CONTENT_DIGEST = b"Content-Digest"
"""Content-Digest []

[RFC 9530, Section 2: Digest Fields]
"""

CONTENT_DISPOSITION = b"Content-Disposition"
"""Content-Disposition []

[RFC 6266: Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP)]
"""

CONTENT_ENCODING = b"Content-Encoding"
"""Content-Encoding []

[RFC9110, Section 8.4: HTTP Semantics]
"""

CONTENT_ID = b"Content-ID"
"""Content-ID []

[The HTTP Distribution and Replication Protocol]
"""

CONTENT_LANGUAGE = b"Content-Language"
"""Content-Language []

[RFC9110, Section 8.5: HTTP Semantics]
"""

CONTENT_LENGTH = b"Content-Length"
"""Content-Length []

[RFC9110, Section 8.6: HTTP Semantics]
"""

CONTENT_LOCATION = b"Content-Location"
"""Content-Location []

[RFC9110, Section 8.7: HTTP Semantics]
"""

CONTENT_MD5 = b"Content-MD5"
"""Content-MD5 []

[RFC 2616, Section 14.15: Hypertext Transfer Protocol -- HTTP/1.1]

Obsoleted by [RFC 7231, Appendix B: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content]
"""

CONTENT_RANGE = b"Content-Range"
"""Content-Range []

[RFC9110, Section 14.4: HTTP Semantics]
"""

CONTENT_SCRIPT_TYPE = b"Content-Script-Type"
"""Content-Script-Type []

[HTML 4.01 Specification]
"""

CONTENT_SECURITY_POLICY = b"Content-Security-Policy"
"""Content-Security-Policy []

[Content Security Policy Level 3]
"""

CONTENT_SECURITY_POLICY_REPORT_ONLY = b"Content-Security-Policy-Report-Only"
"""Content-Security-Policy-Report-Only []

[Content Security Policy Level 3]
"""

CONTENT_STYLE_TYPE = b"Content-Style-Type"
"""Content-Style-Type []

[HTML 4.01 Specification]
"""

CONTENT_TYPE = b"Content-Type"
"""Content-Type []

[RFC9110, Section 8.3: HTTP Semantics]
"""

CONTENT_VERSION = b"Content-Version"
"""Content-Version []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

COOKIE = b"Cookie"
"""Cookie []

[RFC 6265: HTTP State Management Mechanism]
"""

COOKIE2 = b"Cookie2"
"""Cookie2 []

[RFC 2965: HTTP State Management Mechanism]

Obsoleted by [RFC 6265: HTTP State Management Mechanism]
"""

CROSS_ORIGIN_EMBEDDER_POLICY = b"Cross-Origin-Embedder-Policy"
"""Cross-Origin-Embedder-Policy [Item]

[HTML]
"""

CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY = b"Cross-Origin-Embedder-Policy-Report-Only"
"""Cross-Origin-Embedder-Policy-Report-Only [Item]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY = b"Cross-Origin-Opener-Policy"
"""Cross-Origin-Opener-Policy [Item]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY_REPORT_ONLY = b"Cross-Origin-Opener-Policy-Report-Only"
"""Cross-Origin-Opener-Policy-Report-Only [Item]

[HTML]
"""

CROSS_ORIGIN_RESOURCE_POLICY = b"Cross-Origin-Resource-Policy"
"""Cross-Origin-Resource-Policy []

[Fetch]
"""

CTA_COMMON_ACCESS_TOKEN = b"CTA-Common-Access-Token"
"""CTA-Common-Access-Token []

[CTA][Chris_Lemmons]
"""

DASL = b"DASL"
"""DASL []

[RFC 5323: Web Distributed Authoring and Versioning (WebDAV) SEARCH]
"""

DATE = b"Date"
"""Date []

[RFC9110, Section 6.6.1: HTTP Semantics]
"""

DAV = b"DAV"
"""DAV []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DEFAULT_STYLE = b"Default-Style"
"""Default-Style []

[HTML 4.01 Specification]
"""

DELTA_BASE = b"Delta-Base"
"""Delta-Base []

[RFC 3229: Delta encoding in HTTP]
"""

DEPRECATION = b"Deprecation"
"""Deprecation [Item]

[RFC-ietf-httpapi-deprecation-header-09, Section 2: The Deprecation HTTP Response Header Field]
"""

DEPTH = b"Depth"
"""Depth []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DERIVED_FROM = b"Derived-From"
"""Derived-From []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

DESTINATION = b"Destination"
"""Destination []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DIFFERENTIAL_ID = b"Differential-ID"
"""Differential-ID []

[The HTTP Distribution and Replication Protocol]
"""

DICTIONARY_ID = b"Dictionary-ID"
"""Dictionary-ID []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.3: Compression Dictionary Transport]
"""

DIGEST = b"Digest"
"""Digest []

[RFC 3230: Instance Digests in HTTP]

Obsoleted by [RFC 9530, Section 1.3: Digest Fields]
"""

DPOP = b"DPoP"
"""DPoP []

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

DPOP_NONCE = b"DPoP-Nonce"
"""DPoP-Nonce []

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

EARLY_DATA = b"Early-Data"
"""Early-Data []

[RFC 8470: Using Early Data in HTTP]
"""

EDIINT_FEATURES = b"EDIINT-Features"
"""EDIINT-Features []

[RFC 6017: Electronic Data Interchange - Internet Integration (EDIINT) Features Header Field]
"""

ETAG = b"ETag"
"""ETag []

[RFC9110, Section 8.8.3: HTTP Semantics]
"""

EXPECT = b"Expect"
"""Expect []

[RFC9110, Section 10.1.1: HTTP Semantics]
"""

EXPECT_CT = b"Expect-CT"
"""Expect-CT []

[RFC9163: Expect-CT Extension for HTTP]

Obsoleted by [IESG]        [HTTPBIS]
"""

EXPIRES = b"Expires"
"""Expires []

[RFC9111, Section 5.3: HTTP Caching]
"""

EXT = b"Ext"
"""Ext []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

FORWARDED = b"Forwarded"
"""Forwarded []

[RFC 7239: Forwarded HTTP Extension]
"""

FROM = b"From"
"""From []

[RFC9110, Section 10.1.2: HTTP Semantics]
"""

GETPROFILE = b"GetProfile"
"""GetProfile []

[Implementation of OPS Over HTTP]
"""

HOBAREG = b"Hobareg"
"""Hobareg []

[RFC 7486, Section 6.1.1: HTTP Origin-Bound Authentication (HOBA)]
"""

HOST = b"Host"
"""Host []

[RFC9110, Section 7.2: HTTP Semantics]
"""

HTTP2_SETTINGS = b"HTTP2-Settings"
"""HTTP2-Settings []

[RFC 7540, Section 3.2.1: Hypertext Transfer Protocol Version 2 (HTTP/2)]

Obsolete; see Section 11.1 of [RFC9113]
"""

IF = b"If"
"""If []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

IF_MATCH = b"If-Match"
"""If-Match []

[RFC9110, Section 13.1.1: HTTP Semantics]
"""

IF_MODIFIED_SINCE = b"If-Modified-Since"
"""If-Modified-Since []

[RFC9110, Section 13.1.3: HTTP Semantics]
"""

IF_NONE_MATCH = b"If-None-Match"
"""If-None-Match []

[RFC9110, Section 13.1.2: HTTP Semantics]
"""

IF_RANGE = b"If-Range"
"""If-Range []

[RFC9110, Section 13.1.5: HTTP Semantics]
"""

IF_SCHEDULE_TAG_MATCH = b"If-Schedule-Tag-Match"
"""If-Schedule-Tag-Match []

[ RFC 6338: Scheduling Extensions to CalDAV]
"""

IF_UNMODIFIED_SINCE = b"If-Unmodified-Since"
"""If-Unmodified-Since []

[RFC9110, Section 13.1.4: HTTP Semantics]
"""

IM = b"IM"
"""IM []

[RFC 3229: Delta encoding in HTTP]
"""

INCLUDE_REFERRED_TOKEN_BINDING_ID = b"Include-Referred-Token-Binding-ID"
"""Include-Referred-Token-Binding-ID []

[RFC 8473: Token Binding over HTTP]
"""

ISOLATION = b"Isolation"
"""Isolation []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

KEEP_ALIVE = b"Keep-Alive"
"""Keep-Alive []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

LABEL = b"Label"
"""Label []

[RFC 3253: Versioning Extensions to WebDAV: (Web Distributed Authoring and Versioning)]
"""

LAST_EVENT_ID = b"Last-Event-ID"
"""Last-Event-ID []

[HTML]
"""

LAST_MODIFIED = b"Last-Modified"
"""Last-Modified []

[RFC9110, Section 8.8.2: HTTP Semantics]
"""

LINK = b"Link"
"""Link []

[RFC 8288: Web Linking]
"""

LINK_TEMPLATE = b"Link-Template"
"""Link-Template []

[RFC 9652: The Link-Template HTTP Header Field]
"""

LOCATION = b"Location"
"""Location []

[RFC9110, Section 10.2.2: HTTP Semantics]
"""

LOCK_TOKEN = b"Lock-Token"
"""Lock-Token []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

MAN = b"Man"
"""Man []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

MAX_FORWARDS = b"Max-Forwards"
"""Max-Forwards []

[RFC9110, Section 7.6.2: HTTP Semantics]
"""

MEMENTO_DATETIME = b"Memento-Datetime"
"""Memento-Datetime []

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

METER = b"Meter"
"""Meter []

[RFC 2227: Simple Hit-Metering and Usage-Limiting for HTTP]
"""

METHOD_CHECK = b"Method-Check"
"""Method-Check []

[Access Control for Cross-site Requests]
"""

METHOD_CHECK_EXPIRES = b"Method-Check-Expires"
"""Method-Check-Expires []

[Access Control for Cross-site Requests]
"""

MIME_VERSION = b"MIME-Version"
"""MIME-Version []

[RFC9112, Appendix B.1: HTTP/1.1]
"""

NEGOTIATE = b"Negotiate"
"""Negotiate []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

NEL = b"NEL"
"""NEL []

[Network Error Logging]
"""

ODATA_ENTITYID = b"OData-EntityId"
"""OData-EntityId []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_ISOLATION = b"OData-Isolation"
"""OData-Isolation []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_MAXVERSION = b"OData-MaxVersion"
"""OData-MaxVersion []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_VERSION = b"OData-Version"
"""OData-Version []

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

OPT = b"Opt"
"""Opt []

[RFC 2774: An HTTP Extension Framework]

[Status change of HTTP experiments to Historic]
"""

OPTIONAL_WWW_AUTHENTICATE = b"Optional-WWW-Authenticate"
"""Optional-WWW-Authenticate []

[RFC 8053, Section 3: HTTP Authentication Extensions for Interactive Clients]
"""

ORDERING_TYPE = b"Ordering-Type"
"""Ordering-Type []

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

ORIGIN = b"Origin"
"""Origin []

[RFC 6454: The Web Origin Concept]
"""

ORIGIN_AGENT_CLUSTER = b"Origin-Agent-Cluster"
"""Origin-Agent-Cluster [Item]

[HTML]
"""

OSCORE = b"OSCORE"
"""OSCORE []

[RFC 8613, Section 11.1: Object Security for Constrained RESTful Environments (OSCORE)]
"""

OSLC_CORE_VERSION = b"OSLC-Core-Version"
"""OSLC-Core-Version []

[OASIS Project Specification 01][OASIS][Chet_Ensign]
"""

OVERWRITE = b"Overwrite"
"""Overwrite []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

P3P = b"P3P"
"""P3P []

[The Platform for Privacy Preferences 1.0 (P3P1.0) Specification]
"""

PEP = b"PEP"
"""PEP []

[PEP - an Extension Mechanism for HTTP]
"""

PEP_INFO = b"PEP-Info"
"""PEP-Info []

[PEP - an Extension Mechanism for HTTP]
"""

PERMISSIONS_POLICY = b"Permissions-Policy"
"""Permissions-Policy []

[Permissions Policy]
"""

PICS_LABEL = b"PICS-Label"
"""PICS-Label []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PING_FROM = b"Ping-From"
"""Ping-From []

[HTML]
"""

PING_TO = b"Ping-To"
"""Ping-To []

[HTML]
"""

POSITION = b"Position"
"""Position []

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

PRAGMA = b"Pragma"
"""Pragma []

[RFC9111, Section 5.4: HTTP Caching]
"""

PREFER = b"Prefer"
"""Prefer []

[RFC 7240: Prefer Header for HTTP]
"""

PREFERENCE_APPLIED = b"Preference-Applied"
"""Preference-Applied []

[RFC 7240: Prefer Header for HTTP]
"""

PRIORITY = b"Priority"
"""Priority [Dictionary]

[RFC9218: Extensible Prioritization Scheme for HTTP]
"""

PROFILEOBJECT = b"ProfileObject"
"""ProfileObject []

[Implementation of OPS Over HTTP]
"""

PROTOCOL = b"Protocol"
"""Protocol []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROTOCOL_INFO = b"Protocol-Info"
"""Protocol-Info []

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_QUERY = b"Protocol-Query"
"""Protocol-Query []

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_REQUEST = b"Protocol-Request"
"""Protocol-Request []

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROXY_AUTHENTICATE = b"Proxy-Authenticate"
"""Proxy-Authenticate []

[RFC9110, Section 11.7.1: HTTP Semantics]
"""

PROXY_AUTHENTICATION_INFO = b"Proxy-Authentication-Info"
"""Proxy-Authentication-Info []

[RFC9110, Section 11.7.3: HTTP Semantics]
"""

PROXY_AUTHORIZATION = b"Proxy-Authorization"
"""Proxy-Authorization []

[RFC9110, Section 11.7.2: HTTP Semantics]
"""

PROXY_FEATURES = b"Proxy-Features"
"""Proxy-Features []

[Notification for Proxy Caches]
"""

PROXY_INSTRUCTION = b"Proxy-Instruction"
"""Proxy-Instruction []

[Notification for Proxy Caches]
"""

PROXY_STATUS = b"Proxy-Status"
"""Proxy-Status [List]

[RFC9209: The Proxy-Status HTTP Response Header Field]
"""

PUBLIC = b"Public"
"""Public []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

PUBLIC_KEY_PINS = b"Public-Key-Pins"
"""Public-Key-Pins []

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

PUBLIC_KEY_PINS_REPORT_ONLY = b"Public-Key-Pins-Report-Only"
"""Public-Key-Pins-Report-Only []

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

RANGE = b"Range"
"""Range []

[RFC9110, Section 14.2: HTTP Semantics]
"""

REDIRECT_REF = b"Redirect-Ref"
"""Redirect-Ref []

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

REFERER = b"Referer"
"""Referer []

[RFC9110, Section 10.1.3: HTTP Semantics]
"""

REFERER_ROOT = b"Referer-Root"
"""Referer-Root []

[Access Control for Cross-site Requests]
"""

REFERRER_POLICY = b"Referrer-Policy"
"""Referrer-Policy []

[Referrer Policy]

The header name does not share the HTTP Referer header's misspelling.
"""

REFRESH = b"Refresh"
"""Refresh []

[HTML]
"""

REPEATABILITY_CLIENT_ID = b"Repeatability-Client-ID"
"""Repeatability-Client-ID []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_FIRST_SENT = b"Repeatability-First-Sent"
"""Repeatability-First-Sent []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_REQUEST_ID = b"Repeatability-Request-ID"
"""Repeatability-Request-ID []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_RESULT = b"Repeatability-Result"
"""Repeatability-Result []

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPLAY_NONCE = b"Replay-Nonce"
"""Replay-Nonce []

[RFC 8555, Section 6.5.1: Automatic Certificate Management Environment (ACME)]
"""

REPORTING_ENDPOINTS = b"Reporting-Endpoints"
"""Reporting-Endpoints []

[Reporting API]
"""

REPR_DIGEST = b"Repr-Digest"
"""Repr-Digest []

[RFC 9530, Section 3: Digest Fields]
"""

RETRY_AFTER = b"Retry-After"
"""Retry-After []

[RFC9110, Section 10.2.3: HTTP Semantics]
"""

SAFE = b"Safe"
"""Safe []

[RFC 2310: The Safe Response Header Field]

[Status change of HTTP experiments to Historic]
"""

SCHEDULE_REPLY = b"Schedule-Reply"
"""Schedule-Reply []

[RFC 6638: Scheduling Extensions to CalDAV]
"""

SCHEDULE_TAG = b"Schedule-Tag"
"""Schedule-Tag []

[RFC 6338: Scheduling Extensions to CalDAV]
"""

SEC_GPC = b"Sec-GPC"
"""Sec-GPC []

[Global Privacy Control (GPC)]
"""

SEC_PURPOSE = b"Sec-Purpose"
"""Sec-Purpose []

[Fetch]

Intended to replace the (not registered) Purpose and x-moz headers.
"""

SEC_TOKEN_BINDING = b"Sec-Token-Binding"
"""Sec-Token-Binding []

[RFC 8473: Token Binding over HTTP]
"""

SEC_WEBSOCKET_ACCEPT = b"Sec-WebSocket-Accept"
"""Sec-WebSocket-Accept []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_EXTENSIONS = b"Sec-WebSocket-Extensions"
"""Sec-WebSocket-Extensions []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_KEY = b"Sec-WebSocket-Key"
"""Sec-WebSocket-Key []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_PROTOCOL = b"Sec-WebSocket-Protocol"
"""Sec-WebSocket-Protocol []

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_VERSION = b"Sec-WebSocket-Version"
"""Sec-WebSocket-Version []

[RFC 6455: The WebSocket Protocol]
"""

SECURITY_SCHEME = b"Security-Scheme"
"""Security-Scheme []

[RFC 2660: The Secure HyperText Transfer Protocol]

[Status change of HTTP experiments to Historic]
"""

SERVER = b"Server"
"""Server []

[RFC9110, Section 10.2.4: HTTP Semantics]
"""

SERVER_TIMING = b"Server-Timing"
"""Server-Timing []

[Server Timing]
"""

SET_COOKIE = b"Set-Cookie"
"""Set-Cookie []

[RFC 6265: HTTP State Management Mechanism]
"""

SET_COOKIE2 = b"Set-Cookie2"
"""Set-Cookie2 []

[RFC 2965: HTTP State Management Mechanism]

Obsoleted by [RFC 6265: HTTP State Management Mechanism]
"""

SETPROFILE = b"SetProfile"
"""SetProfile []

[Implementation of OPS Over HTTP]
"""

SIGNATURE = b"Signature"
"""Signature []

[RFC 9421, Section 4.2: HTTP Message Signatures]
"""

SIGNATURE_INPUT = b"Signature-Input"
"""Signature-Input []

[RFC 9421, Section 4.1: HTTP Message Signatures]
"""

SLUG = b"SLUG"
"""SLUG []

[RFC 5023: The Atom Publishing Protocol]
"""

SOAPACTION = b"SoapAction"
"""SoapAction []

[Simple Object Access Protocol (SOAP) 1.1]
"""

STATUS_URI = b"Status-URI"
"""Status-URI []

[RFC 2518: HTTP Extensions for Distributed Authoring -- WEBDAV]
"""

STRICT_TRANSPORT_SECURITY = b"Strict-Transport-Security"
"""Strict-Transport-Security []

[RFC 6797: HTTP Strict Transport Security (HSTS)]
"""

SUNSET = b"Sunset"
"""Sunset []

[RFC 8594: The Sunset HTTP Header Field]
"""

SURROGATE_CAPABILITY = b"Surrogate-Capability"
"""Surrogate-Capability []

[Edge Architecture Specification]
"""

SURROGATE_CONTROL = b"Surrogate-Control"
"""Surrogate-Control []

[Edge Architecture Specification]
"""

TCN = b"TCN"
"""TCN []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

TE = b"TE"
"""TE []

[RFC9110, Section 10.1.4: HTTP Semantics]
"""

TIMEOUT = b"Timeout"
"""Timeout []

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

TIMING_ALLOW_ORIGIN = b"Timing-Allow-Origin"
"""Timing-Allow-Origin []

[Resource Timing Level 1]
"""

TOPIC = b"Topic"
"""Topic []

[RFC 8030, Section 5.4: Generic Event Delivery Using HTTP Push]
"""

TRACEPARENT = b"Traceparent"
"""Traceparent []

[Trace Context]
"""

TRACESTATE = b"Tracestate"
"""Tracestate []

[Trace Context]
"""

TRAILER = b"Trailer"
"""Trailer []

[RFC9110, Section 6.6.2: HTTP Semantics]
"""

TRANSFER_ENCODING = b"Transfer-Encoding"
"""Transfer-Encoding []

[RFC9112, Section 6.1: HTTP Semantics]
"""

TTL = b"TTL"
"""TTL []

[RFC 8030, Section 5.2: Generic Event Delivery Using HTTP Push]
"""

UPGRADE = b"Upgrade"
"""Upgrade []

[RFC9110, Section 7.8: HTTP Semantics]
"""

URGENCY = b"Urgency"
"""Urgency []

[RFC 8030, Section 5.3: Generic Event Delivery Using HTTP Push]
"""

URI = b"URI"
"""URI []

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

USE_AS_DICTIONARY = b"Use-As-Dictionary"
"""Use-As-Dictionary []

[RFC-ietf-httpbis-compression-dictionary-19, Section 2.1: Compression Dictionary Transport]
"""

USER_AGENT = b"User-Agent"
"""User-Agent []

[RFC9110, Section 10.1.5: HTTP Semantics]
"""

VARIANT_VARY = b"Variant-Vary"
"""Variant-Vary []

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

VARY = b"Vary"
"""Vary []

[RFC9110, Section 12.5.5: HTTP Semantics]
"""

VIA = b"Via"
"""Via []

[RFC9110, Section 7.6.3: HTTP Semantics]
"""

WANT_CONTENT_DIGEST = b"Want-Content-Digest"
"""Want-Content-Digest []

[RFC 9530, Section 4: Digest Fields]
"""

WANT_DIGEST = b"Want-Digest"
"""Want-Digest []

[RFC 3230: Instance Digests in HTTP]

Obsoleted by [RFC 9530, Section 1.3: Digest Fields]
"""

WANT_REPR_DIGEST = b"Want-Repr-Digest"
"""Want-Repr-Digest []

[RFC 9530, Section 4: Digest Fields]
"""

WARNING = b"Warning"
"""Warning []

[RFC9111, Section 5.5: HTTP Caching]
"""

WWW_AUTHENTICATE = b"WWW-Authenticate"
"""WWW-Authenticate []

[RFC9110, Section 11.6.1: HTTP Semantics]
"""

X_CONTENT_TYPE_OPTIONS = b"X-Content-Type-Options"
"""X-Content-Type-Options []

[Fetch]
"""

X_FRAME_OPTIONS = b"X-Frame-Options"
"""X-Frame-Options []

[HTML]
"""

STAR = b"*"
"""* []

[RFC9110, Section 12.5.5: HTTP Semantics]

(reserved)
"""
