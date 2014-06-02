import datetime
from haystack import indexes
#from queued_search.indexes import QueuedSearchIndex
from celery_haystack.indexes import CelerySearchIndex
from portal.apps.osac.models import Note

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#class NoteIndex(CelerySearchIndex, indexes.Indexable):    
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')    

    def get_model(self):
        return Note    

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all() #//return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
