# Postman Collection

This folder contains a Postman collection that mirrors the pytest test suite.

## Import Instructions

1. Open Postman
2. Navigate to 'Collections' and import `JSONPlaceholder_API_Tests.postman_collection.json`
3. Navigate to 'Environment' and import `JSONPlaceholder.postman_environment`
4. Click "Import"

## Running the Collection

1. Click on the collection name
2. Click "Run" to execute all tests
3. All 7 requests should pass with their test assertions

## Test Coverage

- GET all posts
- GET single post
- GET invalid post (404 handling)
- GET posts filtered by user
- POST create new post
- PUT update existing post
- DELETE post
