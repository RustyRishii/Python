# Challenge 1 – Authenticated API Consumption

Goal: Practice making authenticated API requests, handling pagination, and surfacing relevant data.

## Steps
1. Generate a fine-grained GitHub personal access token with the `repo:read` scope (Settings → Developer settings → Personal access tokens).  
2. Export the token so the script can read it:  
   `export GITHUB_TOKEN="ghp_your_token_here"`  
3. Run the helper script:  
   `python authenticated_api.py --max-count 5 --visibility all`  
4. Observe how headers, timeouts, and pagination are handled inside the script (`fetch_repositories` + `_paginated_get`).  
5. Tweak parameters to explore:  
   - `--per-page 100` to reduce API round-trips.  
   - `--visibility public` to see public repos only.  
   - `--env-var OTHER_VAR` if you store the token under a different name.  
6. Extend the script with your own experiments (e.g., list issues, filter by language, write results to JSON).

## Key Takeaways
- Always keep secrets outside of source code (environment variables, secret managers).  
- Use explicit timeouts (`requests.get(..., timeout=10)`) to avoid hanging processes.  
- Parse the `Link` header for pagination; GitHub combines multiple relation links in a comma-separated list.  
- Provide clear error messages for missing credentials, invalid tokens, or rate limiting.  
- Keep the script importable by wrapping execution in `if __name__ == "__main__":`.

