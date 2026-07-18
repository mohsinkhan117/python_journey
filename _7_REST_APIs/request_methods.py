import requests

# ============================================================
# PYTHON 'requests' LIBRARY — REST API QUICK REVISION SHEET
# Covers: GET, POST, PUT, PATCH, DELETE, headers, query params,
# payload/body (data vs json), status codes, sessions, auth,
# error handling, and free practice API URLs to test against.
# ============================================================
#
# NOTE: this script makes REAL network calls, so run it on your
# own machine with internet access (not in a restricted sandbox).
# pip install requests   -> if not already installed
#
# ============================================================
# FREE PRACTICE API URLs (no signup / no API key needed)
# ============================================================
#   https://jsonplaceholder.typicode.com   -> fake REST API: posts, users, comments, todos
#   https://reqres.in/api                   -> fake user-management API (login, CRUD)
#   https://httpbin.org                     -> echoes back whatever you send (great for learning headers/params/body)
#   https://dummyjson.com                   -> realistic fake data: products, carts, users, auth
#   https://catfact.ninja/fact               -> tiny GET-only API, good for absolute basics
#   https://restcountries.com/v3.1/all        -> real public data about countries, GET-only
# ============================================================


BASE = "https://jsonplaceholder.typicode.com"   # used throughout this file


print("\n================= GET REQUEST (READ DATA) =================")
# GET -> retrieve data from the server. Should NOT change anything on the server.
response = requests.get(f"{BASE}/posts/1")

print(response.status_code)    # 200 = success
print(response.url)            # the final URL that was actually requested
print(response.json())         # parses the JSON response body into a Python dict/list
print(response.text[:100])     # raw response body as a string (truncated here)
print(response.ok)             # True if status_code < 400

# -----------------------------------------------------------

print("\n================= RESPONSE OBJECT — KEY ATTRIBUTES =================")
# Everything useful about a response lives on the response object
print(response.headers)         # response headers (dict-like) sent BACK by the server
print(response.headers["Content-Type"])   # access a specific header
print(response.status_code == 200)        # manual status check
print(response.elapsed)          # how long the request took (a timedelta)

# -----------------------------------------------------------

print("\n================= QUERY PARAMETERS (params=) =================")
# Query params get appended to the URL as ?key=value&key2=value2
# Use params= instead of manually building the string yourself.
params = {"userId": 1}
response = requests.get(f"{BASE}/posts", params=params)
print(response.url)              # shows params were added: .../posts?userId=1
print(len(response.json()))      # number of posts returned for that user

# -----------------------------------------------------------

print("\n================= REQUEST HEADERS =================")
# Headers send extra metadata with the request (auth tokens, content type, etc.)
custom_headers = {
    "User-Agent": "python-revision-script",
    "Accept": "application/json",
    # "Authorization": "Bearer YOUR_TOKEN_HERE"   # typical way to send an auth token
}
response = requests.get(f"{BASE}/posts/1", headers=custom_headers)
print(response.status_code)
print(response.request.headers)   # headers that were actually SENT (on the request object)

# -----------------------------------------------------------

print("\n================= POST REQUEST (CREATE DATA) =================")
# POST -> send data to create a NEW resource on the server.
# payload/body: the data you're sending, usually as JSON.

new_post = {
    "title": "My New Post",
    "body": "This is the content of the post.",
    "userId": 1
}

# json= automatically converts the dict to JSON AND sets Content-Type header for you
response = requests.post(f"{BASE}/posts", json=new_post)
print(response.status_code)     # 201 = Created
print(response.json())          # server echoes back the created resource (with a new "id")

# data= sends form-encoded data instead of JSON (older style, still common)
response = requests.post(f"{BASE}/posts", data=new_post)
print(response.status_code)
print(response.json())

# -----------------------------------------------------------

print("\n================= PUT REQUEST (FULL UPDATE) =================")
# PUT -> replace an ENTIRE existing resource with new data
# Convention: you must send ALL fields, even ones that didn't change.
updated_post = {
    "id": 1,
    "title": "Completely Updated Title",
    "body": "Completely updated body text.",
    "userId": 1
}
response = requests.put(f"{BASE}/posts/1", json=updated_post)
print(response.status_code)     # 200 = OK (updated)
print(response.json())

# -----------------------------------------------------------

print("\n================= PATCH REQUEST (PARTIAL UPDATE) =================")
# PATCH -> update ONLY the specific fields you send, leave the rest untouched
partial_update = {"title": "Just Changing the Title"}
response = requests.patch(f"{BASE}/posts/1", json=partial_update)
print(response.status_code)     # 200 = OK
print(response.json())          # only "title" changed, other fields stay the same

# -----------------------------------------------------------

print("\n================= DELETE REQUEST (REMOVE DATA) =================")
# DELETE -> removes a resource from the server
response = requests.delete(f"{BASE}/posts/1")
print(response.status_code)     # 200 or 204 = successfully deleted
print(response.text)            # often empty body on successful delete

# -----------------------------------------------------------

print("\n================= HTTP STATUS CODES — QUICK REFERENCE =================")
#   CODE   MEANING                          TYPICAL CAUSE
#   -----  -------------------------------  ------------------------------------
#   200    OK                                 successful GET / PUT / PATCH
#   201    Created                            successful POST that created something
#   204    No Content                         successful DELETE, nothing to return
#   400    Bad Request                        malformed request / bad payload
#   401    Unauthorized                       missing or invalid auth credentials
#   403    Forbidden                          authenticated but not allowed to access this
#   404    Not Found                          wrong URL / resource doesn't exist
#   429    Too Many Requests                  rate limit exceeded
#   500    Internal Server Error              something broke on the SERVER's side

# -----------------------------------------------------------

print("\n================= ERROR HANDLING =================")
# raise_for_status() -> raises an exception automatically if status is 4xx/5xx
try:
    response = requests.get(f"{BASE}/posts/99999")   # doesn't exist -> 404
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)

# Catching connection/timeout issues too (e.g. no internet, server down)
try:
    response = requests.get("https://thisdomaindoesnotexist12345.com", timeout=5)
except requests.exceptions.ConnectionError:
    print("Connection error: could not reach the server")
except requests.exceptions.Timeout:
    print("Timeout error: server took too long to respond")

# -----------------------------------------------------------

print("\n================= TIMEOUTS =================")
# ALWAYS set a timeout in real code - without it, a hung server can freeze your program forever
response = requests.get(f"{BASE}/posts/1", timeout=5)   # waits max 5 seconds
print(response.status_code)

# -----------------------------------------------------------

print("\n================= AUTHENTICATION =================")
# Basic auth -> username/password sent with the request
# response = requests.get(url, auth=("username", "password"))

# Bearer token auth -> most common for modern APIs (send token in headers)
# headers = {"Authorization": "Bearer YOUR_TOKEN"}
# response = requests.get(url, headers=headers)

# Example using reqres.in's fake login endpoint (returns a fake token)
login_payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
response = requests.post("https://reqres.in/api/login", json=login_payload)
print(response.status_code)
print(response.json())    # -> {'token': 'QpwL5tke4Pnpja7X4'}  (fake token, for practice only)

# -----------------------------------------------------------

print("\n================= SESSIONS (REUSE HEADERS/COOKIES ACROSS CALLS) =================")
# requests.Session() -> keeps headers/cookies/auth persistent across multiple calls,
# instead of repeating them on every single request. Also reuses the connection (faster).
session = requests.Session()
session.headers.update({"Authorization": "Bearer fake-token-123"})

response1 = session.get(f"{BASE}/posts/1")   # both calls automatically include the header
response2 = session.get(f"{BASE}/posts/2")
print(response1.status_code, response2.status_code)

# -----------------------------------------------------------

print("\n================= FILE UPLOAD (files=) =================")
# files= is used to upload a file as multipart/form-data
# with open("example.txt", "rb") as f:
#     response = requests.post("https://httpbin.org/post", files={"file": f})
# print(response.json())

# -----------------------------------------------------------

print("\n================= QUICK METHOD CHEAT SHEET (REST VERBS) =================")
#   METHOD    PURPOSE                          IDEMPOTENT?*   TYPICAL SUCCESS CODE
#   --------  -------------------------------  -------------  ----------------------
#   GET        read/retrieve data                 Yes            200
#   POST       create a new resource               No             201
#   PUT        replace an entire resource           Yes            200
#   PATCH      update part of a resource             No*            200
#   DELETE     remove a resource                     Yes            200 / 204
#
#   *Idempotent = calling it multiple times has the SAME effect as calling it once.
#    PATCH is often not idempotent since repeated partial updates can compound
#    (e.g. incrementing a counter field), depending on what the update actually does.