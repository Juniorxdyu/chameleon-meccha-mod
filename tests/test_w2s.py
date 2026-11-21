from src.core.w2s import world_to_screen


def _identity_view():
    return [
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1,
    ]


def test_world_to_screen_center():
    pt = world_to_screen(_identity_view(), (0.0, 0.0, 0.0), 1920, 1080)
    assert pt is not None
    x, y = pt
    assert 950 < x < 970
    assert 530 < y < 550


def test_behind_camera_returns_none():
    vm = _identity_view()
    vm[15] = -1.0
    pt = world_to_screen(vm, (0.0, 0.0, 0.0), 1920, 1080)
    assert pt is None
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>