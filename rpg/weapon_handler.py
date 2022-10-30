from services.item_repository import ItemRepository
from models.game_items.weapon import Weapon
from models.entity import Entity
from models.game_items.game_item_types import GameItemTypes


def get_entity_weapon(target_entity: Entity) -> Weapon:
    item_id = target_entity.get_item_from_slot(GameItemTypes.WEAPON)
    weapon_item: Weapon = ItemRepository.get_item_by_id(item_id)
    return weapon_item
