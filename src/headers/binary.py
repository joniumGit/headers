"""HTTP Headers as bytes

see: https://www.iana.org/assignments/http-fields/http-fields.xhtml
"""

A_IM = b"A-IM"
"""A-IM [permanent]

[RFC 3229: Delta encoding in HTTP]
"""

ACCEPT = b"Accept"
"""Accept [permanent]

[RFC9110, Section 12.5.1: HTTP Semantics]
"""

ACCEPT_ADDITIONS = b"Accept-Additions"
"""Accept-Additions [permanent]

[RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)]
"""

ACCEPT_CH = b"Accept-CH"
"""Accept-CH [permanent]

[RFC 8942, Section 3.1: HTTP Client Hints]
"""

ACCEPT_CHARSET = b"Accept-Charset"
"""Accept-Charset [deprecated]

[RFC9110, Section 12.5.2: HTTP Semantics]
"""

ACCEPT_DATETIME = b"Accept-Datetime"
"""Accept-Datetime [permanent]

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

ACCEPT_ENCODING = b"Accept-Encoding"
"""Accept-Encoding [permanent]

[RFC9110, Section 12.5.3: HTTP Semantics]
"""

ACCEPT_FEATURES = b"Accept-Features"
"""Accept-Features [permanent]

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

ACCEPT_LANGUAGE = b"Accept-Language"
"""Accept-Language [permanent]

[RFC9110, Section 12.5.4: HTTP Semantics]
"""

ACCEPT_PATCH = b"Accept-Patch"
"""Accept-Patch [permanent]

[RFC 5789: PATCH Method for HTTP]
"""

ACCEPT_POST = b"Accept-Post"
"""Accept-Post [permanent]

[Linked Data Platform 1.0]
"""

ACCEPT_RANGES = b"Accept-Ranges"
"""Accept-Ranges [permanent]

[RFC9110, Section 14.3: HTTP Semantics]
"""

ACCEPT_SIGNATURE = b"Accept-Signature"
"""Accept-Signature [permanent]

[RFC-ietf-httpbis-message-signatures-19, Section 5.1: HTTP Message Signatures]
"""

ACCESS_CONTROL = b"Access-Control"
"""Access-Control [obsoleted]

[Access Control for Cross-site Requests]
"""

ACCESS_CONTROL_ALLOW_CREDENTIALS = b"Access-Control-Allow-Credentials"
"""Access-Control-Allow-Credentials [permanent]

[Fetch]
"""

ACCESS_CONTROL_ALLOW_HEADERS = b"Access-Control-Allow-Headers"
"""Access-Control-Allow-Headers [permanent]

[Fetch]
"""

ACCESS_CONTROL_ALLOW_METHODS = b"Access-Control-Allow-Methods"
"""Access-Control-Allow-Methods [permanent]

[Fetch]
"""

ACCESS_CONTROL_ALLOW_ORIGIN = b"Access-Control-Allow-Origin"
"""Access-Control-Allow-Origin [permanent]

[Fetch]
"""

ACCESS_CONTROL_EXPOSE_HEADERS = b"Access-Control-Expose-Headers"
"""Access-Control-Expose-Headers [permanent]

[Fetch]
"""

ACCESS_CONTROL_MAX_AGE = b"Access-Control-Max-Age"
"""Access-Control-Max-Age [permanent]

[Fetch]
"""

ACCESS_CONTROL_REQUEST_HEADERS = b"Access-Control-Request-Headers"
"""Access-Control-Request-Headers [permanent]

[Fetch]
"""

ACCESS_CONTROL_REQUEST_METHOD = b"Access-Control-Request-Method"
"""Access-Control-Request-Method [permanent]

[Fetch]
"""

AGE = b"Age"
"""Age [permanent]

[RFC9111, Section 5.1: HTTP Caching]
"""

ALLOW = b"Allow"
"""Allow [permanent]

[RFC9110, Section 10.2.1: HTTP Semantics]
"""

ALPN = b"ALPN"
"""ALPN [permanent]

[RFC 7639, Section 2: The ALPN HTTP Header Field]
"""

ALT_SVC = b"Alt-Svc"
"""Alt-Svc [permanent]

[RFC 7838: HTTP Alternative Services]
"""

ALT_USED = b"Alt-Used"
"""Alt-Used [permanent]

[RFC 7838: HTTP Alternative Services]
"""

ALTERNATES = b"Alternates"
"""Alternates [permanent]

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

AMP_CACHE_TRANSFORM = b"AMP-Cache-Transform"
"""AMP-Cache-Transform [provisional]

[AMP-Cache-Transform HTTP request header]
"""

APPLY_TO_REDIRECT_REF = b"Apply-To-Redirect-Ref"
"""Apply-To-Redirect-Ref [permanent]

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

AUTHENTICATION_CONTROL = b"Authentication-Control"
"""Authentication-Control [permanent]

[RFC 8053, Section 4: HTTP Authentication Extensions for Interactive Clients]
"""

AUTHENTICATION_INFO = b"Authentication-Info"
"""Authentication-Info [permanent]

[RFC9110, Section 11.6.3: HTTP Semantics]
"""

AUTHORIZATION = b"Authorization"
"""Authorization [permanent]

[RFC9110, Section 11.6.2: HTTP Semantics]
"""

C_EXT = b"C-Ext"
"""C-Ext [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

C_MAN = b"C-Man"
"""C-Man [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

C_OPT = b"C-Opt"
"""C-Opt [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

C_PEP = b"C-PEP"
"""C-PEP [obsoleted]

[PEP - an Extension Mechanism for HTTP][status-change-http-experiments-to-historic]
"""

C_PEP_INFO = b"C-PEP-Info"
"""C-PEP-Info [deprecated]

[PEP - an Extension Mechanism for HTTP][status-change-http-experiments-to-historic]
"""

CACHE_CONTROL = b"Cache-Control"
"""Cache-Control [permanent]

[RFC9111, Section 5.2]
"""

CACHE_STATUS = b"Cache-Status"
"""Cache-Status [permanent]

[RFC9211: The Cache-Status HTTP Response Header Field]
"""

CAL_MANAGED_ID = b"Cal-Managed-ID"
"""Cal-Managed-ID [permanent]

[RFC 8607, Section 5.1: Calendaring Extensions to WebDAV (CalDAV): Managed Attachments]
"""

CALDAV_TIMEZONES = b"CalDAV-Timezones"
"""CalDAV-Timezones [permanent]

[RFC 7809, Section 7.1: Calendaring Extensions to WebDAV (CalDAV): Time Zones by Reference]
"""

CAPSULE_PROTOCOL = b"Capsule-Protocol"
"""Capsule-Protocol [permanent]

[RFC9297]
"""

CDN_CACHE_CONTROL = b"CDN-Cache-Control"
"""CDN-Cache-Control [permanent]

[RFC9213: Targeted HTTP Cache Control]

Cache directives targeted at content delivery networks
"""

CDN_LOOP = b"CDN-Loop"
"""CDN-Loop [permanent]

[RFC 8586: Loop Detection in Content Delivery Networks (CDNs)]
"""

CERT_NOT_AFTER = b"Cert-Not-After"
"""Cert-Not-After [permanent]

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CERT_NOT_BEFORE = b"Cert-Not-Before"
"""Cert-Not-Before [permanent]

[RFC 8739, Section 3.3: Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)]
"""

CLEAR_SITE_DATA = b"Clear-Site-Data"
"""Clear-Site-Data [permanent]

[Clear Site Data]
"""

CLIENT_CERT = b"Client-Cert"
"""Client-Cert [permanent]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLIENT_CERT_CHAIN = b"Client-Cert-Chain"
"""Client-Cert-Chain [permanent]

[RFC9440, Section 2: Client-Cert HTTP Header Field]
"""

CLOSE = b"Close"
"""Close [permanent]

[RFC9112, Section 9.6: HTTP/1.1]

(reserved)
"""

CONFIGURATION_CONTEXT = b"Configuration-Context"
"""Configuration-Context [provisional]

[OSLC Configuration Management Version 1.0. Part 3: Configuration Specification]
"""

CONNECTION = b"Connection"
"""Connection [permanent]

[RFC9110, Section 7.6.1: HTTP Semantics]
"""

CONTENT_BASE = b"Content-Base"
"""Content-Base [obsoleted]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1][RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1]
"""

CONTENT_DIGEST = b"Content-Digest"
"""Content-Digest [permanent]

[RFC-ietf-httpbis-digest-headers-13, Section 2: Digest Fields]
"""

CONTENT_DISPOSITION = b"Content-Disposition"
"""Content-Disposition [permanent]

[RFC 6266: Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP)]
"""

CONTENT_ENCODING = b"Content-Encoding"
"""Content-Encoding [permanent]

[RFC9110, Section 8.4: HTTP Semantics]
"""

CONTENT_ID = b"Content-ID"
"""Content-ID [permanent]

[The HTTP Distribution and Replication Protocol]
"""

CONTENT_LANGUAGE = b"Content-Language"
"""Content-Language [permanent]

[RFC9110, Section 8.5: HTTP Semantics]
"""

CONTENT_LENGTH = b"Content-Length"
"""Content-Length [permanent]

[RFC9110, Section 8.6: HTTP Semantics]
"""

CONTENT_LOCATION = b"Content-Location"
"""Content-Location [permanent]

[RFC9110, Section 8.7: HTTP Semantics]
"""

CONTENT_MD5 = b"Content-MD5"
"""Content-MD5 [obsoleted]

[RFC 2616, Section 14.15: Hypertext Transfer Protocol -- HTTP/1.1][RFC 7231, Appendix B: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content]
"""

CONTENT_RANGE = b"Content-Range"
"""Content-Range [permanent]

[RFC9110, Section 14.4: HTTP Semantics]
"""

CONTENT_SCRIPT_TYPE = b"Content-Script-Type"
"""Content-Script-Type [obsoleted]

[HTML 4.01 Specification]
"""

CONTENT_SECURITY_POLICY = b"Content-Security-Policy"
"""Content-Security-Policy [permanent]

[Content Security Policy Level 3]
"""

CONTENT_SECURITY_POLICY_REPORT_ONLY = b"Content-Security-Policy-Report-Only"
"""Content-Security-Policy-Report-Only [permanent]

[Content Security Policy Level 3]
"""

CONTENT_STYLE_TYPE = b"Content-Style-Type"
"""Content-Style-Type [obsoleted]

[HTML 4.01 Specification]
"""

CONTENT_TYPE = b"Content-Type"
"""Content-Type [permanent]

[RFC9110, Section 8.3: HTTP Semantics]
"""

CONTENT_VERSION = b"Content-Version"
"""Content-Version [obsoleted]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

COOKIE = b"Cookie"
"""Cookie [permanent]

[RFC 6265: HTTP State Management Mechanism]
"""

COOKIE2 = b"Cookie2"
"""Cookie2 [obsoleted]

[RFC 2965: HTTP State Management Mechanism][RFC 6265: HTTP State Management Mechanism]
"""

CROSS_ORIGIN_EMBEDDER_POLICY = b"Cross-Origin-Embedder-Policy"
"""Cross-Origin-Embedder-Policy [permanent]

[HTML]
"""

CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY = b"Cross-Origin-Embedder-Policy-Report-Only"
"""Cross-Origin-Embedder-Policy-Report-Only [permanent]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY = b"Cross-Origin-Opener-Policy"
"""Cross-Origin-Opener-Policy [permanent]

[HTML]
"""

CROSS_ORIGIN_OPENER_POLICY_REPORT_ONLY = b"Cross-Origin-Opener-Policy-Report-Only"
"""Cross-Origin-Opener-Policy-Report-Only [permanent]

[HTML]
"""

CROSS_ORIGIN_RESOURCE_POLICY = b"Cross-Origin-Resource-Policy"
"""Cross-Origin-Resource-Policy [permanent]

[Fetch]
"""

DASL = b"DASL"
"""DASL [permanent]

[RFC 5323: Web Distributed Authoring and Versioning (WebDAV) SEARCH]
"""

DATE = b"Date"
"""Date [permanent]

[RFC9110, Section 6.6.1: HTTP Semantics]
"""

DAV = b"DAV"
"""DAV [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DEFAULT_STYLE = b"Default-Style"
"""Default-Style [obsoleted]

[HTML 4.01 Specification]
"""

DELTA_BASE = b"Delta-Base"
"""Delta-Base [permanent]

[RFC 3229: Delta encoding in HTTP]
"""

DEPTH = b"Depth"
"""Depth [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DERIVED_FROM = b"Derived-From"
"""Derived-From [obsoleted]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

DESTINATION = b"Destination"
"""Destination [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

DIFFERENTIAL_ID = b"Differential-ID"
"""Differential-ID [permanent]

[The HTTP Distribution and Replication Protocol]
"""

DIGEST = b"Digest"
"""Digest [obsoleted]

[RFC 3230: Instance Digests in HTTP][RFC-ietf-httpbis-digest-headers-13, Section 1.3: Digest Fields]
"""

DPOP = b"DPoP"
"""DPoP [permanent]

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

DPOP_NONCE = b"DPoP-Nonce"
"""DPoP-Nonce [permanent]

[RFC9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)]
"""

EARLY_DATA = b"Early-Data"
"""Early-Data [permanent]

[RFC 8470: Using Early Data in HTTP]
"""

EDIINT_FEATURES = b"EDIINT-Features"
"""EDIINT-Features [provisional]

[RFC 6017: Electronic Data Interchange - Internet Integration (EDIINT) Features Header Field]
"""

ETAG = b"ETag"
"""ETag [permanent]

[RFC9110, Section 8.8.3: HTTP Semantics]
"""

EXPECT = b"Expect"
"""Expect [permanent]

[RFC9110, Section 10.1.1: HTTP Semantics]
"""

EXPECT_CT = b"Expect-CT"
"""Expect-CT [permanent]

[RFC9163: Expect-CT Extension for HTTP]
"""

EXPIRES = b"Expires"
"""Expires [permanent]

[RFC9111, Section 5.3: HTTP Caching]
"""

EXT = b"Ext"
"""Ext [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

FORWARDED = b"Forwarded"
"""Forwarded [permanent]

[RFC 7239: Forwarded HTTP Extension]
"""

FROM = b"From"
"""From [permanent]

[RFC9110, Section 10.1.2: HTTP Semantics]
"""

GETPROFILE = b"GetProfile"
"""GetProfile [obsoleted]

[Implementation of OPS Over HTTP]
"""

HOBAREG = b"Hobareg"
"""Hobareg [permanent]

[RFC 7486, Section 6.1.1: HTTP Origin-Bound Authentication (HOBA)]
"""

HOST = b"Host"
"""Host [permanent]

[RFC9110, Section 7.2: HTTP Semantics]
"""

HTTP2_SETTINGS = b"HTTP2-Settings"
"""HTTP2-Settings [obsoleted]

[RFC 7540, Section 3.2.1: Hypertext Transfer Protocol Version 2 (HTTP/2)]

Obsolete; see Section 11.1 of [RFC9113]
"""

IF = b"If"
"""If [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

IF_MATCH = b"If-Match"
"""If-Match [permanent]

[RFC9110, Section 13.1.1: HTTP Semantics]
"""

IF_MODIFIED_SINCE = b"If-Modified-Since"
"""If-Modified-Since [permanent]

[RFC9110, Section 13.1.3: HTTP Semantics]
"""

IF_NONE_MATCH = b"If-None-Match"
"""If-None-Match [permanent]

[RFC9110, Section 13.1.2: HTTP Semantics]
"""

IF_RANGE = b"If-Range"
"""If-Range [permanent]

[RFC9110, Section 13.1.5: HTTP Semantics]
"""

IF_SCHEDULE_TAG_MATCH = b"If-Schedule-Tag-Match"
"""If-Schedule-Tag-Match [permanent]

[ RFC 6338: Scheduling Extensions to CalDAV]
"""

IF_UNMODIFIED_SINCE = b"If-Unmodified-Since"
"""If-Unmodified-Since [permanent]

[RFC9110, Section 13.1.4: HTTP Semantics]
"""

IM = b"IM"
"""IM [permanent]

[RFC 3229: Delta encoding in HTTP]
"""

INCLUDE_REFERRED_TOKEN_BINDING_ID = b"Include-Referred-Token-Binding-ID"
"""Include-Referred-Token-Binding-ID [permanent]

[RFC 8473: Token Binding over HTTP]
"""

ISOLATION = b"Isolation"
"""Isolation [provisional]

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

KEEP_ALIVE = b"Keep-Alive"
"""Keep-Alive [permanent]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

LABEL = b"Label"
"""Label [permanent]

[RFC 3253: Versioning Extensions to WebDAV: (Web Distributed Authoring and Versioning)]
"""

LAST_EVENT_ID = b"Last-Event-ID"
"""Last-Event-ID [permanent]

[HTML]
"""

LAST_MODIFIED = b"Last-Modified"
"""Last-Modified [permanent]

[RFC9110, Section 8.8.2: HTTP Semantics]
"""

LINK = b"Link"
"""Link [permanent]

[RFC 8288: Web Linking]
"""

LOCATION = b"Location"
"""Location [permanent]

[RFC9110, Section 10.2.2: HTTP Semantics]
"""

LOCK_TOKEN = b"Lock-Token"
"""Lock-Token [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

MAN = b"Man"
"""Man [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

MAX_FORWARDS = b"Max-Forwards"
"""Max-Forwards [permanent]

[RFC9110, Section 7.6.2: HTTP Semantics]
"""

MEMENTO_DATETIME = b"Memento-Datetime"
"""Memento-Datetime [permanent]

[RFC 7089: HTTP Framework for Time-Based Access to Resource States -- Memento]
"""

METER = b"Meter"
"""Meter [permanent]

[RFC 2227: Simple Hit-Metering and Usage-Limiting for HTTP]
"""

METHOD_CHECK = b"Method-Check"
"""Method-Check [obsoleted]

[Access Control for Cross-site Requests]
"""

METHOD_CHECK_EXPIRES = b"Method-Check-Expires"
"""Method-Check-Expires [obsoleted]

[Access Control for Cross-site Requests]
"""

MIME_VERSION = b"MIME-Version"
"""MIME-Version [permanent]

[RFC9112, Appendix B.1: HTTP/1.1]
"""

NEGOTIATE = b"Negotiate"
"""Negotiate [permanent]

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

ODATA_ENTITYID = b"OData-EntityId"
"""OData-EntityId [permanent]

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_ISOLATION = b"OData-Isolation"
"""OData-Isolation [permanent]

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_MAXVERSION = b"OData-MaxVersion"
"""OData-MaxVersion [permanent]

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

ODATA_VERSION = b"OData-Version"
"""OData-Version [permanent]

[OData Version 4.01 Part 1: Protocol][OASIS][Chet_Ensign]
"""

OPT = b"Opt"
"""Opt [obsoleted]

[RFC 2774: An HTTP Extension Framework][status-change-http-experiments-to-historic]
"""

OPTIONAL_WWW_AUTHENTICATE = b"Optional-WWW-Authenticate"
"""Optional-WWW-Authenticate [permanent]

[RFC 8053, Section 3: HTTP Authentication Extensions for Interactive Clients]
"""

ORDERING_TYPE = b"Ordering-Type"
"""Ordering-Type [permanent]

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

ORIGIN = b"Origin"
"""Origin [permanent]

[RFC 6454: The Web Origin Concept]
"""

ORIGIN_AGENT_CLUSTER = b"Origin-Agent-Cluster"
"""Origin-Agent-Cluster [permanent]

[HTML]
"""

OSCORE = b"OSCORE"
"""OSCORE [permanent]

[RFC 8613, Section 11.1: Object Security for Constrained RESTful Environments (OSCORE)]
"""

OSLC_CORE_VERSION = b"OSLC-Core-Version"
"""OSLC-Core-Version [permanent]

[OASIS Project Specification 01][OASIS][Chet_Ensign]
"""

OVERWRITE = b"Overwrite"
"""Overwrite [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

P3P = b"P3P"
"""P3P [obsoleted]

[The Platform for Privacy Preferences 1.0 (P3P1.0) Specification]
"""

PEP = b"PEP"
"""PEP [obsoleted]

[PEP - an Extension Mechanism for HTTP]
"""

PEP_INFO = b"Pep-Info"
"""Pep-Info [obsoleted]

[PEP - an Extension Mechanism for HTTP]
"""

PERMISSIONS_POLICY = b"Permissions-Policy"
"""Permissions-Policy [provisional]

[Permissions Policy]
"""

PICS_LABEL = b"PICS-Label"
"""PICS-Label [obsoleted]

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PING_FROM = b"Ping-From"
"""Ping-From [permanent]

[HTML]
"""

PING_TO = b"Ping-To"
"""Ping-To [permanent]

[HTML]
"""

POSITION = b"Position"
"""Position [permanent]

[RFC 3648: Web Distributed Authoring and Versioning (WebDAV) Ordered Collections Protocol]
"""

PRAGMA = b"Pragma"
"""Pragma [deprecated]

[RFC9111, Section 5.4: HTTP Caching]
"""

PREFER = b"Prefer"
"""Prefer [permanent]

[RFC 7240: Prefer Header for HTTP]
"""

PREFERENCE_APPLIED = b"Preference-Applied"
"""Preference-Applied [permanent]

[RFC 7240: Prefer Header for HTTP]
"""

PRIORITY = b"Priority"
"""Priority [permanent]

[RFC9218: Extensible Prioritization Scheme for HTTP]
"""

PROFILEOBJECT = b"ProfileObject"
"""ProfileObject [obsoleted]

[Implementation of OPS Over HTTP]
"""

PROTOCOL = b"Protocol"
"""Protocol [obsoleted]

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROTOCOL_INFO = b"Protocol-Info"
"""Protocol-Info [deprecated]

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_QUERY = b"Protocol-Query"
"""Protocol-Query [deprecated]

[White Paper: Joint Electronic Payment Initiative]
"""

PROTOCOL_REQUEST = b"Protocol-Request"
"""Protocol-Request [obsoleted]

[PICS Label Distribution Label Syntax and Communication Protocols]
"""

PROXY_AUTHENTICATE = b"Proxy-Authenticate"
"""Proxy-Authenticate [permanent]

[RFC9110, Section 11.7.1: HTTP Semantics]
"""

PROXY_AUTHENTICATION_INFO = b"Proxy-Authentication-Info"
"""Proxy-Authentication-Info [permanent]

[RFC9110, Section 11.7.3: HTTP Semantics]
"""

PROXY_AUTHORIZATION = b"Proxy-Authorization"
"""Proxy-Authorization [permanent]

[RFC9110, Section 11.7.2: HTTP Semantics]
"""

PROXY_FEATURES = b"Proxy-Features"
"""Proxy-Features [obsoleted]

[Notification for Proxy Caches]
"""

PROXY_INSTRUCTION = b"Proxy-Instruction"
"""Proxy-Instruction [obsoleted]

[Notification for Proxy Caches]
"""

PROXY_STATUS = b"Proxy-Status"
"""Proxy-Status [permanent]

[RFC9209: The Proxy-Status HTTP Response Header Field]
"""

PUBLIC = b"Public"
"""Public [obsoleted]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

PUBLIC_KEY_PINS = b"Public-Key-Pins"
"""Public-Key-Pins [permanent]

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

PUBLIC_KEY_PINS_REPORT_ONLY = b"Public-Key-Pins-Report-Only"
"""Public-Key-Pins-Report-Only [permanent]

[RFC 7469: Public Key Pinning Extension for HTTP]
"""

RANGE = b"Range"
"""Range [permanent]

[RFC9110, Section 14.2: HTTP Semantics]
"""

REDIRECT_REF = b"Redirect-Ref"
"""Redirect-Ref [permanent]

[RFC 4437: Web Distributed Authoring and Versioning (WebDAV) Redirect Reference Resources]
"""

REFERER = b"Referer"
"""Referer [permanent]

[RFC9110, Section 10.1.3: HTTP Semantics]
"""

REFERER_ROOT = b"Referer-Root"
"""Referer-Root [obsoleted]

[Access Control for Cross-site Requests]
"""

REFRESH = b"Refresh"
"""Refresh [permanent]

[HTML]
"""

REPEATABILITY_CLIENT_ID = b"Repeatability-Client-ID"
"""Repeatability-Client-ID [provisional]

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_FIRST_SENT = b"Repeatability-First-Sent"
"""Repeatability-First-Sent [provisional]

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_REQUEST_ID = b"Repeatability-Request-ID"
"""Repeatability-Request-ID [provisional]

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPEATABILITY_RESULT = b"Repeatability-Result"
"""Repeatability-Result [provisional]

[Repeatable Requests Version 1.0][OASIS][Chet_Ensign]
"""

REPLAY_NONCE = b"Replay-Nonce"
"""Replay-Nonce [permanent]

[RFC 8555, Section 6.5.1: Automatic Certificate Management Environment (ACME)]
"""

REPORTING_ENDPOINTS = b"Reporting-Endpoints"
"""Reporting-Endpoints [provisional]

[Reporting API]
"""

REPR_DIGEST = b"Repr-Digest"
"""Repr-Digest [permanent]

[RFC-ietf-httpbis-digest-headers-13, Section 3: Digest Fields]
"""

RETRY_AFTER = b"Retry-After"
"""Retry-After [permanent]

[RFC9110, Section 10.2.3: HTTP Semantics]
"""

SAFE = b"Safe"
"""Safe [obsoleted]

[RFC 2310: The Safe Response Header Field][status-change-http-experiments-to-historic]
"""

SCHEDULE_REPLY = b"Schedule-Reply"
"""Schedule-Reply [permanent]

[RFC 6638: Scheduling Extensions to CalDAV]
"""

SCHEDULE_TAG = b"Schedule-Tag"
"""Schedule-Tag [permanent]

[RFC 6338: Scheduling Extensions to CalDAV]
"""

SEC_GPC = b"Sec-GPC"
"""Sec-GPC [provisional]

[Global Privacy Control (GPC)]
"""

SEC_PURPOSE = b"Sec-Purpose"
"""Sec-Purpose [permanent]

[Fetch]

Intended to replace the (not registered) Purpose and x-moz headers.
"""

SEC_TOKEN_BINDING = b"Sec-Token-Binding"
"""Sec-Token-Binding [permanent]

[RFC 8473: Token Binding over HTTP]
"""

SEC_WEBSOCKET_ACCEPT = b"Sec-WebSocket-Accept"
"""Sec-WebSocket-Accept [permanent]

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_EXTENSIONS = b"Sec-WebSocket-Extensions"
"""Sec-WebSocket-Extensions [permanent]

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_KEY = b"Sec-WebSocket-Key"
"""Sec-WebSocket-Key [permanent]

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_PROTOCOL = b"Sec-WebSocket-Protocol"
"""Sec-WebSocket-Protocol [permanent]

[RFC 6455: The WebSocket Protocol]
"""

SEC_WEBSOCKET_VERSION = b"Sec-WebSocket-Version"
"""Sec-WebSocket-Version [permanent]

[RFC 6455: The WebSocket Protocol]
"""

SECURITY_SCHEME = b"Security-Scheme"
"""Security-Scheme [obsoleted]

[RFC 2660: The Secure HyperText Transfer Protocol][status-change-http-experiments-to-historic]
"""

SERVER = b"Server"
"""Server [permanent]

[RFC9110, Section 10.2.4: HTTP Semantics]
"""

SERVER_TIMING = b"Server-Timing"
"""Server-Timing [permanent]

[Server Timing]
"""

SET_COOKIE = b"Set-Cookie"
"""Set-Cookie [permanent]

[RFC 6265: HTTP State Management Mechanism]
"""

SET_COOKIE2 = b"Set-Cookie2"
"""Set-Cookie2 [obsoleted]

[RFC 2965: HTTP State Management Mechanism][RFC 6265: HTTP State Management Mechanism]
"""

SETPROFILE = b"SetProfile"
"""SetProfile [obsoleted]

[Implementation of OPS Over HTTP]
"""

SIGNATURE = b"Signature"
"""Signature [permanent]

[RFC-ietf-httpbis-message-signatures-19, Section 4.2: HTTP Message Signatures]
"""

SIGNATURE_INPUT = b"Signature-Input"
"""Signature-Input [permanent]

[RFC-ietf-httpbis-message-signatures-19, Section 4.1: HTTP Message Signatures]
"""

SLUG = b"SLUG"
"""SLUG [permanent]

[RFC 5023: The Atom Publishing Protocol]
"""

SOAPACTION = b"SoapAction"
"""SoapAction [permanent]

[Simple Object Access Protocol (SOAP) 1.1]
"""

STATUS_URI = b"Status-URI"
"""Status-URI [permanent]

[RFC 2518: HTTP Extensions for Distributed Authoring -- WEBDAV]
"""

STRICT_TRANSPORT_SECURITY = b"Strict-Transport-Security"
"""Strict-Transport-Security [permanent]

[RFC 6797: HTTP Strict Transport Security (HSTS)]
"""

SUNSET = b"Sunset"
"""Sunset [permanent]

[RFC 8594: The Sunset HTTP Header Field]
"""

SURROGATE_CAPABILITY = b"Surrogate-Capability"
"""Surrogate-Capability [permanent]

[Edge Architecture Specification]
"""

SURROGATE_CONTROL = b"Surrogate-Control"
"""Surrogate-Control [permanent]

[Edge Architecture Specification]
"""

TCN = b"TCN"
"""TCN [permanent]

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

TE = b"TE"
"""TE [permanent]

[RFC9110, Section 10.1.4: HTTP Semantics]
"""

TIMEOUT = b"Timeout"
"""Timeout [permanent]

[RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)]
"""

TIMING_ALLOW_ORIGIN = b"Timing-Allow-Origin"
"""Timing-Allow-Origin [provisional]

[Resource Timing Level 1]
"""

TOPIC = b"Topic"
"""Topic [permanent]

[RFC 8030, Section 5.4: Generic Event Delivery Using HTTP Push]
"""

TRACEPARENT = b"Traceparent"
"""Traceparent [permanent]

[Trace Context]
"""

TRACESTATE = b"Tracestate"
"""Tracestate [permanent]

[Trace Context]
"""

TRAILER = b"Trailer"
"""Trailer [permanent]

[RFC9110, Section 6.6.2: HTTP Semantics]
"""

TRANSFER_ENCODING = b"Transfer-Encoding"
"""Transfer-Encoding [permanent]

[RFC9112, Section 6.1: HTTP Semantics]
"""

TTL = b"TTL"
"""TTL [permanent]

[RFC 8030, Section 5.2: Generic Event Delivery Using HTTP Push]
"""

UPGRADE = b"Upgrade"
"""Upgrade [permanent]

[RFC9110, Section 7.8: HTTP Semantics]
"""

URGENCY = b"Urgency"
"""Urgency [permanent]

[RFC 8030, Section 5.3: Generic Event Delivery Using HTTP Push]
"""

URI = b"URI"
"""URI [obsoleted]

[RFC 2068: Hypertext Transfer Protocol -- HTTP/1.1]
"""

USER_AGENT = b"User-Agent"
"""User-Agent [permanent]

[RFC9110, Section 10.1.5: HTTP Semantics]
"""

VARIANT_VARY = b"Variant-Vary"
"""Variant-Vary [permanent]

[RFC 2295: Transparent Content Negotiation in HTTP]
"""

VARY = b"Vary"
"""Vary [permanent]

[RFC9110, Section 12.5.5: HTTP Semantics]
"""

VIA = b"Via"
"""Via [permanent]

[RFC9110, Section 7.6.3: HTTP Semantics]
"""

WANT_CONTENT_DIGEST = b"Want-Content-Digest"
"""Want-Content-Digest [permanent]

[RFC-ietf-httpbis-digest-headers-13, Section 4: Digest Fields]
"""

WANT_DIGEST = b"Want-Digest"
"""Want-Digest [obsoleted]

[RFC 3230: Instance Digests in HTTP][RFC-ietf-httpbis-digest-headers-13, Section 1.3: Digest Fields]
"""

WANT_REPR_DIGEST = b"Want-Repr-Digest"
"""Want-Repr-Digest [permanent]

[RFC-ietf-httpbis-digest-headers-13, Section 4: Digest Fields]
"""

WARNING = b"Warning"
"""Warning [obsoleted]

[RFC9111, Section 5.5: HTTP Caching]
"""

WWW_AUTHENTICATE = b"WWW-Authenticate"
"""WWW-Authenticate [permanent]

[RFC9110, Section 11.6.1: HTTP Semantics]
"""

X_CONTENT_TYPE_OPTIONS = b"X-Content-Type-Options"
"""X-Content-Type-Options [permanent]

[Fetch]
"""

X_FRAME_OPTIONS = b"X-Frame-Options"
"""X-Frame-Options [permanent]

[HTML]
"""

STAR = b"*"
"""* [permanent]

[RFC9110, Section 12.5.5: HTTP Semantics]

(reserved)
"""
