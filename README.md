# news_portal

<img width="1066" alt="Screenshot 2024-05-07 at 19 08 02" src="https://github.com/nitish-gautam/news_portal/assets/46977634/a2e90af4-72cf-46b7-8f41-e5dd1e29cce6">

## 1. Use of Django REST Framework (DRF):
Today's approach to developing web applications, especially those requiring robust, scalable REST
APIs, prominently features frameworks like Django REST Framework. DRF provides a powerful,
flexible toolkit for building Web APIs with several key advantages:

Modular and Reusable Components: DRF utilises class-based views and serializers,
allowing for modular, reusable code that can easily be adjusted or extended without modifying the
core logic.

Automatic URL Routing: By using routers, DRF automatically handles the URL routing for
all CRUD operations associated with model view-sets, simplifying the API's URL configuration and
reducing the potential for human error.

## 2. Implementation of Testing Strategies ( implemented pytest):
Modern software development emphasises test-driven development (TDD) or at least ensuring
comprehensive test coverage post-development to catch bugs early and facilitate continuous
integration processes. 

Using pytest with Django:
Integration with Django: Pytest integrates seamlessly with Django's test framework,
allowing you to use Django's ORM and other components within your tests.

Database Isolation: The @pytest.mark.django_db decorator is used to ensure that each
test has access to a clean database instance, which is essential for testing database interactions
without side effects.


## 3. Cleaner and maintainable codebase
#### 3.1.1. Application of Object-Oriented Programming (OOP):
Ensured that the codebase adheres strictly to OOP principles can greatly enhance its clarity and
maintainability.

#### 3.2.2. Domain-Driven Design (DDD):
Applying DDD principles involves modelling the domain closely to ensure the software reflects
requirements. Key aspects include:

Entity and Value Object: Identify entities and value objects within the application. For
instance, ‘News’ and ‘Comment’ are entities with unique identifiers, whereas attributes like title or
body can be treated as value objects.

Aggregates: Treat the ‘News’ model as an aggregate root with ‘Comment’ as part of the
same aggregate if comments cannot exist without a news item.


## 4. Clean Architecture:
Clearly separate the layers of the application (presentation, business logic, data access) to reduce
dependencies between them. For instance, Django views should handle HTTP requests and
responses but delegate business logic to service classes.

High-level modules should not depend on low-level modules but on abstractions. Using interfaces
or abstract classes can help achieve this in Python.


## 5. Scalability and Flexibility:
Use of Environment Variables: For settings like database configurations or third-party APIs, use
environment variables to keep the codebase secure and flexible across different deployment
environments.

Asynchronous Operations: Consider integrating asynchronous views or tasks where heavy or
blocking operations are needed, using Django's support for asynchronous views or Celery for
background tasks.
