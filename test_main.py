import pytest
from main import Ball

radius_valid_check = [(1.0), (3.5), (2.3)]


@pytest.mark.parametrize('radius', radius_valid_check)
def test_valid_radius(radius: float):
    """The function checks the ball radius for validity.

    Args:
        radius (float): radius of ball
    """
    assert Ball(radius).radius == radius



uniform_ball_motion_check_ans = [(5, 3, 4, 137.51), (8.7, 4.5, 1.2, 35.563), (10, 10, 10, 212.958)]


@pytest.mark.parametrize('radius, speed, time, ans', uniform_ball_motion_check_ans)
def test_uniform(radius: float, speed: float, time: float, ans: float):
    """The function checks the values uniform_motion

    Args:
        radius (float): radius of ball
        speed (float): speed of ball
        time (float): the time that the ball travels
        ans (float): answer uniform_motion
    """
    assert Ball(radius).uniform_motion(speed, time) == ans


uniformly_accelerated_motion_ans = [(5, 5, 5, 356.197), (4.5, 1.5, 7.8, 220.979)]


@pytest.mark.parametrize('radius, acceleration, time, ans', uniformly_accelerated_motion_ans)
def test_accelereted(radius: float, acceleration: float, time: float, ans: float):
    """The function checks the values uniformly_accelerated_motion

    Args:
        radius (float): radius of ball
        acceleration (float): acceleration of ball
        time (float): the time that the ball travels
        ans (float): answer uniform_motion
    """
    assert Ball(radius).uniformly_accelerated_motion(acceleration, time) == ans