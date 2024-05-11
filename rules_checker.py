import re
import sys

def check_rules(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Define regex patterns for rule validation
            rule_pattern = re.compile(r'\d+\.\s+\*\*(.{1,60})\*\* - (.{1,160})')

            # Split content into individual rules
            rules = content.split('# Rules')[1].strip().split('\n\n')

            # Check each rule
            for i, rule in enumerate(rules, start=1):
                match = rule_pattern.match(rule)
                if not match:
                    raise ValueError(f"Rule {i} does not adhere to the specified format.")
                else:
                    rule_number, rule_description, rule_explanation = match.groups()
                    if len(rule_description) > 60:
                        raise ValueError(f"Rule {i}: The description exceeds 60 characters.")
                    if len(rule_explanation) > 160:
                        raise ValueError(f"Rule {i}: The explanation exceeds 160 characters.")

        print("Rules are correct lengths.")
        return True

    except FileNotFoundError:
        print("File not found.")
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rules_checker.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    check_rules(filename)
