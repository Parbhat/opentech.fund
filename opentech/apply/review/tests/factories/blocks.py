import json
import random
import factory

from opentech.apply.review import blocks
from opentech.apply.review.options import YES, MAYBE, NO
from opentech.apply.stream_forms.testing.factories import FormFieldBlockFactory, CharFieldBlockFactory, \
    StreamFieldUUIDFactory
from opentech.apply.utils.testing.factories import RichTextFieldBlockFactory

__all__ = ['ReviewFormFieldsFactory', 'RecommendationBlockFactory', 'ScoreFieldBlockFactory']


class RecommendationBlockFactory(FormFieldBlockFactory):
    class Meta:
        model = blocks.RecommendationBlock

    @classmethod
    def make_answer(cls, params=dict()):
        return random.choices([NO, MAYBE, YES])


class RecommendationCommentsBlockFactory(FormFieldBlockFactory):
    class Meta:
        model = blocks.RecommendationCommentsBlock


class ScoreFieldBlockFactory(FormFieldBlockFactory):
    class Meta:
        model = blocks.ScoreFieldBlock

    @classmethod
    def make_answer(cls, params=dict()):
        return json.dumps([random.randint(0, 5), factory.Faker('word').generate(params)])


ReviewFormFieldsFactory = StreamFieldUUIDFactory({
    'char': CharFieldBlockFactory,
    'rich_text': RichTextFieldBlockFactory,
    'scored_answer': ScoreFieldBlockFactory,
    'recommendation': RecommendationBlockFactory,
    'recommendation_comments': RecommendationCommentsBlockFactory,
})