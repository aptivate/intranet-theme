from django_tables2 import tables
class DocumentsAuthoredTable(tables.Table):
    """
    Basically the same as search.search.SearchTable, but copied here
    in order to avoid introducing a dependency.
    """
    
    title = tables.Column(verbose_name="Title")
    authors = tables.Column(verbose_name="Authors")
    created = tables.Column(verbose_name="Date Added")
    programs = tables.Column(verbose_name="Programs")
    document_type = tables.Column(verbose_name="Document Type")
    
    def render_title(self, value, record):
        # print "record = %s (%s)" % (record, dir(record))
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='%s'>%s</a>" % (record.get_absolute_url(),
            value))

    def render_authors(self, value):
        users = value.all()
        return ', '.join([user.full_name for user in users])
    
    def render_programs(self, value):
        programs = value.all()
        return ', '.join([program.name for program in programs])
    
    def render_document_type(self, value):
        return value.name
    
    class Meta:
        attrs = {'class': 'paleblue'}
        sortable = False # doesn't make sense on a form, would lose changes

from django.forms.widgets import Widget
class DocumentsAuthoredWidget(Widget):
    """
    A widget that displays documents authored by the user being viewed.
    Actually the data is initialised by
    IntranetUserReadOnlyForm.get_documents_authored(), and just rendered
    into a table here. 
    """

    has_readonly_view = True
    def render(self, name, value, attrs=None):
        table = DocumentsAuthoredTable(value)
        
        if 'return_table' in attrs:
            return table
        else:
            return table.as_html()

from django import forms        
class DocumentsAuthoredField(forms.Field):
    """
    A field that displays documents authored by the user being viewed.
    Actually the data is initialised by
    IntranetUserReadOnlyForm.get_documents_authored(), and just rendered here. 
    """
    widget = DocumentsAuthoredWidget

class ProgramWithProgramTypeWidget(Widget):
    """
    A widget that displays the user's program and their program type.
    """

    has_readonly_view = True
    def render(self, name, value, attrs=None):
        table = DocumentsAuthoredTable(value)
        
        if 'return_table' in attrs:
            return table
        else:
            return table.as_html()
