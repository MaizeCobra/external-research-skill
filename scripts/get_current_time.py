"""
Time-aware search utility for external research.

This script provides current date/time information in formats useful for
constructing search queries that prioritize recent and relevant results.

Usage:
    python get_current_time.py           # Get all formats
    python get_current_time.py --year    # Just the year
    python get_current_time.py --search  # Search-friendly format
"""

import sys
from datetime import datetime

def get_time_info():
    """Returns a dictionary of useful time formats for search queries."""
    now = datetime.now()
    
    return {
        "year": now.strftime("%Y"),
        "year_short": now.strftime("%y"),
        "month_year": now.strftime("%B %Y"),  # "February 2026"
        "quarter": f"Q{(now.month - 1) // 3 + 1} {now.year}",  # "Q1 2026"
        "date_iso": now.strftime("%Y-%m-%d"),
        "search_suffix": now.strftime("%Y"),  # Most useful for appending to queries
        "full_datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
    }

def print_search_tips(time_info):
    """Print search query tips with current time context."""
    print("=" * 60)
    print("TIME-AWARE SEARCH TIPS")
    print("=" * 60)
    print(f"\nCurrent Year: {time_info['year']}")
    print(f"Current Quarter: {time_info['quarter']}")
    print(f"Current Date: {time_info['date_iso']}")
    print()
    print("SEARCH QUERY EXAMPLES:")
    print("-" * 40)
    print(f'  "FastAPI JWT authentication {time_info["year"]}"')
    print(f'  "React useEffect best practices {time_info["year"]}"')
    print(f'  "Python security vulnerabilities {time_info["year"]}"')
    print(f'  "Next.js 14 breaking changes {time_info["year"]}"')
    print()
    print("WHY ADD THE YEAR?")
    print("-" * 40)
    print("  • Libraries and frameworks update frequently")
    print("  • Best practices evolve over time")
    print("  • Security recommendations change")
    print("  • Adding the year filters out outdated content")
    print("  • Results prioritize recent tutorials and docs")
    print()
    print("SEARCH SUFFIXES TO TRY:")
    print("-" * 40)
    print(f'  "[topic] {time_info["year"]}"          - General current info')
    print(f'  "[topic] latest {time_info["year"]}"   - Emphasize recency')
    print(f'  "[topic] best practices {time_info["year"]}" - Current standards')
    print(f'  "[topic] changelog {time_info["year"]}" - Recent changes')
    print()

def main():
    time_info = get_time_info()
    
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg in ["--year", "-y"]:
            print(time_info["year"])
        elif arg in ["--search", "-s"]:
            print(time_info["search_suffix"])
        elif arg in ["--quarter", "-q"]:
            print(time_info["quarter"])
        elif arg in ["--date", "-d"]:
            print(time_info["date_iso"])
        elif arg in ["--json", "-j"]:
            import json
            print(json.dumps(time_info, indent=2))
        elif arg in ["--tips", "-t"]:
            print_search_tips(time_info)
        elif arg in ["--help", "-h"]:
            print(__doc__)
            print("\nOptions:")
            print("  --year, -y     Just the current year (e.g., 2026)")
            print("  --search, -s   Search-friendly suffix")
            print("  --quarter, -q  Current quarter (e.g., Q1 2026)")
            print("  --date, -d     ISO date (e.g., 2026-02-08)")
            print("  --json, -j     All formats as JSON")
            print("  --tips, -t     Print search tips with examples")
            print("  --help, -h     Show this help message")
        else:
            print(f"Unknown argument: {arg}")
            print("Use --help for usage information")
            sys.exit(1)
    else:
        print_search_tips(time_info)

if __name__ == "__main__":
    main()
