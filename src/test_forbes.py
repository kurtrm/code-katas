"""Test forbes script."""
import pytest


@pytest.fixture
def youngest():
    """Youngest answer."""
    return {
        "name": "Mark Zuckerberg",
        "age": 32,
        "rank": 6,
        "net_worth (USD)": 44600000000,
        "source": "Facebook",
        "country": "United States"
    }


@pytest.fixture
def oldest():
    """Oldest answer under 80."""
    return {
        "name": "Phil Knight",
        "age": 78,
        "rank": 24,
        "net_worth (USD)": 24400000000,
        "source": "Nike",
        "country": "United States"
    }


def test_returns_oldest(oldest):
    """Ensure we get the oldest billionaire back."""
    from forbes import main
    important_list = main()
    assert (important_list[0],
            int(important_list[1]),
            important_list[2]) == (oldest['name'],
                                   oldest['net_worth (USD)'],
                                   oldest['source'])


def test_returns_youngest(youngest):
    """Ensure we get the youngest billionaire back."""
    from forbes import main
    important_list = main()
    assert (important_list[3],
            int(important_list[4]),
            important_list[5]) == (youngest['name'],
                                   youngest['net_worth (USD)'],
                                   youngest['source'])
