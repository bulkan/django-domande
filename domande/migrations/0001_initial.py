# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table('domande_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_domande.question_set', null=True, to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('domande', ['Question'])

        # Adding model 'TextQuestion'
        db.create_table('domande_textquestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domande.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('domande', ['TextQuestion'])

        # Adding model 'Choice'
        db.create_table('domande_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('label', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('domande', ['Choice'])

        # Adding model 'ChoiceQuestion'
        db.create_table('domande_choicequestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domande.Question'], unique=True, primary_key=True)),
            ('multichoice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('domande', ['ChoiceQuestion'])

        # Adding M2M table for field choices on 'ChoiceQuestion'
        db.create_table('domande_choicequestion_choices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('choicequestion', models.ForeignKey(orm['domande.choicequestion'], null=False)),
            ('choice', models.ForeignKey(orm['domande.choice'], null=False))
        ))
        db.create_unique('domande_choicequestion_choices', ['choicequestion_id', 'choice_id'])

        # Adding model 'Answer'
        db.create_table('domande_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name='polymorphic_domande.answer_set', null=True, to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['domande.Question'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('domande', ['Answer'])

        # Adding model 'TextAnswer'
        db.create_table('domande_textanswer', (
            ('answer_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domande.Answer'], unique=True, primary_key=True)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('domande', ['TextAnswer'])

        # Adding model 'ChoiceAnswer'
        db.create_table('domande_choiceanswer', (
            ('answer_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['domande.Answer'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('domande', ['ChoiceAnswer'])

        # Adding M2M table for field answer on 'ChoiceAnswer'
        db.create_table('domande_choiceanswer_answer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('choiceanswer', models.ForeignKey(orm['domande.choiceanswer'], null=False)),
            ('choice', models.ForeignKey(orm['domande.choice'], null=False))
        ))
        db.create_unique('domande_choiceanswer_answer', ['choiceanswer_id', 'choice_id'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table('domande_question')

        # Deleting model 'TextQuestion'
        db.delete_table('domande_textquestion')

        # Deleting model 'Choice'
        db.delete_table('domande_choice')

        # Deleting model 'ChoiceQuestion'
        db.delete_table('domande_choicequestion')

        # Removing M2M table for field choices on 'ChoiceQuestion'
        db.delete_table('domande_choicequestion_choices')

        # Deleting model 'Answer'
        db.delete_table('domande_answer')

        # Deleting model 'TextAnswer'
        db.delete_table('domande_textanswer')

        # Deleting model 'ChoiceAnswer'
        db.delete_table('domande_choiceanswer')

        # Removing M2M table for field answer on 'ChoiceAnswer'
        db.delete_table('domande_choiceanswer_answer')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'domande.answer': {
            'Meta': {'object_name': 'Answer'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_domande.answer_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domande.Question']"})
        },
        'domande.choice': {
            'Meta': {'ordering': "['order']", 'object_name': 'Choice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'domande.choiceanswer': {
            'Meta': {'object_name': 'ChoiceAnswer', '_ormbases': ['domande.Answer']},
            'answer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['domande.Choice']", 'symmetrical': 'False'}),
            'answer_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domande.Answer']", 'unique': 'True', 'primary_key': 'True'})
        },
        'domande.choicequestion': {
            'Meta': {'ordering': "['order']", 'object_name': 'ChoiceQuestion', '_ormbases': ['domande.Question']},
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['domande.Choice']", 'symmetrical': 'False'}),
            'multichoice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domande.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        'domande.question': {
            'Meta': {'ordering': "['order']", 'object_name': 'Question'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_domande.question_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'domande.textanswer': {
            'Meta': {'object_name': 'TextAnswer', '_ormbases': ['domande.Answer']},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domande.Answer']", 'unique': 'True', 'primary_key': 'True'})
        },
        'domande.textquestion': {
            'Meta': {'ordering': "['order']", 'object_name': 'TextQuestion', '_ormbases': ['domande.Question']},
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['domande.Question']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['domande']