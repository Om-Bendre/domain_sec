# from core.models.configuration import Configuration

# # Change these two imports
# from core.models.requests.security_headers_request import SecurityHeadersRequest
# from scanners.security_headers.scanner import SecurityHeadersScanner


# configuration = Configuration()

# scanner = SecurityHeadersScanner()

# request = SecurityHeadersRequest(
#     target="https://google.com",
# )

# result = scanner.scan(
#     request,
#     configuration,
# )

# print("\nStatus")
# print(result.status)



# print("\nErrors")

# if result.errors:

#     for error in result.errors:

#         print(f"\nType    : {error.error_type}")
#         print(f"Message : {error.message}")

# else:

#     print("No Errors")