#!/usr/bin/env python3
"""
PR Description Generator - Main entry point

Usage:
    python scripts/main.py --from-file commits.txt
    python scripts/main.py --commits "feat: xxx" "fix: yyy"
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.git_analyzer import CommitAnalyzer
from scripts.pr_generator import PRGenerator


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Generate professional PR descriptions from git commits'
    )
    
    # Create mutually exclusive group for input methods
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--from-file',
        type=str,
        help='Read commits from a file (one commit per line)'
    )
    input_group.add_argument(
        '--commits',
        nargs='+',
        help='Directly provide commits as arguments'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='pr_description.md',
        help='Output file path (default: pr_description.md)'
    )
    
    return parser.parse_args()


def load_commits_from_file(file_path):
    """Load commits from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            commits = [line.strip() for line in f if line.strip()]
        return commits
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def main():
    """Main function"""
    args = parse_arguments()
    
    # Load commits
    if args.from_file:
        commits = load_commits_from_file(args.from_file)
    else:
        commits = args.commits
    
    if not commits:
        print("Error: No commits provided.")
        sys.exit(1)
    
    print(f"Processing {len(commits)} commits...")
    
    # Analyze commits
    analyzer = CommitAnalyzer()
    parsed_commits = analyzer.parse_commits(commits)
    
    # Generate PR description
    generator = PRGenerator()
    pr_title = generator.generate_title(parsed_commits)
    pr_summary = generator.generate_summary(parsed_commits)
    pr_features = generator.generate_features(parsed_commits)
    
    # Format output
    output = generator.format_output(pr_title, pr_summary, pr_features)
    
    # Save to file
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ PR description saved to: {args.output}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)
    
    # Print to console
    print("\n" + "="*60)
    print(output)
    print("="*60)


if __name__ == '__main__':
    main()