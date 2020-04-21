# Generated by Django 3.0.5 on 2020-04-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EUIVStats', '0002_euivcountrystats'),
    ]

    operations = [
        migrations.AddField(
            model_name='euivcountrystats',
            name='adm_tech',
            field=models.IntegerField(blank=True, help_text='Current administrative technology of the country.', null=True, verbose_name='Administrative technology'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='army_professionalism',
            field=models.FloatField(blank=True, help_text='Current army professionalism of the country.', null=True, verbose_name='Army professionalism'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='army_tradition',
            field=models.FloatField(blank=True, help_text='Current army tradition of the country.', null=True, verbose_name='Army tradition'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='average_autonomy',
            field=models.FloatField(blank=True, help_text='Current autonomy of the country.', null=True, verbose_name='Average autonomy'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='average_effective_unrest',
            field=models.FloatField(blank=True, help_text='Current average unrest of the country.', null=True, verbose_name='Average unrest'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='base_tax',
            field=models.FloatField(blank=True, help_text='Current base tax of the country.', null=True, verbose_name='Base tax'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='capped_development',
            field=models.FloatField(blank=True, help_text='Current capped development of the country.', null=True, verbose_name='Capped development'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='corruption',
            field=models.FloatField(blank=True, help_text='Current corruption of the country.', null=True, verbose_name='Corruption'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='current_power_projection',
            field=models.FloatField(blank=True, help_text='Current power projection of the country.', null=True, verbose_name='Power projection'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='development',
            field=models.FloatField(blank=True, help_text='Current development of the country.', null=True, verbose_name='Development'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='dip_tech',
            field=models.IntegerField(blank=True, help_text='Current diplomatic technology of the country.', null=True, verbose_name='Diplomatic technology'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='estimated_loan',
            field=models.FloatField(blank=True, help_text='Current estimated loan of the country.', null=True, verbose_name='Estimated loan'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='forts',
            field=models.IntegerField(blank=True, help_text='Current forts of the country.', null=True, verbose_name='Forts'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='government',
            field=models.CharField(blank=True, db_index=True, help_text='Current government of the country.', max_length=50, unique=True, verbose_name='Government'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='government_reform_progress',
            field=models.FloatField(blank=True, help_text='Current max sailors of the country.', null=True, verbose_name='Government reform progress'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='great_power_score',
            field=models.FloatField(blank=True, help_text='Current great power score of the country.', null=True, verbose_name='Great power score'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='inflation',
            field=models.FloatField(blank=True, help_text='Current inflation of the country.', null=True, verbose_name='Inflation'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='is_great_power',
            field=models.BooleanField(db_index=True, default=False, help_text='Indicate if the country is great power.', verbose_name='Great power'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='last_month_expense',
            field=models.FloatField(blank=True, help_text='Current last month expense of the country.', null=True, verbose_name='Last month expense'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='last_month_income',
            field=models.FloatField(blank=True, help_text='Current last month income of the country.', null=True, verbose_name='Last month income'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='legitimacy',
            field=models.FloatField(blank=True, help_text='Current legitimacy of the country.', null=True, verbose_name='Legitimacy'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='manpower',
            field=models.FloatField(blank=True, help_text='Current manpower of the country.', null=True, verbose_name='Manpower'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='max_manpower',
            field=models.FloatField(blank=True, help_text='Current max manpower of the country.', null=True, verbose_name='Max manpower'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='max_sailors',
            field=models.FloatField(blank=True, help_text='Current max sailors of the country.', null=True, verbose_name='Max sailors'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='mercantilism',
            field=models.FloatField(blank=True, help_text='Current mercantilism of the country.', null=True, verbose_name='Mercantilism'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='mil_tech',
            field=models.IntegerField(blank=True, help_text='Current military technology of the country.', null=True, verbose_name='Military technology'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='navy_strength',
            field=models.FloatField(blank=True, help_text='Current navy strength of the country.', null=True, verbose_name='Navy strength'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='navy_tradition',
            field=models.FloatField(blank=True, help_text='Current navy tradition of the country.', null=True, verbose_name='Navy tradition'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='num_of_allies',
            field=models.IntegerField(blank=True, help_text='Current total allies of the country.', null=True, verbose_name='Total allies'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='num_of_controlled_cities',
            field=models.IntegerField(blank=True, help_text='Current total controlled cities of the country.', null=True, verbose_name='Total controlled cities'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='num_of_total_ports',
            field=models.IntegerField(blank=True, help_text='Current total ports of the country.', null=True, verbose_name='Total ports'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='num_owned_home_cores',
            field=models.IntegerField(blank=True, help_text='Current total owned home cores of the country.', null=True, verbose_name='Total owned home cores'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='prestige',
            field=models.FloatField(blank=True, help_text='Current prestige of the country.', null=True, verbose_name='Prestige'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='raw_development',
            field=models.FloatField(blank=True, help_text='Current raw development of the country.', null=True, verbose_name='Raw development'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='realm_development',
            field=models.FloatField(blank=True, help_text='Current realm development of the country.', null=True, verbose_name='Realm development'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='sailors',
            field=models.FloatField(blank=True, help_text='Current sailors of the country.', null=True, verbose_name='Sailors'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='splendor',
            field=models.FloatField(blank=True, help_text='Current splendor of the country.', null=True, verbose_name='Splendor'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='stability',
            field=models.FloatField(blank=True, help_text='Current stability of the country.', null=True, verbose_name='Stability'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='total_controlled_provinces',
            field=models.IntegerField(blank=True, help_text='Current total controlled provinces of the country.', null=True, verbose_name='Total controlled provinces'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='total_owned_provinces',
            field=models.IntegerField(blank=True, help_text='Current total owned provinces of the country.', null=True, verbose_name='Total owned provinces'),
        ),
        migrations.AddField(
            model_name='euivcountrystats',
            name='treasury',
            field=models.FloatField(blank=True, help_text='Current treasury of the country.', null=True, verbose_name='Treasury'),
        ),
    ]