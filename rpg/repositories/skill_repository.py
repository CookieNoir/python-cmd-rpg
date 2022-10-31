from local_repository import LocalRepository
from rpg.models.skills.skill import Skill


class SkillRepository(LocalRepository):
    def __init__(self):
        super().__init__()

    def get_item(self, key: int) -> Skill:
        return super().get_item(key)
