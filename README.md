# building-graphql-apis-with-python
This repository contains scripts documenting my learning journey on building APIs with GraphQL in Python

GraphQL is a **query language for APIs** and a **server-side runtime for fulfilling those queries** with existing data. It provides a **complete** and **understandable description** of the data in an API, giving clients the power to ask for **exactly what they need and nothing more**. 

This allows for more efficient data fetching, as clients can **retrieve multiple resources in a single request**, reducing the number of network calls. 

### Key characteristics and benefits of GraphQL include:

**Precise Data Fetching**: Clients can specify the exact data fields they require, preventing over-fetching or under-fetching of data.

**Single Request Efficiency**: GraphQL enables fetching data from multiple related resources in a single request, contrasting with typical REST APIs that might require multiple requests to different URLs.

**Strongly Typed Schema**: A GraphQL API is defined by a strongly typed schema, which provides a clear contract between the client and the server, enabling powerful developer tools and easier API evolution.

**Flexibility and Evolution**: The schema-based approach allows for easier evolution of APIs over time, as changes can be introduced without breaking existing clients if the schema is managed effectively.

**Data Source Agnostic**: GraphQL is not tied to any specific database or storage engine; it can be implemented on top of existing data sources, including databases, REST APIs, and microservices. 

**Improved Performance**: By reducing the number of network requests and enabling clients to control the data they receive, GraphQL can lead to faster and more stable applications, especially on slower network connections.
