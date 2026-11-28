# === Stage 24: Взвешенный рейтинг ===
# Project: DanceStudio
"""
weighted_scores.py
Weighted rating for a dance group based on several metrics.
"""

DEFAULT_WEIGHTS = {
    "attendance": 0.30,
    "performance": 0.40,
    "attendance_bonus": 0.10,
    "participation": 0.20,
}


def normalize_weights(weights):
    """Return a copy of the weights dict with normalized values."""
    total = sum(weights.values())
    if total <= 0:
        return dict(weights)
    return {key: value / total for key, value in weights.items()}


def weighted_rating(metrics, weights):
    """
    Compute the weighted rating of a group.

    Parameters
    ----------
    metrics : dict
        Mapping of metric names to numeric values.
    weights : dict
        Mapping of metric names to their weights.

    Returns
    -------
    float
        The weighted rating.
    """
    effective_weights = normalize_weights(weights)
    total = 0.0
    for name, value in metrics.items():
        if name in effective_weights:
            total += value * effective_weights[name]
    return total


def clamp_rating(rating, low=0.0, high=1.0):
    """Clamp the rating to the given inclusive range."""
    return max(low, min(high, rating))


def group_ranking(groups, weights):
    """
    Return a list of (name, rating) tuples sorted by rating descending.

    Parameters
    ----------
    groups : list of dict
        Each element has the keys:
            name, metrics, attendance, performance, participation,
            attendance_bonus.
    weights : dict
        Weights for each metric.

    Returns
    -------
    list of tuple
        (group_name, rating) sorted by rating in descending order.
    """
    results = []
    for group in groups:
        metrics = {
            "attendance": group.get("attendance", 0.0),
            "performance": group.get("performance", 0.0),
            "attendance_bonus": group.get("attendance_bonus", 0.0),
            "participation": group.get("participation", 0.0),
        }
        rating = weighted_rating(metrics, weights)
        rating = clamp_rating(rating)
        results.append((group["name"], rating))
    return sorted(results, key=lambda item: item[1], reverse=True)
