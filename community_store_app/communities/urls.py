from django.urls import path
from . import views

urlpatterns = [
    # Index communities
    path('my-communities/', views.my_communities, name="my-communities"),
    # Show community / Index products
    path('my-communities/<int:community_id>/', views.community_page, name="community-page"),
    # Create community
    path('my-communities/', views.create_community, name="create-community"),
    # Create membership
    path('join-community/', views.join_community, name="join-community"),
    # Index
    path('my-communities/<str:community_name>/pending-requests/', views.pending_requests, name="pending-requests"),
    # Show product
    path('my-communities/<str:community_name>/<int:product_id>/', views.product_page, name="product"),
    path('basket/', views.basket_page, name="basket"),
    # Create product
    path('my-communities/<str:community_name>/', views.add_product, name="add-product")
]
