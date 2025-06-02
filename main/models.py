import uuid

from django.db import models

from authentication.models import User


class TimeStampMixin(models.Model):
    """
    Mixin to add created and updated timestamps to a model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampMixin):
    class ProjectType(models.TextChoices):
        BACKEND = "Back-end"
        FRONTEND = "Front-end"
        iOS = "iOS"
        ANDROID = "Android"

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=ProjectType.choices, default=ProjectType.BACKEND)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributors')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class Issue(TimeStampMixin):
    class IssueStatus(models.TextChoices):
        TODO = "To Do"
        IN_PROGRESS = "In Progress"
        FINISHED = "Finished"

    class IssuePriority(models.TextChoices):
        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"

    class IssueTag(models.TextChoices):
        BUG = "Bug"
        FEATURE = "Feature"
        TASK = "Task"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="issues")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="assigned_issues"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=IssueStatus.choices, default=IssueStatus.TODO)
    tag = models.CharField(max_length=15, choices=IssueTag.choices)
    priority = models.CharField(max_length=15, choices=IssuePriority.choices)

    def __str__(self):
        return self.name


class Comment(TimeStampMixin):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.issue}"
