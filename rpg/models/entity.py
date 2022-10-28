from math import ceil
from entity_stat import EntityStat
from damage_types import DamageTypes as DTypes
from entity_stat_types import EntityStatTypes as ESTypes
from inventory_item_types import InventoryItemTypes as IITypes
from equippable_item import EquippableItem
from stat_modifier import StatModifier
from item_catalogue import get_item_by_id


class Entity:
    def __init__(self,
                 base_max_health: int = 1,
                 base_speed: int = 1,
                 base_physical_armor: int = 0,
                 base_magical_armor: int = 0,
                 base_damage: int = 0,
                 base_armor_pierce: int = 0,
                 base_damage_reflection: int = 0):
        self.stats = {
            ESTypes.MAX_HEALTH: EntityStat(base_max_health),
            ESTypes.SPEED: EntityStat(base_speed),
            ESTypes.PHYSICAL_RESISTANCE: EntityStat(base_physical_armor),
            ESTypes.MAGICAL_RESISTANCE: EntityStat(base_magical_armor),
            ESTypes.DAMAGE: EntityStat(base_damage),
            ESTypes.ARMOR_PIERCE: EntityStat(base_armor_pierce),
            ESTypes.DAMAGE_REFLECTION: EntityStat(base_damage_reflection),
        }
        self.equipped_item_slots = {
            IITypes.WEAPON: 0,
            IITypes.HEAD: 0,
            IITypes.BODY: 0,
            IITypes.LEGS: 0,
        }
        max_health = self.stats[ESTypes.MAX_HEALTH].get_linear_value()
        self.current_health = max_health

    def _recalculate_current_health(self, start_max_health: int):
        new_max_health = self.stats[ESTypes.MAX_HEALTH].get_linear_value()
        if new_max_health == start_max_health:
            return
        multiplier = self.current_health / start_max_health
        self.current_health = ceil(new_max_health * multiplier)
        self._clamp_current_health()

    def _clamp_current_health(self):
        max_health = self.stats[ESTypes.MAX_HEALTH].get_linear_value()
        if self.current_health > max_health:
            self.current_health = max_health
        elif self.current_health < 0:
            self.current_health = 0

    def get_healed(self, healing_value):
        if self.current_health <= 0:
            return
        if healing_value < 0:
            return
        self.current_health += healing_value
        self._clamp_current_health()

    def get_damaged(self, damage_type: DTypes, damage: int, pierce: int = 0) -> int:
        if self.current_health <= 0:
            return 0
        damage_received = 0
        match damage_type:
            case DTypes.PHYSICAL:
                damage_received = self.stats[ESTypes.PHYSICAL_RESISTANCE].get_incoming_damage(damage, pierce)
            case DTypes.MAGICAL:
                damage_received = self.stats[ESTypes.MAGICAL_RESISTANCE].get_incoming_damage(damage, pierce)
            case DTypes.PURE:
                damage_received = damage
            case DTypes.HEALING:
                self.get_healed(damage)
        self.current_health -= damage_received
        self._clamp_current_health()
        return self.stats[ESTypes.DAMAGE_REFLECTION].get_damage_reflection(damage_received)

    def _free_item_slot(self, item_slot: IITypes) -> int:
        pop_item_id = self.equipped_item_slots[item_slot]
        self.equipped_item_slots[item_slot] = 0
        if pop_item_id > 0:
            self._remove_item_modifiers(pop_item_id)
        return pop_item_id

    def remove_item(self, item_id: int) -> int:
        removed = False
        for i in self.equipped_item_slots:
            if self.equipped_item_slots[i] == item_id:
                self.equipped_item_slots[i] = 0
                self._remove_item_modifiers(item_id)
                removed = True
                break
        if removed:
            return item_id
        else:
            return 0

    def _remove_item_modifiers(self, item_id: int):
        max_health = self.stats[ESTypes.MAX_HEALTH].get_linear_value()
        for i in self.stats:
            self.stats[i].remove_modifier(item_id)
        self._recalculate_current_health(max_health)

    def equip_item(self, item_id: int) -> int:
        item: EquippableItem = get_item_by_id(item_id)
        item_slot = item.item_type
        match item_slot:
            case IITypes.OTHER:
                return 0
            case _:
                previous_item = self._free_item_slot(item_slot)
                self.equipped_item_slots[item_slot] = item_id
                self._apply_item_modifiers(item)
                return previous_item

    def _apply_item_modifiers(self, item: EquippableItem):
        max_health = self.stats[ESTypes.MAX_HEALTH].get_linear_value()
        for i in item.stat_modifiers:
            if i is StatModifier:
                stat_modifier: StatModifier = i
                self.stats[stat_modifier.stat_type].add_modifier(item.item_id,
                                                                 stat_modifier.is_multiplier,
                                                                 stat_modifier.value)
        self._recalculate_current_health(max_health)
