def print_skills(skills: list,
                 weapon_damage: int,
                 index_offset: int = 1):
    for skill in skills:
        damages = skill.get_skill_step_damages(weapon_damage)
        print(f"{index_offset:<3} {skill.name}")
        print(f"Description:    {skill.description.format(damages)}")
        index_offset += 1
