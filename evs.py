import hashlib
import random
import string
from collections import defaultdict

class ElectronicVotingSystem:
    def __init__(self):
        self.voters = {}  # To store voter info and hashed votes
        self.candidates = ["Alice", "Bob", "Charlie"]
        self.votes = defaultdict(int)  # To count votes for each candidate
    
    def register_voter(self, voter_id):
        """Register a voter with a unique ID."""
        # Generate a random voter token for anonymity
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.voters[voter_id] = {'token': token, 'vote_hash': None}
        print(f"Voter {voter_id} registered with token: {token}")
    
    def cast_vote(self, voter_id, candidate):
        """Allow a voter to cast their vote for a candidate."""
        if voter_id not in self.voters:
            raise ValueError("Voter not registered")
        
        if candidate not in self.candidates:
            raise ValueError("Invalid candidate")
        
        # Hash the vote for integrity
        vote_hash = hashlib.sha256(f"{self.voters[voter_id]['token']}:{candidate}".encode()).hexdigest()
        
        # Ensure that the vote hasn't been cast already
        if self.voters[voter_id]['vote_hash']:
            raise ValueError("Vote already cast")
        
        # Store the hash to prevent tampering
        self.voters[voter_id]['vote_hash'] = vote_hash
        
        # Increment the vote count for the candidate
        self.votes[candidate] += 1
        
        print(f"Vote cast successfully by voter {voter_id} for {candidate}.")
    
    def tally_votes(self):
        """Tally the votes and return the result."""
        return dict(self.votes)

# Example usage
if __name__ == "__main__":
    evs = ElectronicVotingSystem()
    evs.register_voter("Voter1")
    evs.register_voter("Voter2")

    evs.cast_vote("Voter1", "Alice")
    evs.cast_vote("Voter2", "Bob")

    results = evs.tally_votes()
    print("Election Results:", results)
