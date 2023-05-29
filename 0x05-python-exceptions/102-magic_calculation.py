#!/usr/bin/python3

def magic_calculation(a_param, b_param):
    result_var = 0
    for i_var in range(1, 3):
        try:
            if i_var > a_param:
                raise Exception('Too far')
            else:
                result_var += a_param ** b_param / i_var
        except Exception:
            result_var = b_param + a_param
            break
    return result_var
