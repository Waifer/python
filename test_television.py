import pytest
from television import Television

def test_init():
    """Test the __init__ method."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    """Test the power method."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    """Test the mute method."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = Muted"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_channel_up():
    """Test the channel_up method."""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Wrap around to MIN_CHANNEL
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    """Test the channel_down method."""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Wrap around to MAX_CHANNEL

def test_volume_up():
    """Test the volume_up method."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()  # Should stay at MAX_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.mute()
    tv.volume_up()  # Unmute and stay at MAX_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    """Test the volume_down method."""
    tv = Television()
    tv.power()
    tv.volume_down()  # Should stay at MIN_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

