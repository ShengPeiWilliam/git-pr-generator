"""
Git Commit Analyzer

Parses commits in conventional commit format:
    <type>: <description>
"""

import re


class CommitAnalyzer:
    """Analyze and parse git commits"""
    
    # Commit types and their priorities
    COMMIT_TYPES = {
        'feat': {'priority': 1, 'label': 'Features'},
        'fix': {'priority': 2, 'label': 'Bug Fixes'},
        'refactor': {'priority': 3, 'label': 'Refactoring'},
        'test': {'priority': 4, 'label': 'Tests'},
        'docs': {'priority': 5, 'label': 'Documentation'},
        'chore': {'priority': 6, 'label': 'Chores'},
    }
    
    def __init__(self):
        """Initialize the analyzer"""
        self.commit_pattern = re.compile(r'^(\w+):\s*(.+)$')
    
    def parse_commits(self, commits):
        """
        Parse a list of commits
        
        Args:
            commits: List of commit strings
            
        Returns:
            List of parsed commit dicts with 'type', 'description', 'raw'
        """
        parsed = []
        
        for commit in commits:
            parsed_commit = self.parse_single_commit(commit)
            parsed.append(parsed_commit)
        
        return parsed
    
    def parse_single_commit(self, commit):
        """
        Parse a single commit line
        
        Args:
            commit: Single commit string
            
        Returns:
            Dict with 'type', 'description', 'raw'
        """
        commit = commit.strip()
        
        match = self.commit_pattern.match(commit)
        
        if match:
            commit_type = match.group(1).lower()
            description = match.group(2).strip()
            
            return {
                'type': commit_type,
                'description': description,
                'raw': commit,
                'valid': True
            }
        else:
            # Invalid format, store as-is
            return {
                'type': 'unknown',
                'description': commit,
                'raw': commit,
                'valid': False
            }
    
    def group_by_type(self, parsed_commits):
        """
        Group commits by type
        
        Args:
            parsed_commits: List of parsed commits
            
        Returns:
            Dict grouped by type, sorted by priority
        """
        grouped = {}
        
        for commit in parsed_commits:
            commit_type = commit['type']
            if commit_type not in grouped:
                grouped[commit_type] = []
            grouped[commit_type].append(commit)
        
        # Sort by priority
        sorted_grouped = {}
        for commit_type in sorted(
            grouped.keys(),
            key=lambda x: self.COMMIT_TYPES.get(x, {}).get('priority', 999)
        ):
            sorted_grouped[commit_type] = grouped[commit_type]
        
        return sorted_grouped
    
    def get_type_label(self, commit_type):
        """Get human-readable label for commit type"""
        return self.COMMIT_TYPES.get(commit_type, {}).get('label', commit_type.title())