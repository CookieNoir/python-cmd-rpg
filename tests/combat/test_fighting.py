from rpg.models.game_items.weapon import Weapon
from rpg.models.skills.skill import Skill
from rpg.models.skills.skill_step import SkillStep
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.damage_types import DamageTypes
from rpg.repositories.skill_repository import SkillRepository
from rpg.repositories.item_repository import ItemRepository
from rpg.models.entities.entity import Entity
from rpg.combat.fighter import Fighter
from rpg.combat.skill_selectors.manual_skill_selector import ManualSkillSelector
from rpg.input.mock_console_input import MockConsoleInput
from rpg.combat import fighting


def test_make_move_prints_log(capsys):
    skills = SkillRepository()
    skills.fill_from_dict(
        {"Test skill": Skill("Test skill", True, SkillTargets.ENEMIES, [SkillStep(DamageTypes.PURE, True, 1.0)],
                             "Deals {} PURE damage")})
    items = ItemRepository()
    items.fill_from_dict({0: Weapon(0, "Test weapon", 1, 0, ["Test skill"])})
    caster = Fighter(Entity("Robert"), True)
    fighters = [caster, Fighter(Entity("Mark"), False)]
    game_input = MockConsoleInput()
    skill_selector = ManualSkillSelector(game_input)
    fighting._make_move(caster, fighters, skill_selector, items, skills)
    out, err = capsys.readouterr()
    assert len(out) > 0
    assert out.count('\n') >= 3
