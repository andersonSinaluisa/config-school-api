from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    objects = models.Manager()
    class Meta:
        abstract = True
        
        
class LevelModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'level'
        verbose_name = 'Level'
        ordering = ['order']




class CourseModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    level = models.ForeignKey(LevelModel, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        

class CourseSubjectModel(BaseModel):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='course_subjects')
    subject = models.ForeignKey('SubjectModel', on_delete=models.CASCADE, related_name='course_subjects')
    hoursPerWeek = models.TimeField(default='00:00:00')
    isRequired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.subject.name}"

    class Meta:
        db_table = 'course_subject'
        verbose_name = 'Course Subject'
        unique_together = ('course', 'subject')
        

class ParallelModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='parallels')
    capacity = models.IntegerField()
    section = models.ForeignKey('SectionModel', on_delete=models.CASCADE, related_name='parallels')
    schoolYear = models.ForeignKey('SchoolYearModel', on_delete=models.CASCADE, related_name='parallels')
    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'parallel'
        verbose_name = 'Parallel'
        unique_together = ('name', 'course', 'section', 'schoolYear')
        verbose_name_plural = 'Parallels'
        ordering = ['name']
        

class SchoolYearModel(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('planning', 'Planning'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='planning')

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'school_year'
        verbose_name = 'School Year'
        ordering = ['startDate']
        

class SectionModel(BaseModel):
    TYPE_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('weekend', 'Weekend'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='morning')
    description = models.TextField(blank=True, null=True)
    startDate = models.TimeField(default='08:00:00')
    endDate = models.TimeField(default='17:00:00')
    hasBreak = models.BooleanField(default=False)
    breakCount = models.IntegerField(default=0)
    breakDuration = models.IntegerField(default=0)
    days = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated list of days
    
    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'section'
        verbose_name = 'Section'
        ordering = ['name']
        

class SubjectModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    hoursPerWeek = models.IntegerField()

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'subject'
        verbose_name = 'Subject'
        ordering = ['name']
        
        
class LogActivityModel(BaseModel):
    id = models.AutoField(primary_key=True)
    userId = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.userId} - {self.action} - {self.timestamp}"

    class Meta:
        db_table = 'log_activity'
        verbose_name = 'Log Activity'
        ordering = ['-timestamp']


class ConfigurationModel(BaseModel):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.key} - {self.value}"

    class Meta:
        db_table = 'configuration'
        verbose_name = 'Configuration'
        ordering = ['key']


class GradingSystemModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    numberOfTerms = models.IntegerField()
    passingScore = models.DecimalField(max_digits=5, decimal_places=2, default=7.00)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'grading_system'
        verbose_name = 'Grading System'
        verbose_name_plural = 'Grading Systems'
        ordering = ['name']


class GradingTermModel(BaseModel):
    id = models.AutoField(primary_key=True)
    gradingSystem = models.ForeignKey(GradingSystemModel, on_delete=models.CASCADE, related_name='terms')
    academicYear = models.ForeignKey('SchoolYearModel', on_delete=models.CASCADE, related_name='grading_terms')
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.gradingSystem.name} - {self.name}"

    class Meta:
        db_table = 'grading_term'
        verbose_name = 'Grading Term'
        verbose_name_plural = 'Grading Terms'
        ordering = ['order']


class EvaluationTypeModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'evaluation_type'
        verbose_name = 'Evaluation Type'
        verbose_name_plural = 'Evaluation Types'
        ordering = ['name']


class MeetingTypeModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'meeting_type'
        verbose_name = 'Meeting Type'
        verbose_name_plural = 'Meeting Types'
        ordering = ['name']


class AttendanceCodeModel(BaseModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)
    affectsGrade = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.description}"

    class Meta:
        db_table = 'attendance_code'
        verbose_name = 'Attendance Code'
        verbose_name_plural = 'Attendance Codes'
        ordering = ['code']


class BehaviorScaleModel(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    minScore = models.DecimalField(max_digits=5, decimal_places=2)
    maxScore = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = 'behavior_scale'
        verbose_name = 'Behavior Scale'
        verbose_name_plural = 'Behavior Scales'
        ordering = ['name']


class ClassScheduleModel(BaseModel):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='class_schedules')
    parallel = models.ForeignKey(ParallelModel, on_delete=models.CASCADE, related_name='class_schedules')
    schoolYear = models.ForeignKey(SchoolYearModel, on_delete=models.CASCADE, related_name='class_schedules')
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, related_name='class_schedules')
    dayOfWeek = models.CharField(max_length=9, choices=DAY_CHOICES)
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self):
        return f"{self.parallel.name} - {self.subject.name} ({self.dayOfWeek})"

    class Meta:
        db_table = 'class_schedule'
        verbose_name = 'Class Schedule'
        verbose_name_plural = 'Class Schedules'
        unique_together = ('parallel', 'dayOfWeek', 'startTime')
        ordering = ['dayOfWeek', 'startTime']


class AcademicPlanningModel(BaseModel):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(
        CourseModel, on_delete=models.CASCADE, related_name='academic_plannings'
    )
    parallel = models.ForeignKey(
        ParallelModel, on_delete=models.CASCADE, related_name='academic_plannings'
    )
    schoolYear = models.ForeignKey(
        SchoolYearModel, on_delete=models.CASCADE, related_name='academic_plannings'
    )
    subject = models.ForeignKey(
        SubjectModel, on_delete=models.CASCADE, related_name='academic_plannings'
    )
    topic = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name} - {self.topic}"

    class Meta:
        db_table = 'academic_planning'
        verbose_name = 'Academic Planning'
        verbose_name_plural = 'Academic Plannings'
        unique_together = ('parallel', 'subject', 'startDate')
        ordering = ['startDate']
