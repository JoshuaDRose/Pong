import pytest
from ball import Ball

def test_rect():
	ball = Ball(10, 10, 5)
	assert (ball.rect.x and ball.rect.y >= 0), "Invalid position"

def test_vector():
    ball = Ball(10, 10, 5)
    assert (ball.direction.x and ball.direction.y == 1), "Invalid vector"
