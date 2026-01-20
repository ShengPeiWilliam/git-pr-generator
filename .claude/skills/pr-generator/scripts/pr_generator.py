"""
PR Description Generator

Generates professional PR titles and descriptions from parsed commits
"""

from scripts.git_analyzer import CommitAnalyzer


class PRGenerator:
    """Generate PR descriptions from commits"""
    
    def __init__(self):
        """Initialize the generator"""
        self.analyzer = CommitAnalyzer()
    
    def generate_title(self, parsed_commits):
        """
        Generate PR title from commits
        
        Prioritizes:
        1. First 'feat' commit (if any)
        2. First 'fix' commit (if any)
        3. First commit overall
        
        Args:
            parsed_commits: List of parsed commit dicts
            
        Returns:
            PR title string
        """
        if not parsed_commits:
            return "chore: update codebase"
        
        # Try to find primary commit (feat > fix > first)
        primary_commit = None
        
        for commit in parsed_commits:
            if commit['type'] == 'feat':
                primary_commit = commit
                break
        
        if not primary_commit:
            for commit in parsed_commits:
                if commit['type'] == 'fix':
                    primary_commit = commit
                    break
        
        if not primary_commit:
            primary_commit = parsed_commits[0]
        
        # Build title from primary commit
        commit_type = primary_commit['type']
        description = primary_commit['description']
        
        # Add context if there are multiple changes
        if len(parsed_commits) > 1:
            # Count different types
            types = set(c['type'] for c in parsed_commits)
            if len(types) > 1:
                description += " and related changes"
        
        # Ensure max 50 characters
        title = f"{commit_type}: {description}"
        if len(title) > 50:
            # Truncate and add ellipsis
            title = title[:47] + "..."
        
        return title
    
    def generate_summary(self, parsed_commits):
        """
        Generate PR summary (1-2 sentences)
        
        Args:
            parsed_commits: List of parsed commit dicts
            
        Returns:
            Summary string
        """
        if not parsed_commits:
            return "Update codebase with various improvements."
        
        # Count commit types
        grouped = self.analyzer.group_by_type(parsed_commits)
        type_count = {}
        
        for commit_type, commits in grouped.items():
            type_count[commit_type] = len(commits)
        
        # Build summary based on commit types
        summary_parts = []
        
        if 'feat' in type_count:
            feature_count = type_count['feat']
            if feature_count == 1:
                summary_parts.append("Add a new feature")
            else:
                summary_parts.append(f"Implement {feature_count} new features")
        
        if 'fix' in type_count:
            fix_count = type_count['fix']
            if fix_count == 1:
                summary_parts.append("fix a bug")
            else:
                summary_parts.append(f"fix {fix_count} bugs")
        
        if 'docs' in type_count:
            summary_parts.append("update documentation")
        
        if 'refactor' in type_count:
            summary_parts.append("refactor code")
        
        # Compose summary
        if summary_parts:
            summary = summary_parts[0].capitalize()
            if len(summary_parts) > 1:
                summary += " and " + ", ".join(summary_parts[1:])
            summary += "."
        else:
            summary = "Update codebase."
        
        return summary
    
    def generate_features(self, parsed_commits):
        """
        Generate list of key features/changes
        
        Args:
            parsed_commits: List of parsed commit dicts
            
        Returns:
            List of feature strings
        """
        features = []
        
        grouped = self.analyzer.group_by_type(parsed_commits)
        
        for commit_type, commits in grouped.items():
            type_label = self.analyzer.get_type_label(commit_type)
            
            for commit in commits:
                description = commit['description']
                # Capitalize first letter if not already
                if description and description[0].islower():
                    description = description[0].upper() + description[1:]
                
                features.append(description)
        
        return features
    
    def format_output(self, title, summary, features):
        """
        Format the final PR description
        
        Args:
            title: PR title string
            summary: PR summary string
            features: List of feature strings
            
        Returns:
            Formatted PR description
        """
        output = f"Title:\n{title}\n\n"
        output += "Description:\n"
        output += f"## Summary\n{summary}\n\n"
        output += "## Key Features\n"
        
        for feature in features:
            output += f"- {feature}\n"
        
        return output