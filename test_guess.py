# test_guess.py

def check_guess(secret, guess):
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else:
        return "Correct"

def test_check_guess():
    secret = 42
    assert check_guess(secret, 20) == "Too low"
    assert check_guess(secret, 50) == "Too high"
    assert check_guess(secret, 42) == "Correct"
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_check_guess()   
