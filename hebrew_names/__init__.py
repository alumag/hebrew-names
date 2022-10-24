from os.path import abspath, join, dirname
import codecs
import random


__title__ = 'hebrew_names'
__version__ = '0.0.1'
__author__ = 'Aluma Gelbard'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:jew:male': full_path('dist.jew.male.first'),
    'first:jew:female': full_path('dist.jew.female.first'),
    'last:jew': full_path('dist.jew.last'),
    'first:muslim:male': full_path('dist.muslim.male.first'),
    'first:muslim:female': full_path('dist.muslim.female.first'),
    'last.muslim': full_path('dist.muslim.last'),
    'first:christian:male': full_path('dist.christian.male.first'),
    'first:christian:female': full_path('dist.christian.female.first'),
    'last:christian': full_path('dist.christian.last'),
    'first:druze:male': full_path('dist.druze.male.first'),
    'first:druze:female': full_path('dist.druze.female.first'),
    'last:druze': full_path('dist.druze.last'),
    'first:other:male': full_path('dist.other.male.first'),
    'first:other:female': full_path('dist.other.female.first'),
    'last:other': full_path('dist.other.last'),
}


def get_name(filename):
    selected = random.random() * 100
    with codecs.open(filename, 'r', 'utf-16') as name_file:
        for line in name_file:
            name, _, _, cumulative, _ = line.split('\t')
            if float(cumulative) >= selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(ethnicity=None, gender=None):
    if ethnicity is None:
        ethnicity = random.choice(('jew', 'muslim', 'christian', 'druze', 'other'))
    if ethnicity not in ('jew', 'muslim', 'christian', 'druze', 'other'):
        raise ValueError("Only 'jew', 'muslim', 'christian', 'druze' and 'other' are supported as ethnicity")
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES[f'first:{ethnicity}:{gender}'])


def get_last_name(ethnicity=None):
    raise NotImplementedError('get_last_name is not implemented')

    if ethnicity is None:
        ethnicity = random.choice(('jew', 'muslim', 'christian', 'druze', 'other'))
    if ethnicity not in ('jew', 'muslim', 'christian', 'druze', 'other'):
        raise ValueError("Only 'jew', 'muslim', 'christian', 'druze' and 'other' are supported as ethnicity")
    return get_name(FILES[f'last:${ethnicity}'])


def get_full_name(ethnicity=None, gender=None):
    raise NotImplementedError('get_full_name is not implemented')

    return "{0} {1}".format(get_first_name(ethnicity, gender), get_last_name(ethnicity))
