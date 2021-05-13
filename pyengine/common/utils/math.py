from pyengine.common.utils.vec2 import Vec2


def clamp(value, mini=None, maxi=None):
    if mini is not None and value < mini:
        return mini
    elif maxi is not None and value > maxi:
        return maxi
    return value


def distance_between_rect(pos, size, pos2, size2):
    pos_ = pos + size
    pos2_ = pos2 + size2

    left = pos2_.x < pos.x
    right = pos_.x < pos2.x
    bottom = pos2_.y < pos.y
    top = pos_.y < pos2.y

    if top and left:
        return Vec2(pos.x, pos_.y).distance(Vec2(pos2_.x, pos2.y))
    elif left and bottom:
        return pos.distance(pos2_)
    elif bottom and right:
        return Vec2(pos_.x, pos.y).distance(Vec2(pos2.x, pos2_.y))
    elif right and top:
        return pos_.distance(pos2)
    elif left:
        return pos.x - pos2_.x
    elif right:
        return pos2.x - pos_.x
    elif bottom:
        return pos.x - pos2_.y
    elif top:
        return pos2.y - pos_.y
    else:
        return 0
