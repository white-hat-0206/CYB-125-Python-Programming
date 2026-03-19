import logging, time, hashlib

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Increments a lowercase alphabetic password guess mutating the character list in place 
# returns True if successfully advanced (e.g., 'a'→'b', 'az'→'ba'); 
# returns False when the sequence overflows past 'zzzzzz'.
def next_guess(chars):
    pos = len(chars) - 1
    while pos >= 0:
        if chars[pos] != "z":
            chars[pos] = chr(ord(chars[pos]) + 1); 
            return True
        chars[pos] = "a"; 
        pos -= 1
    return False

# Performs a brute-force search of all lowercase alphabetic strings up to max_len, 
# hashes each guess with SHA-256 until the target hash is matched or no match has been found.
def brute_force_password(target_hash, max_len=6):
    attempts = 0
    start = time.time()

    # -------------------------------------------
    # Your brute force logic goes here
    # -------------------------------------------
    # HINT: Outer loop should iterate over password lengths (1 → max_len)
    # HINT: Start each length with the smallest possible string ("aaa...")
    # HINT: Continue generating guesses until overflow occurs
    # HINT: Output a debug statement for every 1000 attempts
    
    # HINT: Hash the guess using SHA-256 and compare to target_hash            
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
    
    # HINT: If hashes match, compute elapsed time and return results
    elapsed = time.time() - start
    print(f"Recovered: {guess}  attempts={attempts}  time={elapsed:.6f}s")
    
    # HINT: Advance to next lexicographic candidate using next_guess()
        # If it returns False, we've exhausted this length.

    # HINT: If all lengths are exhausted without success, raise an exception


# This function manages the user input loop, prompting for SHA-256 hashes to crack.
# Calls the brute-force function, passing the user provided hash.
# Catches exceptions thrown by the brute_force_password() function.
# Catches exceptions thrown by the input() function on Ctrl + C.
# Tracks attempts and runtime and displays a summary of results before exiting.
def main():
    cracked = []
    total_attempts = 0
    overall_start = time.time()

    # -------------------------------------------
    # Your main function logic goes here
    # -------------------------------------------

    total_overall_time = time.time()-overall_start

    
# Entry point for the program
if __name__ == "__main__":
    main()