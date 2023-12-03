from candidates import Candidate, read_candidates, write_candidates
from voting_menu import VoteMenu
from candidate_menu import CandidateMenu
from exceptions import InvalidInputError
from typing import Dict

CANDIDATES_FILE: str = "candidates.txt"

def vote(candidate_choice: str, candidates: Dict[str, Candidate]) -> None:
    """Register a vote for the selected candidate."""
    candidate = candidates.get(candidate_choice)
    if candidate:
        candidate.vote()
        print(f"Voted {candidate.get_name()}")
    else:
        raise InvalidInputError("Invalid candidate choice")

def display_results(candidates: Dict[str, Candidate]) -> None:
    """Display the results showing the number of votes for each candidate."""
    total_votes = sum(candidate.get_votes() for candidate in candidates.values())
    print("\n————————————————————————————")
    for candidate in candidates.values():
        print(f"{candidate.get_name()} - {candidate.get_votes()}", end=", ")
    print(f"Total - {total_votes}")
    print("————————————————————————————")

def main() -> None:
    """Main function to run the voting system."""
    candidates = read_candidates()

    vote_menu = VoteMenu()
    candidate_menu = CandidateMenu()

    while True:
        vote_menu.display()
        option = input("Option: ").strip().lower()

        if option == "v":
            candidate_menu.display()
            candidate_choice = input("Candidate: ").strip()

            try:
                vote(candidate_choice, candidates)
            except InvalidInputError as e:
                print(f"Error: {e}")

        elif option == "x":
            display_results(candidates)
            write_candidates(candidates)
            break

if __name__ == "__main__":
    main()