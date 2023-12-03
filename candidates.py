from typing import Dict

class Candidate:
    def __init__(self, name: str, votes: int = 0) -> None:
        """
        Initialize Candidate object with name and votes.

        Args:
        - name (str): The name of the candidate.
        - votes (int): The initial number of votes (default is 0).
        """
        self._name = name
        self._votes = votes

    def vote(self) -> None:
        """Increment the vote count for the candidate."""
        self._votes += 1

    def get_name(self) -> str:
        """Return the name of the candidate."""
        return self._name

    def get_votes(self) -> int:
        """Return the number of votes for the candidate."""
        return self._votes

    def to_string(self) -> str:
        """Convert candidate information to a string format."""
        return f"{self._name},{self._votes}\n"

    @staticmethod
    def from_string(candidate_string: str) -> 'Candidate':
        """
        Create a Candidate object from a string representation.

        Args:
        - candidate_string (str): String containing candidate information.

        Returns:
        - Candidate: A Candidate object created from the string.
        """
        name, votes = candidate_string.strip().split(',')
        return Candidate(name, int(votes))

def read_candidates() -> Dict[str, Candidate]:
    """
    Read candidates' data from a file and return a dictionary of Candidate objects.

    Returns:
    - Dict[str, Candidate]: A dictionary containing Candidate objects.
    """
    candidates = {}
    try:
        with open("candidates.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                candidate = Candidate.from_string(line)
                candidates[candidate.get_name()] = candidate
    except FileNotFoundError:
        print("Candidates file not found. Starting with empty candidates.")
    return candidates

def write_candidates(candidates: Dict[str, Candidate]) -> None:
    """Write candidates' data to a file."""
    with open("candidates.txt", 'w') as file:
        for candidate in candidates.values():
            file.write(candidate.to_string())