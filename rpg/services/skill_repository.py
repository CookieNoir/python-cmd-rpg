from rpg.models.skills.skill import Skill


class SkillRepository:
    _data: dict = {}

    @staticmethod
    def fill(data: dict):
        SkillRepository._data = data

    @staticmethod
    def get_skill_by_name(name: str) -> Skill:
        return SkillRepository._data[name]
