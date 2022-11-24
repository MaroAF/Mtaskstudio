from django.urls import path

from .views import UserSubscriptionView, CancelSubscriptionView

app_name="accounts"

urlpatterns = [
    path("<str:username>/profile/", UserSubscriptionView.as_view(), name="profile"),
    path("<str:username>/profile/cancel/", CancelSubscriptionView.as_view(), name="cancel-subscription"),
]