"""HTTP routes for the spongemock API."""

import random

from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__)


def spongemock(text: str) -> str:
    """Return *text* with the casing of each character randomized."""
    return "".join(
        character.upper() if random.choice((True, False)) else character.lower()
        for character in text
    )


@api.get("/health")
def health():
    """Report that the service is available."""
    return jsonify({"status": "ok"})


@api.get("/spongemock")
def mock_text():
    """Transform the required ``text`` query parameter."""
    text = request.args.get("text")
    if text is None:
        return jsonify({"error": "query is not valid", "mockedText": None}), 400

    return jsonify({"error": None, "mockedText": spongemock(text)})
