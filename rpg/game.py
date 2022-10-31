from repositories.skill_repository import SkillRepository
from repositories.item_repository import ItemRepository
from data.skills_database import all_skills
from data.items_database import all_items


def fill_repositories_with_data():
    skills = SkillRepository()
    items = ItemRepository()
    skills.fill_from_dict(all_skills)
    items.fill_from_dict(all_items)


def start_game():
    fill_repositories_with_data()
    pass  # start game
