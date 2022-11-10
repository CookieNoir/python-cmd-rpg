from rpg.models.game_items.weapon import Weapon
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.damage_types import DamageTypes
from rpg.repositories.skill_repository import SkillRepository
from rpg.repositories.item_repository import ItemRepository
from rpg.models.entities.entity import Entity
from rpg.combat.fighter import Fighter
from rpg.combat.skill_selectors.automatic_skill_selector import AutomaticSkillSelector
from rpg.combat import fighting


def test_make_move_applies_skill_ands_prints_log(capsys):
    skills = SkillRepository()
    skills.fill_from_dict(
        {"Test skill": Skill("Test skill", True, SkillTargets.ENEMIES, [SkillStep(DamageTypes.PURE, True, 1.0)],
                             "Deals {} PURE damage")})
    items = ItemRepository()
    items.fill_from_dict({0: Weapon(0, "Test weapon", 1, 0, ["Test skill"])})
    caster = Fighter(Entity("Robert"), True)
    fighters = [caster, Fighter(Entity("Mark"), False)]
    skill_selector = AutomaticSkillSelector()
    fighting._make_move(caster, fighters, skill_selector, items, skills)
    out, err = capsys.readouterr()
    assert fighters[1].entity.is_alive() is False
    assert len(out) > 0
    assert out.count('\n') >= 3


def test_fight_allies_win_returns_true():
    skills = SkillRepository()
    skills.fill_from_dict(
        {"Test skill": Skill("Test skill", True, SkillTargets.ENEMIES, [SkillStep(DamageTypes.PURE, True, 1.0)],
                             "Deals {} PURE damage")})
    items = ItemRepository()
    items.fill_from_dict({0: Weapon(0, "Test weapon", 1, 0, ["Test skill"])})
    allies = [Entity("Ally", base_speed=1, base_max_health=4)]
    enemies = [Entity("Enemy", base_speed=3)]
    skill_selector = AutomaticSkillSelector()
    assert fighting.fight(allies, enemies, skill_selector, skill_selector, items, skills) is True


def test_fight_enemies_win_returns_false():
    skills = SkillRepository()
    skills.fill_from_dict(
        {"Test skill": Skill("Test skill", True, SkillTargets.ENEMIES, [SkillStep(DamageTypes.PURE, True, 1.0)],
                             "Deals {} PURE damage")})
    items = ItemRepository()
    items.fill_from_dict({0: Weapon(0, "Test weapon", 1, 0, ["Test skill"])})
    allies = [Entity("Ally", base_speed=1, base_max_health=4)]
    enemies = [Entity("Enemy", base_speed=4)]
    skill_selector = AutomaticSkillSelector()
    assert fighting.fight(allies, enemies, skill_selector, skill_selector, items, skills) is False
