def evaluate_performance(total_score, kd_ratio):
    if total_score >= 100 or kd_ratio >= 2.0:
        return "MVP"
    elif total_score >= 60:
        return "Good Game"
    else:
        return "Needs Practice"

def main():
    player_name = "Bob"
    total_score = 0
    total_kills = 0
    total_deaths = 0
    
    print("Match Analysis for", player_name)
    
    while True:
        try:
            num_rounds = int(input("Enter number of rounds played (1-5): "))
            if num_rounds > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for round_num in range(1, num_rounds + 1):
        print("\nRound", round_num, ":")
        kills = int(input("  Enter kills: "))
        deaths = int(input("  Enter deaths (minimum 1): "))
        if deaths < 1:
            deaths = 1
            
        round_score = (kills * 15) - (deaths * 5)
        total_score += round_score
        total_kills += kills
        total_deaths += deaths
        
        print("  -> Round Score:", round_score)

    overall_kd = round(total_kills / total_deaths, 2)
    rank = evaluate_performance(total_score, overall_kd)

    print("Player:", player_name)
    print("Total Kills:", total_kills, "| Total Deaths:", total_deaths)
    print("Overall K/D Ratio:", overall_kd)
    print("Final Score:", total_score)
    print("Performance Rank:", rank)

if __name__ == "__main__":
    main()