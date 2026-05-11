# main_app.py
from logic_tools import assign_badge  # استيراد الوظيفة من الملف الأول

while True:
    try:
        team_name = input("Enter the team name (or 'E' to exit): ")
        if team_name.upper() == "E":
            break
            
        member_name = input("Enter the member name: ")
        score = float(input("Enter the score: "))

        badge = assign_badge(score)

        print(f"Rank for {member_name}: {badge}")
        
        # حفظ البيانات في ملف نصي
        with open("nova_database.txt", "a") as file:
            file.write(f"Team: {team_name} | Member: {member_name} | Rank: {badge}\n")
            
    except ValueError:
        print("Input error: Please enter a valid numerical score.")

print("Nova System Shutdown: Data is safely stored.")