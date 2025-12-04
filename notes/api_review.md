# APIcalls.py – Quick Review

- Imports `process_time_ns`/`print_tb` but never uses them – remove to keep the module tidy.  
- Uses a module-level `base_url` constant but still repeats slashes (`base_url` already ends with `/`).  
- No timeout on `requests.get`, so a slow API call may hang the script.  
- Errors bubble up as `None` with a `print`; better to raise an exception or return structured data.  
- Response parsing assumes keys exist (e.g., `abilities[0]`) and will crash otherwise; add guards.  
- Secrets/config (like API base URL) should come from env vars or config, not hardcoded.  
- The script runs on import; wrap main logic in `if __name__ == "__main__":` to keep it importable.  
- Consider logging instead of raw `print` calls.  

