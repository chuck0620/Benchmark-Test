import random
import time

def get_report(raw_data):
    # evaluates the game_data and calculate the competencies for the report
    my_random = random.uniform(0, 1)

    if 0 <= my_random < 0.001:
        time.sleep(random.uniform(0, 30))

        raise Exception('Unexpected error happened')

    elif 0.001 <= my_random < 0.1:
        time.sleep(random.uniform(0, 0.5))
        report = {'error': 'Did not finished the assessment'}

    elif 0.1 <= my_random < 0.4:
        time.sleep(random.uniform(1, 2))
        calculated_competencies = ['monotony', 'speed', 'accuracy']
        report = {'competencies': {competency: random.randint(1,10) for competency in calculated_competencies}}

    else:
        time.sleep(random.uniform(3, 5))
        calculated_competencies = ['monotony', 'speed', 'accuracy', 'learning', 'conformity']
        report = {'competencies': {competency: random.randint(1,10) for competency in calculated_competencies}}
    
    return report