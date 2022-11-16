"""Class Ball."""
from cmath import pi


class BallErr(Exception):
    """Error for wrong attributes."""

    pass


class Ball:
    """Contains methods for ball movement."""

    def __init__(self, radius: float) -> None:
        """Method which initialize class Ball.

        Args:
            radius: float - radius of a ball.

        Raises:
            BallErr: Exception - radius less then 0 or 0
        """
        self.radius = radius
        if not self.is_valid():
            raise BallErr

    def uniform_motion(self, speed: float, time: float):
        """Determines the turn of the ball in a certain time.

        Args:
            speed: float - speed of a ball in meters per second.
            time: float - time of movement in seconds.

        Returns:
            The turn of the ball in degrees rounded to 3 decimal places,
            None if speed or time less then 0 or 0.
        """
        if speed > 0 and time > 0:
            period = (self.radius * 2 * pi) / speed
            ang_velocity = (2 * pi) / period
            to_valid = 180
            good_digrees = 360
            return round((ang_velocity * time) * (to_valid / pi) % good_digrees, 3)
        return None

    def uniformly_accelerated_motion(self, acceleration: float, time):
        """Determines the turn of the ball in a certain time.

        Args:
            acceleration: float - acceleration of a ball in meters per second squared.
            time: float - time of movement in seconds.

        Returns:
            The turn of the ball in degrees rounded to 3 decimal places,
            None if acceleration or time less then 0 or 0.
        """
        if acceleration > 0 and time > 0:
            speed = acceleration * time
            ang_velocity = speed / self.radius
            ang_acceleration = ang_velocity / time
            to_valid = 180
            good_digrees = 360
            return round(((ang_acceleration * time ** 2) / 2) * (to_valid / pi) % good_digrees, 3)
        return None

    def is_valid(self):
        """Checks acceptability of an attribute."""
        return isinstance(self.radius, (int, float)) and self.radius > 0
