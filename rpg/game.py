from services.skill_repository import SkillRepository
from services.item_repository import ItemRepository
from data.skills_database import all_skills
from data.items_database import all_items


def fill_repositories_with_data():
    SkillRepository.fill(all_skills)
    ItemRepository.fill(all_items)


def start_game():
    fill_repositories_with_data()
    pass  # start game
