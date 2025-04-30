Types of API Architectures:

# We can also understand APIs in terms of their architecture. An API’s architecture consists of the rules that guide what information an API can share with clients and how it shares the data. REST, SOAP, and RPC are the most popular API architectures in use today — let’s unpack each one in more detail.

1) REST API - REpresentational State Transfer  (very important) 💡
# Today, the majority of web APIs are built on REST. REST, which stands for representational state transfer, is a set of guidelines for scalable, lightweight, and easy-to-use APIs. 

# A REST API (or “RESTful” API) is an API that follows REST guidelines and is used for transferring data from a server to a requesting client.

# For a more in-depth look at REST guidelines, see our full guide to REST APIs. Briefly, these guidelines are:

Client-Server Separation: 
# All client-server interactions must be in the form of a request from the client, followed by a response from the server. Servers can’t request and clients can’t respond.

Uniform Interface: 
# All requests and responses must use HTTP as the communication protocol and be formatted in a specific way to ensure compatibility between any client and any server. 

Server responses are formatted in JSON - (JavaScript Object Notation).

Stateless: 
# Each client-server interaction is independent of every other interaction. The server stores no data from client requests and remembers nothing from past interactions.

Layered system: 
# Requests and responses must always be formatted the same way, even when passed through intermediate servers between the client and the API.

Cacheable: 
# Server responses should indicate whether a provided resource can be cached by the client and for how long.
# By following these guidelines, REST APIs can be used for quick, easy, secure data transfers, making them a popular choice among developers.

2) SOAP:
# SOAP (Simple Object Access Protocol) is a protocol for transmitting data across networks and can be used to build APIs. SOAP is standardized by the World Wide Web Consortium (W3C) and utilizes XML to encode information.

# SOAP strictly defines how messages should be sent and what must be included in them. This makes SOAP APIs more secure than REST APIs, although the rigid guidelines also make them more code-heavy and harder to implement in general.

# For this reason, SOAP is often implemented for internal data transfers that require high security, and the more flexible REST architecture is deployed more commonly everywhere else. But, one more advantage to SOAP is that it works over any communication protocol (not just HTTP, as is the case with REST).

3) RPC:
# The RPC (Remote Procedural Call) protocol is the most straightforward of the three architectures. Unlike REST and SOAP that facilitate the transfer of data, RPC APIs invoke processes. In other words, they execute scripts on a server.

# RPC APIs may employ either JSON (a JSON-RPC protocol) or XML (an XML-RPC protocol) in their calls. XML is more secure and more accommodating than JSON, but these two protocols are otherwise similar. Though the RPC protocol is strict, it's a relatively simple and easy way to execute code on remote networks.

# RPC APIs are limited in their security and capabilities, so you likely won’t see them as often as REST or SOAP APIs on the web. However, it can be used for internal systems for making basic process requests, especially many at once.


Summarize API:

# Internal APIs, - which only internal teams may access.
# Composite APIs, - which combine multiple APIs.
# Partner APIs, - which only authorized developers may access.
# Open Public APIs, - which any developer can access.


There are also three common types of API architectures:

# REST, - a collection of guidelines for lightweight, scalable web APIs.
# SOAP, - a stricter protocol for more secure APIs.
# RPC, - a protocol for invoking processes that can be written with XML (XML-RPC) or JSON 


