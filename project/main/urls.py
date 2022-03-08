from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login-request/$', views.login_request, name='login-request'),
    url(r'^register/$', views.register, name='register'),
    url(r'^myprofile/$', views.my_profile, name='myprofile'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^textbook/(?P<textbook_id>[0-9]+)/$', views.view_product_page, name='product-page'),
    url(r'^profile/(?P<account_username>[a-zA-Z0-9]+)/$', views.view_profile, name='view_profile'),
    url(r'^view-my-listings/$', views.view_my_listings, name="view-my-listings"),
    url(r'^view-credit-cards/$', views.view_credit_cards, name="view-credit-cards"),
    url(r'^add-listing/$', views.add_listing, name="add-listing"),
    url(r'^add-listing-request/$', views.add_listing_request, name="add-listing-request"),
    url(r'^edit-listing-request/$', views.edit_listing_request, name="edit-listing-request"),
    url(r'^cancel-listing-request/$', views.cancel_listing_request, name="cancel-listing-request"),
    url(r'^my-listing/$', views.my_listings, name="my-listing"),
    url(r'^search_results/$', views.search, name="search-results"),
    url(r'^search_results/search-request/$', views.search_request, name="search-request"),
    url(r'^shopping_cart/$', views.view_shopping_cart, name="shopping-cart"),
    url(r'^shopping-cart-delete-request/$', views.shopping_cart_delete, name="shopping-cart-delete"),
    url(r'^add-to-cart-request/$', views.add_to_cart, name="add-to-cart"),
    url('^checkout/$', views.view_checkout, name="checkout"),
    url('^checkout-request/$', views.checkout_request, name="checkout-request"),
    url('^check-payment-info/$', views.check_payment_info, name="check-payment-info"),
    url('^view-orders/$', views.view_orders, name="orders"),
    url(r'^wishlist/$', views.view_wishlist, name="wishlist"),
    url(r'^add-to-wishlist-request/$',views.add_to_wishlist, name="add-to-wishlist"),
    url(r'^remove-from-wishlist-request/$', views.remove_from_wishlist, name="remove-from-wishlist"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
