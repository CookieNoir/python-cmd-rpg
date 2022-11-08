from rpg.combat.fighter import Fighter
from rpg.models.entities.entity import Entity
from rpg.combat.skill_selectors.automatic_skill_selector import AutomaticSkillSelector
from rpg.models.skills.skill_targets import SkillTargets
from rpg.models.skills.skill import Skill
from rpg.models.game_items.weapon import Weapon


def test_select_skill_returns_some_skill():
    automatic_skill_selector = AutomaticSkillSelector()
    possible_skills = [Skill("Skill 1", True, SkillTargets.ENEMIES, [], description="None"),
                       Skill("Skill 2", True, SkillTargets.ALLIES, [], description="None"),
                       Skill("Skill 3", True, SkillTargets.EVERYONE, [], description="None")]
    caster_entity = Entity("John")
    weapon = Weapon(1, "Test weapon", 1)
    caster = Fighter(caster_entity, True)
    fighters = [caster, Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False),
                Fighter(Entity("Enemy 2"), False)]
    result = automatic_skill_selector.select_skill(caster, possible_skills, weapon, fighters)
    assert type(result) is Skill
    assert result in possible_skills


def test_select_direct_target_returns_some_target():
    automatic_skill_selector = AutomaticSkillSelector()
    targets = [Entity("Tom"), Entity("Boris"), Entity("Anton")]
    result = automatic_skill_selector.select_direct_target(targets)
    assert type(result) is Entity
    assert result in targets


def test_select_skill_and_targets_returns_not_none():
    automatic_skill_selector = AutomaticSkillSelector()
    possible_skills = [Skill("Skill 1", True, SkillTargets.ENEMIES, [], description="None"),
                       Skill("Skill 2", True, SkillTargets.ALLIES, [], description="None"),
                       Skill("Skill 3", True, SkillTargets.EVERYONE, [], description="None")]
    caster_entity = Entity("John")
    weapon = Weapon(1, "Test weapon", 1)
    caster = Fighter(caster_entity, True)
    fighters = [caster, Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False),
                Fighter(Entity("Enemy 2"), False)]
    skill, direct_target, indirect_targets = automatic_skill_selector.select_skill_and_targets(caster, possible_skills,
                                                                                               weapon, fighters)
    assert skill is not None
    assert direct_target is not None
    assert indirect_targets is not None
    assert direct_target not in indirect_targets
