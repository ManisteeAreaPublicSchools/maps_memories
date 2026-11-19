"""Shared MAPS course-first naming rules; mirrored offline in CPM Tools."""
import re
PREFIX={'algebra1':'Alg1','apcalc':'APCalc','physics':'Phy'}
def artifact_name(course,lesson,resource='Lesson',audience='',extension='pdf'):
    prefix=PREFIX[course]
    if any(not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*',x or '') for x in (lesson,resource)):
        raise ValueError('Invalid artifact token')
    if audience not in ('','Student','Teacher') or extension not in ('pdf','html','css','svg','js'):
        raise ValueError('Invalid audience or extension')
    return '_'.join([prefix,lesson,resource]+([audience] if audience else []))+'.'+extension

def validate_artifact_name(name,course):
    return bool(isinstance(name,str) and name.startswith(PREFIX[course]+'_') and re.fullmatch(r'[A-Za-z0-9._-]+\.(?:pdf|html|css|svg|js)',name) and len(name.split('_'))>=3)
