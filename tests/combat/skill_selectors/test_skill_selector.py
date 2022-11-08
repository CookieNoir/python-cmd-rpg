from rpg.combat.fighter import Fighter
from rpg.models.entities.entity import Entity
from rpg.combat.skill_selectors.skill_selector import SkillSelector
from rpg.models.skills.skill_targets import SkillTargets


def test_get_possible_targets_team_ally_targets_enemies_returns_2():
    fighters = [Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False), Fighter(Entity("Enemy 2"), False)]
    skill_selector = SkillSelector()
    targets = skill_selector._get_possible_targets(fighters, SkillTargets.ENEMIES, True)
    assert len(targets) == 2


def test_get_possible_targets_team_ally_targets_allies_returns_1():
    fighters = [Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False), Fighter(Entity("Enemy 2"), False)]
    skill_selector = SkillSelector()
    targets = skill_selector._get_possible_targets(fighters, SkillTargets.ALLIES, True)
    assert len(targets) == 1


def test_get_possible_targets_team_enemy_targets_enemies_returns_1():
    fighters = [Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False), Fighter(Entity("Enemy 2"), False)]
    skill_selector = SkillSelector()
    targets = skill_selector._get_possible_targets(fighters, SkillTargets.ENEMIES, False)
    assert len(targets) == 1


def test_get_possible_targets_team_enemy_targets_allies_returns_2():
    fighters = [Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False), Fighter(Entity("Enemy 2"), False)]
    skill_selector = SkillSelector()
    targets = skill_selector._get_possible_targets(fighters, SkillTargets.ALLIES, False)
    assert len(targets) == 2


def test_get_possible_targets_targets_everyone_returns_3():
    fighters = [Fighter(Entity("Ally 1"), True), Fighter(Entity("Enemy 1"), False), Fighter(Entity("Enemy 2"), False)]
    skill_selector = SkillSelector()
    targets = skill_selector._get_possible_targets(fighters, SkillTargets.EVERYONE, True)
    assert len(targets) == 3
