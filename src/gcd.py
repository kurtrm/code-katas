"""
Increase player attack by gcd if monster defense > player attack
or monster defense if monster defense < player attack.
"""


def final_attack_value(x, monster_list):
    """
    """
    for defense in monster_list:
        if x >= defense:
            x += defense
        else:
            attack_divisors = {divisor for divisor in range(1, x + 1)
                               if x % divisor == 0}
            defense_divisors = {divisor for divisor in range(1, defense + 1)
                                if defense % divisor == 0}
            gcd = max(attack_divisors & defense_divisors)
            x += gcd

    return x
