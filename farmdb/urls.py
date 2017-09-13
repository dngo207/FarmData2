from django.conf.urls import url, include
from . import views

app_name = 'farmdb'

urlpatterns = [
    url(r'^login/', views.login_user, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout_user, name='logout'),

    # CreateViews
    url(r'^create/AnimalGroup$', views.AnimalGroupCreateView.as_view(), name="AnimalGroupCreate"),
    url(r'^create/Breed$', views.BreedCreateView.as_view(), name="BreedCreate"),
    url(r'^create/AnimalSubGroup$', views.AnimalSubGroupCreateView.as_view(), name="AnimalSubGroupCreate"),
    url(r'^create/Origin$', views.OriginCreateView.as_view(), name="OriginCreate"),
    url(r'^create/Animal$', views.AnimalCreateView.as_view(), name="AnimalCreate"),
    url(r'^create/Reason$', views.ReasonCreateView.as_view(), name="ReasonCreate"),
    url(r'^create/Vet$', views.VetCreateView.as_view(), name="VetCreate"),
    url(r'^create/Medication$', views.MedicationCreateView.as_view(), name="MedicationCreate"),
    url(r'^create/MedsGiven$', views.MedsGivenCreateView.as_view(), name="MedsGivenCreate"),
    url(r'^create/EggLog$', views.EggLogCreateView.as_view(), name="EggLogCreate"),
    url(r'^create/Wormer$', views.WormerCreateView.as_view(), name="WormerCreate"),
    url(r'^create/SheepCare$', views.SheepCareCreateView.as_view(), name="SheepCareCreate"),
    url(r'^create/Forage$', views.ForageCreateView.as_view(), name="ForageCreate"),
    url(r'^create/Paddock$', views.PaddockCreateView.as_view(), name="PaddockCreate"),
    url(r'^create/Note$', views.NoteCreateView.as_view(), name="NoteCreate"),
    url(r'^create/Sale$', views.SaleCreateView.as_view(), name="SaleCreate"),
    url(r'^create/SlayHouse$', views.SlayHouseCreateView.as_view(), name="SlayHouseCreate"),
    url(r'^create/Slaughter$', views.SlaughterCreateView.as_view(), name="SlaughterCreate"),
    url(r'^create/OtherDest$', views.OtherDestCreateView.as_view(), name="OtherDestCreate"),
    url(r'^create/OtherReason$', views.OtherReasonCreateView.as_view(), name="OtherReasonCreate"),
    url(r'^create/OtherRemove$', views.OtherRemoveCreateView.as_view(), name="OtherRemoveCreate"),
    url(r'^create/FeedType$', views.FeedTypeCreateView.as_view(), name="FeedTypeCreate"),
    url(r'^create/FeedUnit$', views.FeedUnitCreateView.as_view(), name="FeedUnitCreate"),
    url(r'^create/FeedSubtype$', views.FeedSubtypeCreateView.as_view(), name="FeedSubtypeCreate"),
    url(r'^create/Vendor$', views.VendorCreateView.as_view(), name="VendorCreate"),
    url(r'^create/FeedPurchase$', views.FeedPurchaseCreateView.as_view(), name="FeedPurchaseCreate"),

    # List views
    url(r'^list/Animal$', views.AnimalListView.as_view(), name='AnimalList'),
    url(r'^list/Reason$', views.ReasonListView.as_view(), name='ReasonList'),
    url(r'^list/AnimalGroup$', views.AnimalGroupListView.as_view(), name='AnimalGroupList'),
    url(r'^list/Breed$', views.BreedListView.as_view(), name='BreedList'),
    url(r'^list/AnimalSubGroup$', views.AnimalSubGroupListView.as_view(), name='AnimalSubGroupList'),
    url(r'^list/Origin$', views.OriginListView.as_view(), name='OriginList'),
    url(r'^list/Animal$', views.AnimalListView.as_view(), name='AnimalList'),
    url(r'^list/Reason$', views.ReasonListView.as_view(), name='ReasonList'),
    url(r'^list/Vet$', views.VetListView.as_view(), name='VetList'),
    url(r'^list/Medication$', views.MedicationListView.as_view(), name='MedicationList'),
    url(r'^list/MedsGiven$', views.MedsGivenListView.as_view(), name='MedsGivenList'),
    url(r'^list/EggLog$', views.EggLogListView.as_view(), name='EggLogList'),
    url(r'^list/Wormer$', views.WormerListView.as_view(), name='WormerList'),
    url(r'^list/SheepCare$', views.SheepCareListView.as_view(), name='SheepCareList'),
    url(r'^list/Forage$', views.ForageListView.as_view(), name='ForageList'),
    url(r'^list/Paddock$', views.PaddockListView.as_view(), name='PaddockList'),
    url(r'^list/Note$', views.NoteListView.as_view(), name='NoteList'),
    url(r'^list/Sale$', views.SaleListView.as_view(), name='SaleList'),
    url(r'^list/SlayHouse$', views.SlayHouseListView.as_view(), name='SlayHouseList'),
    url(r'^list/Slaughter$', views.SlaughterListView.as_view(), name='SlaughterList'),
    url(r'^list/OtherDest$', views.OtherDestListView.as_view(), name='OtherDestList'),
    url(r'^list/OtherReason$', views.OtherReasonListView.as_view(), name='OtherReasonList'),
    url(r'^list/OtherRemove$', views.OtherRemoveListView.as_view(), name='OtherRemoveList'),
    url(r'^list/FeedType$', views.FeedTypeListView.as_view(), name='FeedTypeList'),
    url(r'^list/FeedUnit$', views.FeedUnitListView.as_view(), name='FeedUnitList'),
    url(r'^list/FeedSubtype$', views.FeedSubtypeListView.as_view(), name='FeedSubtypeList'),
    url(r'^list/Vendor$', views.VendorListView.as_view(), name='VendorList'),
    url(r'^list/FeedPurchase$', views.FeedPurchaseListView.as_view(), name='FeedPurchaseList'),
    url(r'^list/Destination$', views.DestinationListView.as_view(), name='DestinationList'),

    # DetailViews

    # UpdateViews
    url(r'^update/OtherDest/(?P<pk>\d+)/$', views.OtherDestUpdateView.as_view(), name='OtherDestUpdate'),


    # DeleteViews
    url(r'^delete/AnimalGroup/(?P<pk>\d+)/$', views.AnimalGroupDelete.as_view(), name='AnimalGroupDelete'),
    url(r'^delete/Breed/(?P<pk>\d+)/$', views.BreedDelete.as_view(), name='BreedDelete'),
    url(r'^delete/AnimalSubGroup/(?P<pk>\d+)/$', views.AnimalSubGroupDelete.as_view(), name='AnimalSubGroupDelete'),
    url(r'^delete/Origin/(?P<pk>\d+)/$', views.OriginDelete.as_view(), name='OriginDelete'),
    url(r'^delete/Animal/(?P<pk>\d+)/$', views.AnimalDelete.as_view(), name='AnimalDelete'),
    url(r'^delete/Reason/(?P<pk>\d+)/$', views.ReasonDelete.as_view(), name='ReasonDelete'),
    url(r'^delete/Vet/(?P<pk>\d+)/$', views.VetDelete.as_view(), name='VetDelete'),
    url(r'^delete/Medication/(?P<pk>\d+)/$', views.MedicationDelete.as_view(), name='MedicationDelete'),
    url(r'^delete/MedsGiven/(?P<pk>\d+)/$', views.MedsGivenDelete.as_view(), name='MedsGivenDelete'),
    url(r'^delete/EggLog/(?P<pk>\d+)/$', views.EggLogDelete.as_view(), name='EggLogDelete'),
    url(r'^delete/Wormer/(?P<pk>\d+)/$', views.WormerDelete.as_view(), name='WormerDelete'),
    url(r'^delete/SheepCare/(?P<pk>\d+)/$', views.SheepCareDelete.as_view(), name='SheepCareDelete'),
    url(r'^delete/Forage/(?P<pk>\d+)/$', views.ForageDelete.as_view(), name='ForageDelete'),
    url(r'^delete/Paddock/(?P<pk>\d+)/$', views.PaddockDelete.as_view(), name='PaddockDelete'),
    url(r'^delete/Note/(?P<pk>\d+)/$', views.NoteDelete.as_view(), name='NoteDelete'),
    url(r'^delete/Sale/(?P<pk>\d+)/$', views.SaleDelete.as_view(), name='SaleDelete'),
    url(r'^delete/SlayHouse/(?P<pk>\d+)/$', views.SlayHouseDelete.as_view(), name='SlayHouseDelete'),
    url(r'^delete/Slaughter/(?P<pk>\d+)/$', views.SlaughterDelete.as_view(), name='SlaughterDelete'),
    url(r'^delete/OtherDest/(?P<pk>\d+)/$', views.OtherDestDelete.as_view(), name='OtherDestDelete'),
    url(r'^delete/OtherReason/(?P<pk>\d+)/$', views.OtherReasonDelete.as_view(), name='OtherReasonDelete'),
    url(r'^delete/OtherRemove/(?P<pk>\d+)/$', views.OtherRemoveDelete.as_view(), name='OtherRemoveDelete'),
    url(r'^delete/FeedType/(?P<pk>\d+)/$', views.FeedTypeDelete.as_view(), name='FeedTypeDelete'),
    url(r'^delete/FeedUnit/(?P<pk>\d+)/$', views.FeedUnitDelete.as_view(), name='FeedUnitDelete'),
    url(r'^delete/FeedSubtype/(?P<pk>\d+)/$', views.FeedSubtypeDelete.as_view(), name='FeedSubtypeDelete'),
    url(r'^delete/Vendor/(?P<pk>\d+)/$', views.VendorDelete.as_view(), name='VendorDelete'),
    url(r'^delete/FeedPurchase/(?P<pk>\d+)/$', views.FeedPurchaseDelete.as_view(), name='FeedPurchaseDelete'),
    url(r'^delete/Destination/(?P<pk>\d+)/$', views.DestinationDelete.as_view(), name='DestinationDelete'),

    # url(r'^$/', views.index, name='index'),
    # url(r'^$/', views.login_user, name='user_login'),
    # url(r'^$/', views.logout_user, name='user_logout'),

]
