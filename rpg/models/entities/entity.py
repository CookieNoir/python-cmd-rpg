from rpg.models.entities.entity_stat import EntityStat
from rpg.models.skills.damage_types import DamageTypes
from rpg.models.game_items.stat_types import StatTypes
from rpg.models.game_items.game_item_types import GameItemTypes
from rpg.models.game_items.equippable_item import EquippableItem
from math import floor, ceil


class Entity:
    def __init__(self,
                 name: str,
                 base_max_health: int = 1,
                 base_speed: int = 1,
                 base_physical_armor: int = 0,
                 base_magical_armor: int = 0,
                 base_damage: int = 0,
                 base_armor_pierce: int = 0,
                 base_damage_reflection: int = 0):
        self._name = name
        if base_max_health < 1:
            base_max_health = 1
        if base_speed < 1:
            base_speed = 1
        self._stats = {
            StatTypes.MAX_HEALTH: EntityStat(base_max_health),
            StatTypes.SPEED: EntityStat(base_speed),
            StatTypes.PHYSICAL_RESISTANCE: EntityStat(base_physical_armor),
            StatTypes.MAGICAL_RESISTANCE: EntityStat(base_magical_armor),
            StatTypes.DAMAGE: EntityStat(base_damage),
            StatTypes.ARMOR_PIERCE: EntityStat(base_armor_pierce),
            StatTypes.DAMAGE_REFLECTION: EntityStat(base_damage_reflection),
        }
        self._equipped_items = {
            GameItemTypes.WEAPON: 0,
            GameItemTypes.HEAD: 0,
            GameItemTypes.BODY: 0,
            GameItemTypes.LEGS: 0,
        }
        self._current_health = self.max_health

    @property
    def name(self) -> str:
        return self._name

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value: int):
        max_health = self.max_health
        if value > max_health:
            value = max_health
        elif value < 0:
            value = 0
        self._current_health = value

    @property
    def max_health(self):
        return self._stats[StatTypes.MAX_HEALTH].get_total_value()

    def is_alive(self):
        return self.current_health > 0

    def _recalculate_current_health(self, start_max_health: int):
        if self.max_health == start_max_health:
            return
        multiplier = self.current_health / start_max_health
        self.current_health = ceil(self.max_health * multiplier)

    def _get_healed(self, healing_value):
        if not self.is_alive or healing_value < 0:
            return
        self.current_health += healing_value

    def _get_damaged(self, damage: int) -> int:
        self.current_health -= damage
        return self._get_damage_reflection(damage)

    def get_damaged(self, damage_type: DamageTypes, damage: int, pierce: int = 0) -> (int, int):
        def _get_incoming_damage(in_damage: int, in_pierce: int, in_resistance: int) -> int:
            resisted = in_resistance - in_pierce
            return max(in_damage - resisted, 1)

        if not self.is_alive():
            return 0, 0
        modified_damage = damage
        damage_reflected = 0
        match damage_type:
            case DamageTypes.PHYSICAL:
                modified_damage = _get_incoming_damage(damage, pierce,
                                                       self._stats[
                                                           StatTypes.PHYSICAL_RESISTANCE].get_total_value())
                damage_reflected = self._get_damaged(modified_damage)
            case DamageTypes.MAGICAL:
                modified_damage = _get_incoming_damage(damage, pierce,
                                                       self._stats[StatTypes.MAGICAL_RESISTANCE].get_total_value())
                damage_reflected = self._get_damaged(modified_damage)
            case DamageTypes.PURE:
                damage_reflected = self._get_damaged(damage)
            case DamageTypes.HEALING:
                self._get_healed(damage)
            case DamageTypes.REFLECTED:
                self._get_damaged(damage)
        return modified_damage, damage_reflected

    def _free_item_slot(self, item_slot: GameItemTypes) -> int:
        pop_item_id = self._equipped_items[item_slot]
        self._equipped_items[item_slot] = 0
        if pop_item_id > 0:
            self._remove_item_modifiers(pop_item_id)
        return pop_item_id

    def remove_item(self, item_id: int) -> int:
        removed = False
        for i in self._equipped_items:
            if self._equipped_items[i] == item_id:
                self._equipped_items[i] = 0
                self._remove_item_modifiers(item_id)
                removed = True
                break
        if removed:
            return item_id
        else:
            return 0

    def _remove_item_modifiers(self, item_id: int):
        prev_max_health = self.max_health
        for i in self._stats:
            self._stats[i].remove_modifier(item_id)
        self._recalculate_current_health(prev_max_health)

    def equip_item(self, item: EquippableItem) -> int:
        item_slot = item.item_type
        match item_slot:
            case GameItemTypes.OTHER:
                result = 0
            case _:
                if self._equipped_items[item_slot] == item.item_id:
                    result = item.item_id
                else:
                    previous_item = self._free_item_slot(item_slot)
                    self._equipped_items[item_slot] = item.item_id
                    self._apply_item_modifiers(item)
                    result = previous_item
        return result

    def _apply_item_modifiers(self, item: EquippableItem):
        prev_max_health = self.max_health
        for stat_modifier in item.stat_modifiers:
            self._stats[stat_modifier.stat_type].add_modifier(item.item_id,
                                                              stat_modifier.is_multiplier,
                                                              stat_modifier.value)
        self._recalculate_current_health(prev_max_health)

    @property
    def speed(self):
        return self._stats[StatTypes.SPEED].get_total_value()

    @property
    def pierce(self):
        return self._stats[StatTypes.ARMOR_PIERCE].get_total_value()

    def _get_damage_reflection(self, damage: int) -> int:
        return self._stats[StatTypes.DAMAGE_REFLECTION].addition \
               + floor(damage * (1.0 - 1.0 / self._stats[StatTypes.DAMAGE_REFLECTION].multiplier))

    def buff_damage(self, damage: int) -> int:
        return ceil((damage + self._stats[StatTypes.DAMAGE].addition) * self._stats[
            StatTypes.DAMAGE].multiplier)

    def get_item_from_slot(self, item_slot: GameItemTypes) -> int:
        if item_slot == GameItemTypes.OTHER:
            return 0
        else:
            return self._equipped_items[item_slot]
