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


def validate_lesson_deliverable_name(name, course, extension='pdf'):
    """Validate a self-explanatory Notability/Drive lesson filename.

    Require a course prefix, lesson/date identifier, resource type and audience.
    This intentionally does not change existing IDs or legacy file names.
    """
    prefix=PREFIX.get(course)
    if not prefix or extension not in ('pdf','html') or not isinstance(name,str):
        return False
    pattern=(re.escape(prefix)+
             r'_[A-Za-z0-9][A-Za-z0-9.-]*(?:_[A-Za-z0-9][A-Za-z0-9.-]*)+'
             r'_(?:Student|Teacher)\.'+re.escape(extension))
    return bool(re.fullmatch(pattern,name))


def lesson_pair(course, identifier, resource='Lesson', extension='pdf'):
    """Produce matching student and teacher filenames for a lesson release."""
    student=artifact_name(course,identifier,resource,'Student',extension)
    teacher=artifact_name(course,identifier,resource,'Teacher',extension)
    if not (validate_lesson_deliverable_name(student,course,extension)
            and validate_lesson_deliverable_name(teacher,course,extension)):
        raise ValueError('Course lesson filename needs lesson, resource, and audience')
    return student,teacher
