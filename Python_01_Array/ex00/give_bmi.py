def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI for each pair of height and weight."""
    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans
    indicating whether each BMI exceeds the limit."""
    return [b > limit for b in bmi]
