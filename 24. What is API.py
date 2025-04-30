# DJango REST API Framework:

# What is API..?
An API - Application Programming Interface

API is a software (application) interface, that allows two or more applications  to talk to each other.

#  Using api we can collect or send particular (selected) data or information to other application

# There are 4 types of API:
1) Private (Internal) API 😀
2) Composite API  😀
3) Partner API    😀
4) Public (Open or External) API  😀




1) Private (Internal) API: ✅

# Internal APIs are only made available for use inside a company and are meant to streamline data transfers between teams and systems. Developers working for the company can use these APIs, but external developers can’t.

# Because internal APIs aren't documented in a publicly released software development kit (or at all in some cases), they are often completely hidden from the public. However, many companies do eventually go public with their internal APIs.

# Using APIs for internal data transfers is regarded as more efficient, secure, and traceable. It’s also a scalable solution — when a business introduces a new internal system, this system can communicate with existing systems via their APIs.

2) Composite API: ✅

# Composite APIs combine multiple APIs allowing developers to bundle calls or requests and receive one unified response from different servers. If you need data from different applications or data sources, you would use a composite API. Alternatively, you can use a composite API to set off an automatic chain of calls and responses without requiring your intervention.

# Because they reduce the number of total API calls, composite APIs can result in less server load and overall faster systems, as well as reduced complexity in the system. They’re commonly deployed in microservices in which one job may require data from many internal APIs to complete.

# Take this example from Stoplight: Say you want to create an order within a shopping cart API. You might think that this takes just one request. But, in fact, several requests must be made. First, you need to create a customer profile. Then, you need to create the order, add an item, add another, and change the status of the order. Instead of making five separate API calls in succession, you can make just one with a composite API.

3) Partner API:  ✅

# Partner APIs are shared externally, but only among those who have a business relationship with the company providing the API. Access is limited to authorized clients with official licenses, and thus security measures tend to be stronger with partner APIs than with public APIs.

# Some businesses favor partner APIs because they want (1) greater control over who can access their resources and (2) more say in how those resources are used. For example, Pinterest adopted a submission-based approach to providing access to new data services via its API, requiring partners to submit a request detailing how they would like to use the API before being granted access.

4) Public (Open or External) API: ✅ 
# Open APIs, also known as public APIs or external APIs, are available to use by any developer. As a result, open APIs typically have relatively low authentication and authorization measures, and are often restricted in the assets they share. While some open APIs are free, others require a subscription fee to use, which is often tiered based on the number of calls made to the API.

# There are several advantages to making APIs public, the biggest being the ability to share data openly. This encourages any external business or developer to integrate with the app that owns the API, making both the third-party software and the API more valuable. Because of the lack of restrictions and easy implementation allowed by the open API, third parties can quickly leverage the data it provides.


