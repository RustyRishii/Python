"""
Challenge 1 – Authenticated API Consumption
-------------------------------------------

This script demonstrates how to call GitHub's REST API v3 with a personal
access token (PAT), including pagination, timeouts, and basic error handling.

Usage:
    export GITHUB_TOKEN=<your_token_with_repo_scope>
    python authenticated_api.py --max-count 5

The script fetches the authenticated user's repositories and prints a concise
summary for each entry. Adjust the CLI flags to explore the API.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, Iterable, Iterator, Optional

import requests

GITHUB_API_ROOT = "https://api.github.com"


class AuthenticatedApiError(RuntimeError):
    """Custom error for clearer exception handling."""


def get_token(env_var: str = "GITHUB_TOKEN") -> str:
    token = os.getenv(env_var)
    if not token:
        raise AuthenticatedApiError(
            f"Missing GitHub token; set the {env_var} environment variable."
        )
    return token


def _build_headers(token: str) -> Dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _parse_next_link(link_header: Optional[str]) -> Optional[str]:
    if not link_header:
        return None
    parts = [chunk.strip() for chunk in link_header.split(",")]
    for part in parts:
        if 'rel="next"' not in part:
            continue
        url_segment, _ = part.split(";", maxsplit=1)
        return url_segment.strip("<>")
    return None


def _paginated_get(
    url: str,
    token: str,
    params: Optional[Dict[str, str]] = None,
    timeout: int = 10,
) -> Iterator[requests.Response]:
    headers = _build_headers(token)
    next_url = url
    next_params = params

    while next_url:
        response = requests.get(
            next_url,
            headers=headers,
            params=next_params,
            timeout=timeout,
        )
        if response.status_code == 401:
            raise AuthenticatedApiError(
                "Unauthorized – check that your token is valid."
            )
        if response.status_code == 403 and "rate limit" in response.text.lower():
            raise AuthenticatedApiError("Hit the GitHub rate limit; try again later.")
        response.raise_for_status()

        yield response

        next_url = _parse_next_link(response.headers.get("Link"))
        next_params = None  # Only needed on the first request


def fetch_repositories(
    token: str,
    visibility: str = "all",
    per_page: int = 50,
) -> Iterable[Dict[str, object]]:
    params = {
        "visibility": visibility,
        "per_page": str(per_page),
        "sort": "pushed",
        "direction": "desc",
    }

    url = f"{GITHUB_API_ROOT}/user/repos"
    for response in _paginated_get(url, token, params=params):
        repos = response.json()
        if not isinstance(repos, list):
            raise AuthenticatedApiError(
                "Unexpected API shape; expected a list of repos."
            )
        for repo in repos:
            yield repo


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List GitHub repositories via authenticated API calls."
    )
    parser.add_argument(
        "--visibility",
        choices=("all", "public", "private"),
        default="all",
        help="Which repositories to include (default: all).",
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=50,
        help="GitHub page size. Higher values reduce round-trips (default: 50).",
    )
    parser.add_argument(
        "--max-count",
        type=int,
        default=10,
        help="Maximum number of repositories to print (default: 10).",
    )
    parser.add_argument(
        "--env-var",
        default="GITHUB_TOKEN",
        help="Environment variable that stores your API token (default: GITHUB_TOKEN).",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        token = get_token(args.env_var)
        repos = fetch_repositories(
            token, visibility=args.visibility, per_page=args.per_page
        )
        printed = 0
        for repo in repos:
            name = repo.get("full_name", "<unknown>")
            stars = repo.get("stargazers_count", 0)
            language = repo.get("language") or "n/a"
            visibility = "private" if repo.get("private") else "public"
            print(
                f"{name:40} | ⭐ {stars:<4} | {visibility:<7} | main language: {language}"
            )
            printed += 1
            if printed >= args.max_count:
                break
    except (AuthenticatedApiError, requests.RequestException) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
