ABUSIVE_OR_RUDE = "ABUSIVE_OR_RUDE"
COPYRIGHT = "COPYRIGHT"
LOW_QUALITY = "LOW_QUALITY"
NOT_CONSTRUCTIVE = "NOT_CONSTRUCTIVE"
PLAGIARISM = "PLAGIARISM"
SPAM = "SPAM"
NOT_SPECIFIED = "NOT_SPECIFIED"

FLAG_REASON_CHOICES = [
    (ABUSIVE_OR_RUDE, ABUSIVE_OR_RUDE),
    (COPYRIGHT, COPYRIGHT),
    (LOW_QUALITY, LOW_QUALITY),
    (NOT_CONSTRUCTIVE, NOT_CONSTRUCTIVE),
    (PLAGIARISM, PLAGIARISM),
    (SPAM, SPAM),
    (NOT_SPECIFIED, NOT_SPECIFIED),
]

VERDICT_REASON_CHOICES = FLAG_REASON_CHOICES + [
    (f"NOT_{tup[0]}", f"NOT_{tup[0]}") for tup in FLAG_REASON_CHOICES
]

VERIDCT_OPEN = "OPEN"
VERIDCT_APPROVED = "APPROVED"
VERDICT_REMOVED = "REMOVED"
VERDICT_FILTER_CHOICES = (
    (VERIDCT_OPEN, VERIDCT_OPEN),
    (VERIDCT_APPROVED, VERIDCT_APPROVED),
    (VERDICT_REMOVED, VERDICT_REMOVED),
)
