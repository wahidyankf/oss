"""
Regular Expressions Comprehensive Demonstration

This heavily commented script illustrates Python's re module for advanced string
manipulation with detailed explanations of each regex concept and pattern.

Key Features Demonstrated:
- Pattern matching fundamentals (search, findall, match)
- Group extraction (numbered and named groups)
- Text substitutions and transformations
- Advanced regex features (lookarounds, quantifiers, flags)
"""

import re


# ========== BASIC PATTERN MATCHING ==========
def demonstrate_basic_matching():
    """
    Demonstrate fundamental regex patterns and matching methods.

    Covers:
    - re.search(): Find first match anywhere in string
    - re.findall(): Find all non-overlapping matches
    - re.match(): Match only at beginning of string
    - Basic pattern syntax (\\d for digits, {n} quantifiers)
    """
    text = "The workshop runs from 2023-12-01 to 2023-12-03"

    # re.search() returns first Match object or None
    # Pattern matches YYYY-MM-DD date format
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
    print(f"First date found: {date_match.group() if date_match else 'None'}")

    # re.findall() returns list of all matching strings
    all_dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
    print(f"All dates: {all_dates}")

    # re.match() only checks beginning of string
    starts_with = re.match(r"^The", text)
    print(f"Starts with 'The': {bool(starts_with)}")


# ========== GROUP EXTRACTION ==========
def demonstrate_groups():
    """
    Demonstrate capturing groups and named groups in regex.

    Key Concepts:
    - Parentheses () create capturing groups
    - Named groups (?P<name>...) for readable extraction
    - Group references in match objects
    """
    log_entry = "[ERROR] 2023-12-02 14:30:45 Failed to connect to database"

    # Basic numbered groups
    # Pattern breakdown:
    # \[(\w+)\]    - Captures word inside [] (log level)
    # (\d{4}-\d{2}-\d{2}) - Captures date
    # (\d{2}:\d{2}:\d{2}) - Captures time
    # (.+)           - Captures remaining message
    pattern = r"\[(\w+)\] (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (.+)"
    match = re.match(pattern, log_entry)
    if match:
        print(f"Log level (group 1): {match.group(1)}")
        print(f"Message (group 4): {match.group(4)}")

    # Named groups make patterns more readable
    # Syntax: (?P<name>pattern)
    named_pattern = (
        r"\[(?P<level>\w+)\] (?P<date>\d{4}-\d{2}-\d{2}) "
        r"(?P<time>\d{2}:\d{2}:\d{2}) (?P<message>.+)"
    )
    named_match = re.match(named_pattern, log_entry)
    if named_match:
        print(f"Time extracted via named group: {named_match.group('time')}")


# ========== SUBSTITUTIONS ==========
def demonstrate_substitutions():
    """
    Demonstrate text replacement using re.sub().

    Covers:
    - Simple pattern replacements
    - Using groups in replacements
    - Complex transformations
    """
    text = "Contact us at support@example.com or sales@example.org"

    # Simple replacement - anonymize emails
    # Pattern matches standard email format
    anonymized = re.sub(r"\b\w+@\w+\.\w+\b", "[EMAIL]", text)
    print(f"Anonymized: {anonymized}")

    # Replacement with group references
    # Reorders email parts: user@domain.tld -> domain.user@tld
    reordered = re.sub(r"(\w+)@(\w+)\.(\w+)", r"\2.\1@\3", text)
    print(f"Reordered emails: {reordered}")


# ========== ADVANCED FEATURES ==========
def demonstrate_advanced_features():
    """
    Demonstrate advanced regex features.

    Covers:
    - Lookaheads/lookbehinds
    - Greedy vs lazy quantifiers
    - Compilation flags (case insensitive)
    """
    text = "Prices: $10.99, $5, $123.45, $7.8"

    # Find prices > $10 using pattern matching
    # \$\d{2,} matches $ followed by 2+ digits
    high_prices = re.findall(r"\$\d{2,}\.?\d*", text)
    print(f"All prices: {re.findall(r'\$\d+\.?\d*', text)}")
    print(f"High prices (>$10): {high_prices}")

    # Case insensitive matching
    text = "Python is PYTHONIC and pythonista"
    print(f"Case insensitive matches: {re.findall(r'python\w*', text, re.IGNORECASE)}")


if __name__ == "__main__":
    """
    Main execution block demonstrating all regex features.
    """
    print("=== BASIC PATTERN MATCHING ===")
    demonstrate_basic_matching()

    print("\n=== GROUP EXTRACTION ===")
    demonstrate_groups()

    print("\n=== SUBSTITUTIONS ===")
    demonstrate_substitutions()

    print("\n=== ADVANCED FEATURES ===")
    demonstrate_advanced_features()

    print("\n=== DEMO COMPLETED ===")
    print("Tip: Experiment with the patterns in each function!")
