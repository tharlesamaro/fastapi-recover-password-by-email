from typing import Any

CONTENT_DEFAULT = {"application/json": {"example": {"detail": "string"}}}

HTTP_RESPONSES: dict[str, dict[str, Any]] = {
    "400": {"content": CONTENT_DEFAULT, "description": "Bad Request"},
    "401": {"content": CONTENT_DEFAULT, "description": "Unauthorized"},
    "403": {"content": CONTENT_DEFAULT, "description": "Access not allowed"},
    "404": {"content": CONTENT_DEFAULT, "description": "Item not found"},
    "409": {"content": CONTENT_DEFAULT, "description": "Item already exists"},
    "500": {
        "content": {"application/json": {"example": "string"}},
        "description": "Internal Server Error",
    },
    # others reponses code here
}


def get_responses(*args: int | str) -> dict[str, dict[str, Any]]:
    responses = {}
    responses["401"] = HTTP_RESPONSES.get("401")
    responses["500"] = HTTP_RESPONSES.get("500")
    for arg in args:
        if not (response := HTTP_RESPONSES.get(str(arg))):
            continue
        responses[str(arg)] = response
    responses_sorted = dict(sorted(responses.items(), key=lambda x: x[0]))
    return responses_sorted
