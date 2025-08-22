def save_log(guess, attempts, play_again, filename="game_log.txt"):
    # Create the log text
    log_text = (
        f"Number {guess} guessed in {attempts} tries\n"
        "Thank you for playing\n"
        "want to play again \n"
        "click on play button\n"
        "log contents\n"
        f"adding:guess:{guess},count:{attempts},responses:{play_again}\n"
    )

    # Append the log to file
    with open(filename, "a") as f:
        f.write(log_text + "\n")

    print(log_text)


# Example usage
guess = 700
attempts = 8
play_again = "yes"

save_log(guess, attempts, play_again)
