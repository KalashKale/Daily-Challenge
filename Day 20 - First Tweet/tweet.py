def tweet_balance(tweet):
  # Write code below 💖
    words = tweet.split()
    used = 0

    for word in words:
        if word.startswith('@'):
            used += 20
        elif word.startswith('http://') or word.startswith('https://'):
            used += 23
        else:
            used += len(word)

    # add spaces
    if len(words) > 1:
        used += len(words) - 1

    return 140 - used

tweet = input("Enter your tweet: ")
print(f"Characters remaining: {tweet_balance(tweet)}")