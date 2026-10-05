def main():
    score = [78, 85, 90, 66, 88]
    total = sum(score)
    average = total / len(score)

    print("=== main/master branch output ===")
    print(f"Scores: {score}")
    print(f"Sum: {total}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()