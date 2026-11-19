
def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(value):
    result = value / 2.54
    return result

def feet_inches_to_cm(feet,inches):
    total_inches = 12 * feet + inches
    result = total_inches * 2.54
    return result

if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
