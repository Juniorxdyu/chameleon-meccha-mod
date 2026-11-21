"""World-to-screen math for the Meccha Chameleon ESP overlay."""
from __future__ import annotations
import numpy as np


VIEW_MATRIX_SIZE = 16


def _matrix_from_flat(flat: list[float]) -> np.ndarray:
    return np.array(flat, dtype=np.float32).reshape(4, 4)


def world_to_screen(
    view_matrix: list[float],
    world_pos: tuple[float, float, float],
    screen_w: int,
    screen_h: int,
) -> tuple[float, float] | None:
    m = _matrix_from_flat(view_matrix)
    x, y, z = world_pos
    clip = np.array([x, y, z, 1.0], dtype=np.float32)
    clip = m @ clip
    if clip[3] < 0.001:
        return None
    ndc_x = clip[0] / clip[3]
    ndc_y = clip[1] / clip[3]
    sx = (screen_w / 2) * (ndc_x + 1.0)
    sy = (screen_h / 2) * (1.0 - ndc_y)
    return float(sx), float(sy)