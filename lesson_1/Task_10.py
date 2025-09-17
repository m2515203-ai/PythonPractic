team = input("Название команды: ")
print(f"{team} - чемпион!")

print("-" * len(team))

team_lower = team.lower()
print(f"Длина: {len(team_lower)}")
print(f"Есть буква 'п': {'п' in team_lower}")
print(f"Буква 'а' встречается: {team_lower.count('а')} раз")
