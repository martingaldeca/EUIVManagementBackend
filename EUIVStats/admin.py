from django.contrib import admin

from .models import EuIVProvinceStats, EuIVCountryStats


@admin.register(EuIVProvinceStats)
class EuIVProvinceStatsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'save_game',
        'stats_date',
        'province',
        'development',
        'base_tax',
        'base_production',
        'base_manpower',
        'trade_power',
        'owner',
        'controller',
        'devastation',
    )
    list_filter = (
        'creation_datetime',
        'modification_datetime',
        'stats_date',
        'save_game',
        'owner',
        'controller'
    )
    search_fields = ('province', 'owner', 'save_game', 'stats_date')
    raw_id_fields = ('save_game', 'province', 'owner', 'controller')


@admin.register(EuIVCountryStats)
class EuIVCountryStatsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'creation_datetime',
        'modification_datetime',
        'save_game',
        'stats_date',
        'country',
        'current_power_projection',
        'great_power_score',
        'development',
        'raw_development',
        'capped_development',
        'realm_development',
        'base_tax',
        'adm_tech',
        'dip_tech',
        'mil_tech',
        'navy_strength',
        'num_owned_home_cores',
        'num_of_controlled_cities',
        'num_of_total_ports',
        'forts',
        'average_effective_unrest',
        'average_autonomy',
        'num_of_allies',
        'prestige',
        'stability',
        'treasury',
        'inflation',
        'total_owned_provinces',
        'total_controlled_provinces',
        'army_tradition',
        'navy_tradition',
        'last_month_income',
        'last_month_expense',
        'estimated_loan',
        'corruption',
        'legitimacy',
        'mercantilism',
        'splendor',
        'army_professionalism',
        'government',
        'manpower',
        'max_manpower',
        'sailors',
        'max_sailors',
        'is_great_power',
        'government_reform_progress',
    )
    list_filter = (
        'creation_datetime',
        'modification_datetime',
        'save_game',
        'stats_date',
        'country',
        'is_great_power',
    )
    search_fields = ('province', 'owner', 'save_game', 'stats_date')
    raw_id_fields = ('save_game', )
