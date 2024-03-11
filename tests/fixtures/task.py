from prompting.tasks import Task, QuestionAnsweringTask, SummarizationTask, DebuggingTask, MathTask, DateQuestionAnsweringTask
from prompting.tools import Context
from .dataset import WIKI_CONTEXT, CODING_CONTEXT, MATH_CONTEXT, DATEQA_CONTEXT

TASKS = [
        QuestionAnsweringTask,
        SummarizationTask,
        DebuggingTask,
        MathTask,
        DateQuestionAnsweringTask,
    ]

CONTEXTS = {
    QuestionAnsweringTask: WIKI_CONTEXT,
    SummarizationTask: WIKI_CONTEXT,
    DebuggingTask: CODING_CONTEXT,
    MathTask:  MATH_CONTEXT,
    DateQuestionAnsweringTask: DATEQA_CONTEXT,
}

TASK_FIELDS = {
'name': str,
'desc': str,
'goal': str,
'query': str,
'topic': str,
'subtopic': str,
'tags': list,
'context': Context,
'reward_definition': list,
'reference': str,
#'reward_threshold': float ,
'penalty_definition': list,
# 'criteria': str = ("",),
'delimiter': str,
'complete': bool,
'static_reference': bool,
'static_query': bool,
'reference_system_prompt': str,
'reference_prompt': str,
'query_system_prompt': str,
'query_prompt': str,
}